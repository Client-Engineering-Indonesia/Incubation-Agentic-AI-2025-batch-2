# 🚀 Build Custom Tools using Agent Development Kit (ADK)

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

### Installation Steps

#### 4. Install the ADK with pip

```bash
pip install ibm-watsonx-orchestrate
```

#### 5. Test the Installation

```bash
orchestrate --version
```

---

## 🤖 Build Multiple Agents

### Step 1: Download Assets
📁 Download the provided zip file from the **Lab3 assets** [zip file link]()

### Step 2: Add Orchestrate Environments

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

### Step 3: Configure API Key
🔑 **Input WatsonX.orchestrate API key**

> **Note:** The terminal will not display anything when you paste the API key. Simply copy, paste once, and press Enter.

### Step 4: Verify Environment Setup
```bash
orchestrate env list
```

### Step 5: Activate Your Environment

Choose one of the following environments to activate:

#### Option A: First Environment
```bash
orchestrate env activate New-Agentic-Incubation
```

#### Option B: Second Environment
```bash
orchestrate env activate agentic-inc-3-v2
```

#### Option C: Third Environment
```bash
orchestrate env activate EU-New-Agentic
```

---

## 📊 Agent Overview

### 🛡️ Compliance Agent
The **Compliance Agent** helps check whether user-submitted documents meet the company's terms and conditions.

**Key Benefits:**
- Supports legal and procurement teams
- Simplifies review of import-related documents
- Reduces time-consuming and complex manual reviews
- Speeds up reviews and reduces errors
- Improves overall efficiency

### 📋 Compliance Planner Agent
The **Compliance Planner Agent** creates step-by-step plans or checklists based on company policies and compliance guidelines.

**Purpose:**
- Ensures every required compliance step is accounted for
- Provides structured approach before document evaluation
- Maintains consistency across compliance processes

### 🔍 Document Finder Agent
The **Document Finder Agent** assists users by locating necessary documents for compliance checks.

**Capabilities:**
- Retrieves documents from various sources
- Organizes and prioritizes documents
- Supports both internal and external document sources
- Streamlines compliance verification process

---

## ⚡ Create Workflow

This section demonstrates how to create flows between agents using workflow tools. You can orchestrate agents to work in **sequence** or **parallel** configurations.

---

## 📥 Import Flow and Agents

### Step 1: Rename Agents with Your Initials

#### A. Compliance Plan Generator Agent

1. Copy the following code
2. Paste inside `Compliance_Plan_Generator_Agent.yaml`
3. Replace `<your initials>` with your actual initials
4. Save the file

```yaml
spec_version: v1
kind: native
name: Compliance_Plan_Generator_Agent_<your initials>
description: >
  A specialized agent that provides a procedure to check compliance.

instructions: |
  Generate procedure or step by step process to ensure that statement given by user is comply with the requirement or existing policy.
  Provide required documents and what contents that needed to perform compliance assessment.

  Output this list clearly. Do not add any other information or perform any other tasks.

llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct
style: default
tools:
# - compliance_plan_generator_tools
# - i__get_flow_status_intrinsic_tool__
```

#### B. Compliance System Agent

1. Copy the following code
2. Paste inside `compliance_system.yaml`
3. Replace `<your initials>` with your actual initials
4. Save the file

```yaml
spec_version: v1
kind: native
name: compliance_system_<your initials>
description: >
  You are a compliance system that checks the compliance of documents against a given procedure and references.
instructions: >
  INPUT: The documents given by the user. Try to use the check check_compliance_flow as tools. 
  OUTPUT: results from compliance_Finish_Agent
llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct
style: default
tools:
  - check_compliance_flow_Bisma
  - i__get_flow_status_intrinsic_tool__
```

### Step 2: Import All Components

- Import all agents, tools, and flows at once using the appropriate script:

#### For Environment 1:
```bash
sh import-all_1.sh
```

#### For Environment 2:
```bash
sh import-all_2.sh
```

#### For Environment 3:
```bash
sh import-all_3.sh
```

> 💡 **Tip:** You can import all agents by running the `.sh` script files.

### Step 3: Wait for Import Completion
- Wait until all agents and tools are successfully imported.

![Terminal Import Progress]()

### Step 4: Access the Web Application
- Click the link to access the webApp: [Link webApp orchestrate]()

---

## 🧪 Test the Imported Agent in Watsonx.orchestrate Platform

### Step 1: Navigate to Agent Builder
1. Click the **burger menu** on the top left of the webApp
   
   ![Burger menu WXO](https://github.com/Client-Engineering-Indonesia/Incubation-Agentic-AI-2025-batch-2/blob/main/Lab%203%20-%20Build%20custom%20tools%20using%20Agent%20Development%20Kit%20(ADK)/assets_lab3/Photos/Burger%20menu%20wxo.png)

2. Click **Agent Builder**
   
   ![Agent Builder](https://github.com/Client-Engineering-Indonesia/Incubation-Agentic-AI-2025-batch-2/blob/main/Lab%203%20-%20Build%20custom%20tools%20using%20Agent%20Development%20Kit%20(ADK)/assets_lab3/Photos/Agent%20Builder%20WXO.png)

### Step 2: Open Your Compliance System
3. Find and open the `compliance_system_<your_initials>` agent

![Finding agent](https://github.com/Client-Engineering-Indonesia/Incubation-Agentic-AI-2025-batch-2/blob/main/Lab%203%20-%20Build%20custom%20tools%20using%20Agent%20Development%20Kit%20(ADK)/assets_lab3/Photos/finding%20agent.png)

### Step 3: Test the Agent
4. 💬 Ask questions in the chat interface:
   - 
   - 
   - 
