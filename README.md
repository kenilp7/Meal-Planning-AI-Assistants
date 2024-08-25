# Meal Planning AI Assistant

## 📌 Overview

The **Meal Planning AI Assistant** is a multi-agent AI system designed to help users generate meal plans while ensuring they stay within a given budget. This project leverages OpenAI's GPT-based models to provide meal suggestions and validate budget constraints using intelligent function tools.

## 📜 Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Agents](#agents)
- [Tools](#tools)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Improvements & Future Enhancements](#improvements--future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/yourusername/meal-planning-ai-assistant.git
cd meal-planning-ai-assistant
```

### 2️⃣ Create & Activate Virtual Environment

```sh
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

---

## 🔧 Configuration

Before running the assistant, set up your **GROQ API Key**:

```python
import os
from getpass import getpass

os.environ["GROQ_API_KEY"] = getpass("Enter GROQ_API_KEY here: ")
```

Alternatively, set it as an environment variable:

```sh
export GROQ_API_KEY="your_api_key"
```

---

## 🤖 Agents

This system includes five AI agents, each designed for specific tasks:

| Agent              | Description                                                      |
| ------------------ | ---------------------------------------------------------------- |
| `BudgetAssistant`  | Ensures meal plans fit within budget constraints.                |
| `BreakfastPlanner` | Suggests breakfast options based on user preferences and budget. |
| `LunchPlanner`     | Generates lunch recommendations with budget awareness.           |
| `DinnerPlanner`    | Plans dinner while maintaining cost-effectiveness.               |
| `SnackPlanner`     | Provides snack suggestions within budget.                        |

---

## 🛠️ Tools

The project includes built-in tools that enhance the AI's functionality.

### **Budget Checker Tool**

A utility to verify if an expense fits within a given budget.

```python
def budget_checker_tool(cost: float, current_budget: float) -> dict:
```

#### **Returns**

```json
{
  "fits_budget": true,
  "message": "The cost of $50.00 fits within your budget."
}
```

---

## 🎯 Usage

Run the meal planning assistant interactively:

```sh
python main.py
```

### **Example Interaction**

```
User: Plan my meals for the day within a $20 budget.
Assistant: Here’s a plan:
- Breakfast: Oatmeal with banana - $3.50
- Lunch: Grilled chicken salad - $7.00
- Dinner: Vegetable stir-fry - $6.00
- Snacks: Apple slices - $2.00
Total: $18.50 (within budget)
```

---

## 📡 API Reference

### **Meal Planning Agents**

Each agent responds with meal suggestions based on dietary needs and budget.

```python
breakfast_agent.system_message
lunch_agent.system_message
dinner_agent.system_message
```

### **Group Chat Management**

Manages agent discussions via a round-robin system.

```python
from autogen_agentchat.teams import RoundRobinGroupChat
team = RoundRobinGroupChat(agents=[budget_agent, breakfast_agent, lunch_agent, dinner_agent, snack_agent])
```

---

## 🚀 Improvements & Future Enhancements

- ✅ **User Preferences**: Add dietary restrictions (vegan, keto, etc.).
- ✅ **Database Integration**: Store user preferences and meal history.
- ✅ **Multi-Language Support**: Expand agent capabilities to different languages.
- ✅ **Mobile-Friendly Interface**: Build a web or mobile UI for meal planning.

---

## 👥 Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

## 📜 License

This project is licensed under the **MIT License**.

