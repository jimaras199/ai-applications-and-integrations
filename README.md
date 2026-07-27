# AI Applications and Integrations

A collection of AI-powered applications and integrations built with the OpenAI API, Python, and modern no-code platforms.

## Current Features

- HTTP-triggered Azure Function
- Integrates with the OpenAI Responses API
- Loads the OpenAI API key from environment configuration
- Structured handling for common OpenAI API errors
- Local execution and deployment to Azure

## Requirements

- Python 3.12
- OpenAI Python SDK
- Azure Functions Core Tools v4
- Azure Functions Python package

## Setup

### Clone the repository

```bash
git clone https://github.com/jimaras199/ai-applications-and-integrations.git
cd ai-applications-and-integrations
```

### Create a virtual environment

```powershell
python -3.12 -m venv .venv
```

### Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```powershell
pip install -r .\Azure-Functions\requirements.txt
```

### Configure local settings

Create the following file:

```text
Azure-Functions/local.settings.json
```

Add:

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "OPENAI_API_KEY": "your-openai-api-key"
  }
}
```

Do not commit `local.settings.json`.

### Run the Function App locally

```powershell
cd .\Azure-Functions
func start
```

The local endpoint will be displayed by Azure Functions Core Tools, typically:

```text
http://localhost:7071/api/greeting
```

## Azure Configuration

The deployed Function App requires an application setting named:

```text
OPENAI_API_KEY
```

Configure it in the Azure portal under the Function App's environment variables or application settings.

Local settings are not automatically deployed to Azure.