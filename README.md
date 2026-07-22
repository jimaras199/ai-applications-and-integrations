# AI Applications and Integrations

A collection of AI-powered applications and integrations built with the OpenAI API, Python, and modern no-code platforms.

## Current Features

- Connects to the OpenAI Responses API
- Authenticates using the `OPENAI_API_KEY` environment variable
- Generates AI responses from user prompts

## Requirements

- Python 3.14+
- OpenAI Python SDK

## Setup

### Clone the repository

```bash
git clone https://github.com/<your-username>/<repository>.git
```

### Create a virtual environment

```powershell
python -m venv .venv
```

### Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```powershell
pip install -r requirements.txt
```

### Configure the API Key

Create an environment variable named:

```
OPENAI_API_KEY
```

### Run

```powershell
python accessapi.py
```