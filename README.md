# GAIA Agent

An AI agent built with **smolagents** for the Hugging Face Agents Course Unit 4 Final Assignment.

The goal of this project is to create an agent capable of answering GAIA benchmark questions by combining:

- Large Language Models
- Tool usage
- Web search
- File processing
- Data analysis
- Automated evaluation submission

---

## Project Overview

This project implements a GAIA agent that receives questions from the Hugging Face evaluation server, reasons about the task, uses available tools when needed, and submits answers automatically.

The agent architecture:

### Agent Components

*   **LLM Integration:** Utilizes various Large Language Models for reasoning and response generation.
*   **Tool Management:** Implements a system for selecting and executing relevant tools based on the user's query.
*   **Planning & Reasoning:** Employs agentic reasoning steps to decompose complex questions into actionable sub-tasks.
*   **I/O Handling:** Manages input from the evaluation server and output submission formats.

### Tools Utilized

The agent leverages several tools to achieve its goal:

1.  **Web Search Tool:** For gathering external, up-to-date information.
2.  **File Processing Tool:** For reading, parsing, and analyzing local files relevant to the task.
3.  **Data Analysis Tool:** For performing calculations or structured data manipulation on retrieved information.
4.  **LLM Interface:** The core component responsible for dialogue management and decision-making.

### Setup and Installation

To run this project, you will need:

1.  **Dependencies:** Install the required Python libraries (e.g., `smolagents`, necessary LLM frameworks).
2.  **API Keys:** Ensure necessary API keys for web search or other external services are configured in your environment variables.
3.  **Model Configuration:** Specify which LLMs will be used for reasoning and generation.

### Running the Agent

## Running the Agent

The agent execution flow is managed by a central script, typically `main.py`, which orchestrates the interaction between the LLM, tool calls, and the evaluation pipeline.

### Execution Steps

1.  **Initialization:** The script loads the necessary configurations (API keys, model settings) and initializes the agent framework (`smolagents`).
2.  **Input Reception:** It receives the benchmark questions or input data from the Hugging Face evaluation server.
3.  **Task Decomposition & Planning:** The agent uses its reasoning capabilities to analyze the input and determine the necessary sequence of actions (which tools to call and in what order).
4.  **Tool Execution Loop:** The agent enters a loop where it selects an appropriate tool, formulates the necessary arguments, executes the tool, and processes the returned output. This cycle repeats until the final answer is formulated or all required information is gathered.
5.  **Final Answer Formulation & Submission:** Once reasoning is complete, the agent synthesizes the gathered data into a coherent response and formats it for automated submission to the evaluation system.

