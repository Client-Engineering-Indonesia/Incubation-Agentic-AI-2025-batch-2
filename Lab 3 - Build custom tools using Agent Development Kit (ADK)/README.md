# 🚀 Build Custom Workflow using Agent Development Kit (ADK)

## 📦 Installing the IBM Watsonx Orchestrate ADK

Before installing the ADK, ensure the following software is installed on your system:

### Prerequisites

#### 1. Python
- The ADK is written in Python and requires **Python 3.11 or later**
- The **latest compatible version** is Python **3.13**
- For more information and download, visit the [Python website](https://www.python.org/downloads/)

#### 2. 📋 Pip
- Pip is Python's package manager and is often included with Python
- If pip is not compliant with your Python installation, please see the [Pip documentation](https://pip.pypa.io/en/stable/installation/)

#### 3.  (Optional) Create a Virtual Environment

Use Python's built-in `venv` module to isolate your environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate     # On Windows
```

## Try to run 

### Installation Steps

#### 4. Install the ADK with pip

```bash
pip install ibm-watsonx-orchestrate
```

#### 5. Test the Installation

```bash
orchestrate --version
```

Configure the following environments based on your needs:

#### Environment 1: New Agentic Incubation
```bash
orchestrate env add -n New-Agentic-Incubation -u https://api.dl.watson-orchestrate.ibm.com/instances/20250606-1001-3583-008e-cbf8fc63ad50
```

#### Environment 2: Agentic Inc v2
```bash
orchestrate env add -n agentic-inc-3-v2 -u https://api.dl.watson-orchestrate.ibm.com/instances/20250716-0744-0171-9068-76c0bcc785f2
```

#### Environment 3: EU New Agentic
```bash
orchestrate env add -n EU-New-Agentic -u https://api.eu-central-1.dl.watson-orchestrate.ibm.com/instances/20250606-1011-3513-90be-63ab3ed9d664
```

### Step 6: Configure API Key
🔑 **Input WatsonX.orchestrate API key**

> **Note:** The terminal will not display anything when you paste the API key. Simply copy, paste once, and press Enter.

### Step 7: Verify Environment Setup
```bash
orchestrate env list
```

### Step 8: Activate Your Environment

Choose one of the following environments to activate:

#### 1. First Environment
```bash
orchestrate env activate New-Agentic-Incubation
```

#### 2. Second Environment
```bash
orchestrate env activate agentic-inc-3-v2
```

#### 3. Third Environment
```bash
orchestrate env activate EU-New-Agentic
```

---

## 🤖 Build Workflow

In this session you will try to deploy collaborator agent from this <a href="https://github.com/IBM/ibm-watsonx-orchestrate-adk/tree/main/examples/flow_builder/get_pet_facts">link</a>

### Change Agent Details

under ```agents/pet_agent.yaml``` adjust this code using your name.

```
spec_version: v1
kind: native
name: pet_agent_<YourName>

...

```

### Change Tools Details

1. Under ```tools/cat-facts.openapi.yaml``` adjust this code using your name.

```
openapi: 3.0.3
info:
 title: Get Cat Facts <YourName>

...

```

2. Under ```tools/dog-facts.openapi.yaml``` adjust this code using your name.

```
openapi: 3.0.3
info:
 title: Get Dog Facts <YourName>

...

```

3. Under ```tools/get_pet_facts.py``` adjust this code using your name.

```
@flow(
        name = "get_pet_facts_<YourName>",
        input_schema = Pet,
        output_schema = PetFacts
)

...

```

4. Open your terminal and go to the directory where you put this agent -> execute this command

```
sh import-all.sh
```

5. Go to your enviroment and check if your agent exists in Agent List. You can test your agent by asking "get facts about cat"

### References:
https://developer.watson-orchestrate.ibm.com/
