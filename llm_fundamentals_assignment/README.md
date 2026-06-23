# Practical Assignment – LLM Fundamentals & APIs

This repository contains the completed implementation for the LLM Fundamentals & APIs assignment. 
As requested, all 4 tasks have been consolidated into a single Jupyter Notebook. 

The implementation uses the **Groq API** (for extremely fast inference) and the **Google Gemini API**.

## Files in this Directory

- `llm_assignment.ipynb`: The master notebook containing all implementation code.
- `requirements.txt`: Python package requirements.
- `.env.example`: Template for API keys.
- **Generated Outputs:**
  - `llm_comparisons.csv`: Output table comparing the responses, times, and lengths between Groq (Llama-3) and Gemini / Groq Mixtral.
  - `prompt_engineering_results.json`: 5 different prompt variations on the BBC News dataset and their generated results.
  - `token_usage_logs.csv`: Tracker logs showing token usage and estimated API cost.

## Tasks Completed

1. **Multi-LLM Response Comparison Tool**: Prompts two different LLM models and outputs the comparison metrics (time, length, content) to `llm_comparisons.csv`.
2. **Prompt Engineering Playground**: Downloads the BBC News dataset and tests 5 distinct summarization prompts. Results are saved in `prompt_engineering_results.json` along with markdown analysis.
3. **Streaming AI Chat Assistant**: Simulates a chatbot directly inside the Jupyter Notebook, implementing streaming to print output token-by-token.
4. **Token Usage and Cost Tracker**: A custom tracking utility that calculates input/output tokens using `tiktoken` (cl100k_base equivalent) and applies standard API pricing to generate a final cost report in `token_usage_logs.csv`.

## How to Run

1. Make sure you have Anaconda or Python installed.
2. Install the requirements: `pip install -r requirements.txt`
3. Duplicate `.env.example` to `.env` and insert your API keys.
4. Run `jupyter lab` or `jupyter notebook` and execute all cells in `llm_assignment.ipynb`.

## Screenshots

### 1. Multi-LLM Comparison
![Multi-LLM Comparison](screenshots/Multi-LLM%20Comparison.png)

### 2. Prompt Engineering
![Prompt Engineering](screenshots/Prompt%20Engineering.png)

### 3. Streaming Chat
![Streaming Chat](screenshots/Streaming%20Chat.png)

### 4. Token Usage Report
![Token Usage Report](screenshots/Token%20Usage%20Report.png)
