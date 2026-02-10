<p align="center">
  <h1 align="center">🤖 ProHire AI</h1>
  <p align="center">
    <strong>An AI-Powered Interview & Career Assistant built with Microsoft AutoGen</strong>
  </p>
  <p align="center">
    <a href="#features">Features</a> •
    <a href="#architecture">Architecture</a> •
    <a href="#installation">Installation</a> •
    <a href="#usage">Usage</a> •
    <a href="#project-structure">Project Structure</a> •
    <a href="#configuration">Configuration</a> •
    <a href="#contributing">Contributing</a>
  </p>
</p>

---

## 📌 Overview

**ProHire AI** is an intelligent, multi-agent interview simulation and career counseling platform powered by [Microsoft AutoGen](https://github.com/microsoft/autogen) and OpenAI's GPT-4o. It orchestrates a realistic interview experience using three specialized AI agents that collaborate in a round-robin conversation flow.

Whether you're preparing for a software engineering interview or seeking career guidance, ProHire AI provides a fully interactive, terminal-based experience that challenges you with deep technical questions and delivers actionable career advice — all in real time.

---

## ✨ Features

- 🎯 **Realistic Technical Interviews** — A strict, professional AI interviewer asks deep, structured technical questions across foundational concepts, implementation details, and system design.
- 💬 **Interactive Candidate Participation** — You respond to interview questions in real time via the terminal, just like a live interview.
- 🧭 **Career Counseling** — After the interview, a career counselor agent provides personalized, actionable career advice based on the conversation.
- 🔄 **Multi-Agent Orchestration** — Powered by AutoGen's `RoundRobinGroupChat`, agents take turns seamlessly in a structured conversation flow.
- 💾 **Chat History Persistence** — Save and load interview sessions as JSON for review or continuation.
- ⚙️ **Centralized Configuration** — All settings (model, token limits, rounds) are managed from a single config file.
- 🧩 **Modular Architecture** — Clean separation of agents, models, teams, utilities, and configuration for easy extension.

---

## 🏗️ Architecture

ProHire AI uses a **multi-agent architecture** with three distinct agents coordinated by AutoGen's group chat system:

```
┌─────────────────────────────────────────────────────────────┐
│                        ProHire AI                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌──────────────┐   ┌──────────────┐   ┌───────────────┐  │
│   │  Interviewer  │──▶│  Interviewee │──▶│    Career      │  │
│   │    Agent      │   │   (You)      │   │  Counsellor    │  │
│   │  (GPT-4o)     │◀──│              │◀──│   (GPT-4o)     │  │
│   └──────────────┘   └──────────────┘   └───────────────┘  │
│          │                                      │           │
│          └──────── RoundRobinGroupChat ─────────┘           │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  Config │ Models │ Utils │ Teams                            │
└─────────────────────────────────────────────────────────────┘
```

### Agent Roles

| Agent | Type | Description |
|-------|------|-------------|
| **Interviewer** | `AssistantAgent` | Conducts a strict, professional technical interview with 5–7 questions covering foundational concepts, practical implementation, and system design. |
| **Interviewee** | `UserProxyAgent` | That's you! You respond to questions interactively via the terminal. |
| **Career Counsellor** | `AssistantAgent` | Provides professional, encouraging career advice and guidance based on the interview context. |

---

## 🚀 Installation

### Prerequisites

- **Python 3.10+**
- **OpenAI API Key** ([Get one here](https://platform.openai.com/api-keys))

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/ankushsingh003/ProHire-AI-AUTOGEN_BASED_Interview_career_assistant_GENAI_agent-.git
   cd ProHire-AI-AUTOGEN_BASED_Interview_career_assistant_GENAI_agent-
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux/macOS
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

### What Happens

1. The **Interviewer agent** kicks off the session by asking the first technical question.
2. You (**Interviewee**) type your answer directly in the terminal.
3. The **Career Counsellor** provides career advice and feedback.
4. This round-robin cycle continues for up to **5 rounds** or until the interviewer ends the session with `"TERMINATE"`.

### Example Session

```
────────────────────────────────────────────────────
Interviewer: Question 1 — Explain the difference between 
a process and a thread. When would you use one over the other?
────────────────────────────────────────────────────
> Your answer: A process is an independent execution unit with 
  its own memory space, while a thread shares memory within 
  a process...
────────────────────────────────────────────────────
Career Counsellor: Great foundation! I'd suggest also 
exploring concurrency patterns like async/await for your 
software engineering interviews...
────────────────────────────────────────────────────
```

---

## 📁 Project Structure

```
ProHire-AI/
│
├── main.py                          # Application entry point
├── AI_interview.py                  # Legacy interview orchestration module
├── requirements.txt                 # Python dependencies
├── .env                             # Environment variables (not tracked)
├── .gitignore                       # Git ignore rules
│
├── agents/                          # Agent definitions
│   ├── __init__.py
│   ├── interviewer_agent.py         # Interviewer AI agent
│   ├── interviewee_agent.py         # User proxy agent (candidate)
│   └── career_counsellor_agent.py   # Career counsellor AI agent
│
├── models/                          # LLM client configuration
│   ├── __init__.py
│   └── openAImodel.py               # OpenAI GPT-4o client factory
│
├── config/                          # Centralized settings
│   ├── __init__.py
│   ├── settings.py                  # Global constants & configuration
│   └── models/
│       └── openAImodel.py           # Alternate model client config
│
├── team/                            # Team/group chat orchestration
│   ├── __init__.py
│   └── travel_team.py               # RoundRobinGroupChat team setup
│
├── utils/                           # Utility functions
│   ├── __init__.py
│   └── utils.py                     # Chat history save/load, termination
│
└── tests/                           # Test suite
    ├── __init__.py
    └── agent_test.py                # Agent unit tests
```

---

## ⚙️ Configuration

All configurable parameters are centralized in [`config/settings.py`](config/settings.py):

| Parameter | Default | Description |
|-----------|---------|-------------|
| `MODEL` | `gpt-4o` | OpenAI model to use |
| `MAX_ROUND` | `5` | Maximum conversation rounds |
| `MAX_TURN` | `10` | Maximum turns per agent |
| `MAX_TOKENS` | `1000` | Maximum tokens per response |
| `TERMINATE_MESSAGE` | `TERMINATE` | Keyword to end the interview |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| [Microsoft AutoGen](https://github.com/microsoft/autogen) | Multi-agent orchestration framework |
| [OpenAI GPT-4o](https://openai.com/) | Large Language Model for AI agents |
| [Python](https://python.org/) | Core programming language |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |
| [Pydantic](https://docs.pydantic.dev/) | Data validation & settings management |
| [tiktoken](https://github.com/openai/tiktoken) | Token counting for OpenAI models |

---

## 🧪 Testing

Run the test suite:

```bash
pytest tests/
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Ankush Kumar Singh**

- GitHub: [@ankushsingh003](https://github.com/ankushsingh003)

---

<p align="center">
  Made with ❤️ using Microsoft AutoGen & OpenAI GPT-4o
</p>
