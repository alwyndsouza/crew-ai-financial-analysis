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

## Project Setup

# Clone the repository
```
git clone https://github.com/alwyndsouza/ai-crewai-multi-agent.git
```

# create virtual environment
```
cd ai-crewai-multi-agent
conda create -n multi-agent python=3.12.8
conda activate multi-agent
```
# install the required packages
```
pip install -r requirements.txt
```
# Run the code
```
python main.py
```

## Final Output

| >>>>> The final answer will look similar to this example: <<<<< |
| --------------------------------------------------------------- |
**Financial Analysis Report**

**Company Overview**
Microsoft Corporation (MSFT) is one of the largest and most influential technology companies worldwide. With its headquarters located in Redmond, Washington, it has become synonymous with innovation and technological advancements.

**Profitability Ratios**

*   **Gross Profit Margin:** 36.3% in the latest fiscal year
*   **Operating Profit Margin:** 28.2% in the latest fiscal year

These metrics indicate a relatively stable profitability trend for MSFT, with gross profit margin slightly increasing over time and operating profit margin showing an upward trend.

**Liquidity Ratios**

*   **Current Ratio:** 1.53 in the latest fiscal year
*   **Quick Ratio:** 0.94 in the latest fiscal year

These ratios suggest that MSFT has sufficient liquidity to meet its short-term obligations, indicating a low risk of default for the company.

**Solvency Ratios**

*   **Debt-to-Equity Ratio:** 0.36 in the latest fiscal year
*   **Interest Coverage Ratio:** 11.4 in the latest fiscal year

These metrics indicate that MSFT has an optimal debt structure, with a manageable level of leverage and sufficient interest coverage ratio to maintain its financial stability.

**Efficiency Ratios**

*   **Asset Turnover Ratio:** 1.45 in the latest fiscal year
*   **Inventory Turnover Ratio:** 4.23 in the latest fiscal year

These ratios suggest that MSFT is efficiently utilizing its assets, resulting in higher revenue and profitability.

**Growth Metrics**

*   **Three-Year Revenue Growth Rate:** 12.1% in the latest fiscal year
*   **Five-Year Revenue Growth Rate:** 13.5% in the latest fiscal year

These growth rates indicate a steady increase in MSFT's revenue, driven by its continued innovation and expansion into new markets.

**Valuation Metrics**

*   **Price-to-Earnings Ratio (P/E):** 30.1 in the latest fiscal year
*   **Enterprise Value/EBITDA:** 13.5 in the latest fiscal year

These valuation metrics suggest that MSFT is slightly overvalued compared to its historical average, indicating potential risks for investors.

**Cash Flow Metrics**

*   **Operating Cash Flow Margin:** 25.1% in the latest fiscal year
*   **Free Cash Flow Yield:** 6.4% in the latest fiscal year

These cash flow metrics indicate that MSFT generates a significant amount of free cash flow, providing flexibility to invest in future growth initiatives.

In conclusion, this financial analysis report provides an in-depth examination of MSFT's financial performance across various key metrics. While it has some areas for improvement, such as its valuation and efficiency ratios, the company's strong profitability, liquidity, solvency, and growth prospects make it a solid investment opportunity for long-term investors.

# Further Improvement to be made - TODO
- add tool to browse the latest news
- add tool to read latest anouncements
- add tool to use technical indicators (macd , rsi, volume profiles, Moving averages etc .. ) and Sector fundamental analysis, seasonal charts
- disply output using streamlit. [chart historical price etc]
- add recommendations and suggestions
- 
