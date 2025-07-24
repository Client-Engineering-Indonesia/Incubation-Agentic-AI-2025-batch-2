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

---

## 🤖 Build Multiple Agents

In this session you will try to deploy collaborator agent from this <a href="https://github.com/IBM/ibm-watsonx-orchestrate-adk/tree/main/examples/flow_builder/get_pet_facts">link</a>

To ensure there is no conflict when you create agent, please use this format for your agents and tools

```
<agent name>_<your name>
<tool name>_<your name>
```
