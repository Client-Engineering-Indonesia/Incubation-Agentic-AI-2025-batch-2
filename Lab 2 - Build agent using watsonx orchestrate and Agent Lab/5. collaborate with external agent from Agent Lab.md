# Membuat AI Agent dengan wx.ai Agent Lab

Pada lab ini, Anda akan membuat *Supplier Researcher Agent* menggunakan **watsonx.AI Agent Lab**. Lab ini akan membantu Anda melakukan riset untuk memilih supplier untuk procurement pada Xtralife berdasarkan data performa supplier, procurement rules, dan review pelanggan.

## Tahapan Membuat Agent

### Step 1 — Create a Project
- Apabila ini pertama kalinya Anda menggunakan akun ini, Anda harus membuat project sebelum menggunakan Agent Lab.

![Create Project](https://github.com/user-attachments/assets/f8e14b8a-ad96-4619-8906-dd85231cc87c)

### Step 2 — Mengasosiasikan Watsonx.ai Service
- Setelah membuat project, klik **Manage → Services & Integrations → Associate Service**.
- Pilih **watsonx.ai** dan asosiasikan service **watsonx.ai runtime**.

![Associate Service](https://github.com/user-attachments/assets/ea9b3a8e-558a-458a-90db-c43e7bf4bb88)

### Step 3 — Buat AI Agent
- Klik **New Asset** di sisi kiri dan pilih **Build an AI Agent to Automate Tasks**.

![Build AI Agent](https://github.com/user-attachments/assets/c6dde849-5455-45a8-a82d-9cd11b135933)

### Step 4 - Instruksi ke agent 
Masukan text di **Agent instructions** sesuai dengan kebutuhan dan fungsi yang dibutuhkan

```text
You are a helpful assistant that uses tools to answer questions concisely.
Make sure only to answer questions based on provided data without adding additional informations. Make sure to pass the SQL query completely and always generate reasoning from all your answers based on provided data make the answer concise. 
When greeted, say "Hi, I am watsonx.ai agent. How can I help you?"
```

![Agent Instruction](https://github.com/user-attachments/assets/204a2c02-27f3-4c66-9880-13bc905c9b83)

Kemudian, apabila ada instruction yang lebih spesifik bisa ditambahkan juga ke dalam **Common instructions**.

```text
# Notes
- Use markdown syntax for formatting code snippets, links, JSON, tables, images, files.
- Any HTML tags must be wrapped in block quotes, for example ```<html>```.
- When returning code blocks, specify language.
- Sometimes, things don't go as planned. Tools may not provide useful information on the first few tries. You should always try a few different approaches before declaring the problem unsolvable.
- When the tool doesn't give you what you were asking for, you must either use another tool or a different tool input.
- When using search engines, you try different formulations of the query, possibly even in a different language.
- You cannot do complex calculations, computations, or data manipulations without using tools.
- If you need to call a tool to compute something, always call it instead of saying you will call it.

## Main Notes
You are an Agent with three functions or task:
1. If the question only related to Customer Information then call ProfilingTools then Db2_tools and generate the final answer
2. If the question only related to Reksadana or Manulife Information then call FundsheetQuery then Db2_tools and generate the final answer
3. If the question will relate to both process. In example you need to find information from Reksadana but need information from Profilingtools. Then the process will be ProfilingTools go to Db2_tools pass the result from Db2_tools as cust_info and the question as question, then go to FundsheetQuery and go to db2_tool again and generate the answer
```

![Agent Instruction](https://github.com/user-attachments/assets/062cc7ad-4510-4c08-91cc-9f2b0a94d64d)


### Step 5 — Tambahkan Tools untuk Agent
Di dalam Agent lab watsonx.ai, kita dapat menambahkan tools yang sudah tersedia atau bisa mengkostumisasi tools

- Tools di **Add atool**
  ![Add Tool](https://github.com/user-attachments/assets/31d08bd7-606c-4d93-8eab-47ea54a56f55)

- Tools di **Create custom tool**
  ![Add Tool](https://github.com/user-attachments/assets/74596736-0460-45b7-a394-f7323859826c)

Pada step ini, kita hanya menggunakan custom tool dikarenakan data yang digunakan merupakan data structured yang harus dikoneksikan ke dalam db2. Ada 3 tools yang akan dibuat, **db2tool** sebagai koneksi ke db2; **Fundsheetquery** sebagai data knowledge terkait fund sheet manulife; serta **Customerprofiling** sebagai data knowledge terkait data dummy customer

1. Tool **db2tool**
   - Name: ```db2tool```
     
   - Tool description:

     ```text
      Use this tool, always after we get result from customer profiling and generate the final data, make sure to pass all query to this tool, including the one after '='
     ```
     
   - Input JSON Schema:
     
     ```python
      {
       "query": {
        "title": "query",
        "description": "query generated from previous profiling tools that we need to pass to db2, make sure to pass all query to this tool",
        "type": "string"
       }
      }
     ```
     
   - Python code:
     Ganti **DB2_USERNAME** dan **DB2_PASSWORD** dengan kredensial DB2 Anda
     
     ```python
      def db2_init(query):
          import ibm_db, ibm_db_dbi as dbi
          import pandas as pd
          DB2_HOST = '54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud'
          DB2_PORT = '32733'
          DB2_USERNAME = 'xxx'
          DB2_PASSWORD = 'xxx'
          db2_dsn = 'DATABASE={};HOSTNAME={};PORT={};PROTOCOL=TCPIP;UID={uid};PWD={pwd};SECURITY=SSL'.format(
              'BLUDB',
              DB2_HOST,   
              DB2_PORT,         
              uid=DB2_USERNAME,     
              pwd=DB2_PASSWORD     
          )
          print(db2_dsn)
          db2_connection = dbi.connect(db2_dsn) 
          answer_df = pd.read_sql_query(query, con=db2_connection)
          json_data = answer_df.to_json(orient='records')
          return json_data
     ```

  ![Add Tool](https://github.com/user-attachments/assets/11c42436-9524-4ce2-abcf-76a3f723b103)

2. Tool **Fundsheetquery**
   - Name: ```Fundsheetquery```
     
   - Tool description:

     ```text
      This is a tool that you should use to generate query SQL from table name FUNDSHEET. Call this tool every time you get question related to Reksadana or Manulife
     ```
     
   - Input JSON Schema:
     
     ```python
      {
       "question": {
        "title": "question",
        "description": "question asked by the user that you must use as the input for the tool",
        "type": "string"
       },
       "cust_info": {
        "title": "customer information to check",
        "description": "by default, always set the value as 'null' but if somehow you get value from previous step, then set it up",
        "type": "string"
       }
      }
     ```
     
   - Python code:
     Ganti **apikey** dengan kredensial DB2 Anda
     
     ```python
      def generate_final_answer(question, cust_info):
          import requests
          import ast 
          token_url = "https://iam.cloud.ibm.com/identity/token"
      
          # Headers
          headers = {
              'Content-Type': 'application/x-www-form-urlencoded',
              'Accept': 'application/json'
          }
      
          # Data (form-encoded)
          data = {
              'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
              'apikey': "xxx"
          }
      
          # Make the POST request to get the token
          response = requests.post(token_url, headers=headers, data=data, verify=False)  # verify=False for --insecure
          iam_token = response.json().get('access_token')
          
          # Step 2: Use the token in the scoring request
          scoring_url = "https://us-south.ml.cloud.ibm.com/ml/v1/deployments/70bc7bb4-3003-48aa-893d-2a0b2724f059/text/generation?version=2021-05-01"  # Replace with your actual scoring endpoint
      
          # Headers for the scoring request
          scoring_headers = {
              'Content-Type': 'application/json',
              'Accept': 'application/json',
              'Authorization': f'Bearer {iam_token}'  # Use the token here
          }
      
          # Define the data to be scored
          scoring_data = {
              "parameters": {
                  "prompt_variables": {
                      "question":f"'{question}'",
                      "cust_info":f"'{cust_info}'"# Replace with actual passage
                  }
              }
          }
      
          # Make the scoring request
          scoring_response = requests.post(scoring_url, headers=scoring_headers, json=scoring_data)
          print(scoring_response)
          scoring_response = scoring_response.json()['results'][0]['generated_text']
          scoring_response = ast.literal_eval(scoring_response)['query']
          return scoring_response
     ```

  ![Add Tool](https://github.com/user-attachments/assets/f1209215-b9e4-4664-b494-f28351ed262f)

3. Tool **CustomerProfilling**
   - Name: ```CustomerProfilling```
     
   - Tool description:

     ```text
      Use this tool if the question related to Customer Information then send the result to db2_tool make it as a query.
     ```
     
   - Input JSON Schema:
     
     ```python
        {
         "question": {
          "title": "question",
          "description": "question asked by the user that you must use as the input for the tool",
          "type": "string"
         }
        }
     ```
     
   - Python code:
     Ganti **apikey** dengan kredensial DB2 Anda
     
     ```python
        def generate_final_answer(question):
            import requests
            import ast 
            token_url = "https://iam.cloud.ibm.com/identity/token"
        
            # Headers
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json'
            }
        
            # Data (form-encoded)
            data = {
                'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
                'apikey': "xxx"
            }
        
            # Make the POST request to get the token
            response = requests.post(token_url, headers=headers, data=data, verify=False)  # verify=False for --insecure
            iam_token = response.json().get('access_token')
            
            # Step 2: Use the token in the scoring request
            scoring_url = "https://us-south.ml.cloud.ibm.com/ml/v1/deployments/4575323a-bcf0-4af5-9fa6-f1c868f5d2f3/text/generation?version=2021-05-01"  # Replace with your actual scoring endpoint
        
            # Headers for the scoring request
            scoring_headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': f'Bearer {iam_token}'  # Use the token here
            }
        
            # Define the data to be scored
            scoring_data = {
                "parameters": {
                    "prompt_variables": {
                        "question":f"'{question}'"  # Replace with actual passage
                    }
                }
            }
        
            # Make the scoring request
            scoring_response = requests.post(scoring_url, headers=scoring_headers, json=scoring_data)
            print(scoring_response)
            scoring_response = scoring_response.json()['results'][0]['generated_text']
            scoring_response = ast.literal_eval(scoring_response)['query']
            return scoring_response
     ```

  ![Add Tool](https://github.com/user-attachments/assets/a31c89f0-f58e-4dc4-aa25-49d9122defad)


### Step 6 — Konfigurasi Model & Parameter Agent
Selanjutnya kita bisa untuk mengkonfigurasikan model dan parameter
![Add Tool](https://github.com/user-attachments/assets/3f3f10d8-d993-4694-a12c-e30b54d5b1d7)

- Konfigurasi model
  ![Add Tool](https://github.com/user-attachments/assets/58bd73b3-0777-4e0d-a376-a83d75bd7541)
  
- Konfigurasi parameter
  ![Add Tool](https://github.com/user-attachments/assets/3f3f10d8-d993-4694-a12c-e30b54d5b1d7)
  <img width="1237" alt="image" src="https://github.com/user-attachments/assets/6e4875be-2be3-410f-bac9-bf31c8268673" />

### Step 7 — Test Agent
Coba pertanyaan berikut:
- **Manulife Fundsheet**
  - Sebutkan 5 rekomendasi reksadana dengan Klasifikasi risiko tinggi?
  - Apa saja reksadana paling aman yang bisa ditawarkan?
  - Bandingkan Manulife dana pasar uang dengan schroder dana ekuitas premier?

- **Customer Profile**
  - Siapa saja pelanggan yang total pengeluaran bulan lalu di atas 3 juta rupiah
  - Berapa banyak segmentasi customer yang masuk ke dalam kategori Young Professional?
  - Berapa persentase pelanggan yang statusnya Single, Married, dan Divorced?

- **Customer and Fundsheet**
  - Tolong tampilkan profil lengkap nasabah Iron Man – umur, status, segmen, rata-rata pengeluaran, dan saran produk Manulife yang paling pas
  - Pendapatan saya sekitar tiga setengah juta per bulan, kadang naik-turun karena kerja lepas. Saya butuh produk Manulife yang bisa bantu kumpulin dana kuliah S2 lima tahun lagi, tapi jangan terlalu berisiko tinggi. Apa rekomendasinya?
  - Produk manulife apa yang cocok untuk customer bernama Yoda?
  - Orang tua saya habis haji, mau investasi syariah risiko sedang. Ada opsi obligasi syariah di Manulife?

### Step 8 — Lihat Respon Agent

![Agent Response](https://github.com/user-attachments/assets/6bfe30de-2a57-4415-a3fc-fdba04a3adcb)

### Step 9 — Simpan Agent

![Save Agent](https://github.com/user-attachments/assets/3c0363a7-cfdf-481a-b365-9ccc0fb1686e)

### Step 10 — Export Agent
- Simpan agent ke dalam notebook atau file yang bisa diedit untuk modifikasi selanjutnya.

![Export Agent](https://github.com/user-attachments/assets/3b1d61d0-7285-4621-88cf-8144cee6f598)
![Export Agent](https://github.com/user-attachments/assets/9f92307a-8808-449d-8bcd-3fe73d43258e)

---







