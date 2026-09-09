# Agent ADK Practice

A small practice project for learning the basics of building agents with the
[Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/).

The project currently contains two agents and a simple algebra tutor implemented
in two ways:

- `first_agent/agent.py` - a Python-defined agent using an ADK `Agent`, runner,
	in-memory sessions, and an asynchronous event loop.
- `yaml_agent/root_agent.yaml` - the same basic tutor defined with an ADK YAML
	configuration.
- `customer_support_agent/agent.py` - a customer support agent whose behavior is
	shaped by detailed, structured instructions.

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

## Try the structured-instructions agent

The customer support agent demonstrates how detailed instructions can give an
agent a consistent role, workflow, and response style:

```powershell
adk web customer_support_agent
```

Its instruction uses five reusable patterns:

- **Identity** - defines who the agent is and its expertise.
- **Mission** - explains what the agent is responsible for.
- **Methodology** - gives the agent a repeatable way to work.
- **Boundaries** - defines what the agent will not do and when it should
	escalate.
- **Examples** - demonstrates how the agent should respond in common situations.

The `instruction` parameter is arguably the most important control for shaping
agent behavior. These instruction boundaries add role-specific control on top
of the model's built-in safety settings. Tool-based responses can reduce
hallucinations by grounding answers in facts, while Markdown formatting helps
the model interpret and follow structured instructions consistently, in line
with ADK best practices. The patterns can be mixed and matched for different
agent types.

## Project structure

```text
.
├── first_agent/
│   └── agent.py          # Python-defined math tutor
├── yaml_agent/
│   └── root_agent.yaml   # YAML-defined math tutor
├── customer_support_agent/
│   └── agent.py          # Customer support agent with structured instructions
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
- Design professional agent instructions with reusable patterns
