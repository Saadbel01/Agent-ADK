# Agent ADK Practice

A small practice project for learning the basics of building agents with the
[Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/).

The project currently contains a simple algebra tutor implemented in two ways:

- `first_agent/agent.py` - a Python-defined agent using an ADK `Agent`, runner,
	in-memory sessions, and an asynchronous event loop.
- `yaml_agent/root_agent.yaml` - the same basic tutor defined with an ADK YAML
	configuration.

This is an experimental learning project, not a production application.

## Requirements

- Python 3.14 or newer
- A Google AI API key with access to the configured Gemini model

## Setup

Create and activate a virtual environment, then install the project:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
```

Set your API key in the current PowerShell session:

```powershell
$env:GOOGLE_API_KEY = "your-api-key"
```

For other shells, set `GOOGLE_API_KEY` using that shell's environment-variable
syntax. Do not commit the key to the repository.

## Run the Python agent

The Python example asks the math tutor to solve `2x + 5 = 13` and prints the
agent's response:

```powershell
adk web first_agent
```

The example uses `InMemorySessionService`, so sessions only exist while the
process is running.

## Try the YAML agent

The YAML version can be loaded with the ADK development web interface:

```powershell
adk web yaml_agent
```

Open the local URL printed by the command and select `math_tutor_agent` to
interact with it.

## Project structure

```text
.
├── first_agent/
│   └── agent.py          # Python-defined math tutor
├── yaml_agent/
│   └── root_agent.yaml   # YAML-defined math tutor
├── main.py               # Minimal project entry point placeholder
├── pyproject.toml        # Project metadata and dependencies
└── README.md
```

## Learning goals

- Define an agent with a model and instructions
- Run an agent with the ADK runner
- Create and use in-memory sessions
- Process asynchronous agent events
- Compare Python and YAML agent definitions
