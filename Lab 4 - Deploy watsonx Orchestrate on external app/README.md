# Deploy watsonx Orchestrate on External App

## Install ReactJS

<i>Skip this step if you already have ReactJS environment</i>

1. Install latest version of Node.js and npm from: https://nodejs.org/
2. Verify installation by running this command from terminal

```
node -v
npm -v
```

## Deploy Frontend Locally

1. For this workshop you may use frontend that can be downloaded from <a href="https://github.com/Client-Engineering-Indonesia/Incubation-Agentic-AI-2025-batch-2/blob/main/assets/wxo-frontend.zip">here</a>.
2. Unzip into your local directory
3. Install all required modules by running this command

```
npm install -i
```

4. Run this command to run frontend. 

```
npm start
```

## Deploy Agent

<i>Skip this step if you already deployed your agent</i>

1. Go to watsonx Orchestrate platform -> click Build -> Agent Builder

<img width="1919" height="753" alt="image" src="https://github.com/user-attachments/assets/6fad8df1-f3cf-442a-8299-9e640aca2262" />

2. Select an agent that you want to deploy -> click Deploy at top-right side -> click Deploy button on Deploy Agent window pane

<img width="1791" height="941" alt="image" src="https://github.com/user-attachments/assets/1979754b-9943-49dc-b05c-645e79daf947" />

3. Ensure you can see notification message as below

<img width="289" height="151" alt="image" src="https://github.com/user-attachments/assets/df7611ab-2a68-4da6-80f8-14dc89b25025" />


## Embed watsonx Orchestrate on frontend

1. From your local terminal run this command

```
orchestrate agents list
```

* If you have deployed your agent, you will see that agent in your terminal.

<img width="1411" height="111" alt="image" src="https://github.com/user-attachments/assets/62b73f78-2529-4241-9b2b-6462cf995299" />

2. Run this command to get deployment script

```
orchestrate channels webchat embed --agent-name=ibm_agent
```

* If you are successful, you may script as below from your terminal

```
<script>

window.wxOConfiguration = {
      orchestrationID: "<Your orchestrate instance ID>",
      hostURL: "<Your orchestrate URL>",
      rootElementID: "root",
      showLauncher: true,
      chatOptions: {
agentId: "<Your orchestrate agent ID>",
agentEnvironmentId: "<Your environment ID>"
}
  };

  setTimeout(function () {
      const script = document.createElement('script');
      script.src = `${window.wxOConfiguration.hostURL}/wxochat/wxoLoader.js?embed=true`;
      script.addEventListener('load', function () {
          wxoLoader.init();
      });
      document.head.appendChild(script);
  }, 0);

*/
    
</script>
```

3. Now go back to your ReactJS directory and open this file: ```wxo-frontend/public/index.html``` and find the script section as image below

<img width="711" height="504" alt="image" src="https://github.com/user-attachments/assets/fd8aeefb-19ff-4506-8cd7-1c3d8891575d" />

4. Replace orchestrate instance ID, orchestrate URL, orchestrate agent ID, environment ID with your generated script -> uncomment it -> if you go to your frontend, you will see launcher icon at bottom-right side

<img width="1920" height="976" alt="image" src="https://github.com/user-attachments/assets/d8bee654-758f-42d9-af7b-8d2be0ccebc3" />

  
