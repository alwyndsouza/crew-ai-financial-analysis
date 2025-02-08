# Multi AI agent system for financial analysis with crewAI

This example leverages the **Ollama/llama3.1 model** and **SEC-API** to generate reports on publicly traded companies based on their filings with the U.S. Securities and Exchange Commission (SEC). SEC filings are regulatory documents that companies and issuers of securities must submit regularly.

> **Disclaimer:** This example is for demonstration and educational purposes only. It should not be construed as legal, tax, investment, financial, or other advice.

# crewAI Framework

**crewAI** is an open-source framework designed to orchestrate role-playing autonomous AI agents, enabling them to collaborate seamlessly on complex tasks.

- **Roles and Tools:** Each AI agent can assume different roles, such as Financial Researcher or Financial Analyst, and can be equipped with various tools for data collection and processing, either from the web or via APIs. crewAI supports both custom tools and existing tools from the LangChain library.
  
- **Team Dynamics:** Agents can operate in teams (crews), working together in a sequential workflow (where the output of one agent serves as the input for another) or within a hierarchical organization (where agents are coordinated and instructed by a "manager").

## Key Components of crewAI

| Components | Description |
| ---------- | ----------- |
| **Crew**   | A crew in crewAI represents a collaborative group of agents working together to achieve a set of tasks. A crew defines the strategy for task execution, agent collaboration, and the overall workflow. |
| **Agents** | Agents are the building blocks of a crew. Each agent has a role, goal, and backstory. This context helps guide the agent's decisions and responses. |
| **Tools**  | Agents can be augmented with custom tools that enhance their capabilities. These tools can be anything from information retrieval modules to data analysis scripts. The agents in this example use the SEC-API tools from the crewAI examples library. These tools download SEC filing reports and then process the reports with Meta's (Facebook's) "FAISS" (Facebook AI Similarity Search) vector store for similarity (semantic) search. They use Central Processing Unit (CPU) only and do not require any Graphic Processing Unit (GPU). |
| **Tasks**  | A crew needs to accomplish tasks. Each task can be assigned to one or more specific agent(s) based on their expertise. |
| **Processes** | Complex tasks can be broken down into smaller, more manageable processes. They orchestrate the flow of information between agents. This example follows a sequential process. |

This example allows you to set the company stock symbol of the company that you want to analyze in the `main.py` script. It is currently set to `MSFT`, which is the company stock symbol for Microsoft Corp.

You also need a free SEC-API key for this example to download the SEC filings. [Get your free SEC-API key here](https://sec-api.io/login).
You can insert your SEC-API key in the `main.py` script, or you can supply your SEC-API key either via the `.env` file, or through an environment variable called `SEC_API_API_KEY`.


# Further Improvement to be made - TODO
- add tool to browse the latest news
- add tool to read latest anouncements
- add tool to use technical indicators (macd , rsi, volume profiles, Moving averages etc .. ) and Sector fundamental analysis, seasonal charts
- disply output using streamlit. [chart historical price etc]
- add recommendations and suggestions
- 
