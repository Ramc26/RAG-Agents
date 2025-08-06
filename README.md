# RAG-Agents

A Retrieval-Augmented Generation (RAG) project for answering questions about your organization's documents (MCP and Policy) using LLMs and CrewAI agents.

---

## 🚀 Setup

### 1. **Clone the Repository**
```sh
git clone https://github.com/Ramc26/RAG-Agents.git
cd RAG-Agents
```

### 2. **Install [uv](https://github.com/astral-sh/uv) (if not already installed)**
```sh
pip install uv
```

### 3. **Initialize the Project Environment**
```sh
uv venv
uv pip install -r pyproject.toml
```
Or, if you want to use `uv` directly with the `pyproject.toml`:
```sh
uv pip install -r pyproject.toml
```

### 4. **Set Up Environment Variables**
Create a `.env` file in the project root with your OpenAI API key:
```
OPENAI_API_KEY=sk-...
```
**Important:** Never commit your `.env` file to git.

### 5. **Add Your Documents**
Place your PDF files in the `data/` directory:
- `data/mcp.pdf`
- `data/policy.pdf`

---

## 🧑‍💻 Running the RAG Scripts Directly

You can run the RAG scripts for each document separately:

### **Policy RAG**
```sh
uv run rags/policy_rag.py
```
This will load `data/policy.pdf` and allow you to query it via the `query_policy_rag` function.

### **MCP RAG**
```sh
uv run rags/mcp_rag.py
```
This will load `data/mcp.pdf` and allow you to query it via the `query_mcp_rag` function.

---

## 🕹️ Using the Agent UI (`main.py`)

The main entry point is a Streamlit app that uses CrewAI agents to answer questions about both documents.

### **Run the Streamlit App**
```sh
uv run main.py
```
or
```sh
streamlit run main.py
```

- Enter your question in the UI.
- The agent will select the appropriate RAG tool (MCP or Policy) and return an answer.

---

## 🧩 Code Structure & Explanation

### **main.py**
- **Streamlit UI**: Provides a web interface for user queries.
- **Tools**: `MCPTool` and `PolicyTool` wrap the RAG functions for each document.
- **Agent**: A CrewAI `Agent` is created with both tools and a goal to answer questions using the most relevant document.
- **Task**: A `Task` is defined for the agent to answer the user's question.
- **Crew**: A `Crew` is created with the agent and task, orchestrating the workflow.
- **Execution**: When the user submits a query, the crew is kicked off, and the answer is displayed.

### **CrewAI Concepts**
- **Agent**: An autonomous entity with a role, goal, and access to tools. Here, the agent decides which document/tool to use.
- **Task**: A unit of work assigned to an agent. In this project, the task is to answer the user's question.
- **Crew**: A group of agents and tasks, managing the workflow and execution.

### **RAG Scripts (`rags/policy_rag.py`, `rags/mcp_rag.py`)**
- **PDF Loading**: Uses `PyPDFLoader` to load the document.
- **Text Splitting**: Splits the document into chunks for retrieval.
- **Vector Store**: Embeds and stores chunks using FAISS and OpenAI embeddings.
- **Query Function**: Retrieves relevant chunks and generates an answer using an LLM chain.

---

## 📝 Example Usage

**Ask a question about the MCP or Policy document:**
- "What is the company’s leave policy?"
- "How does the MCP handle data privacy?"

The agent will select the right tool and provide an answer based on the relevant document.

---

## ⚠️ Security Note

- **Never commit your `.env` file or API keys to git.**
- If you accidentally commit a secret, remove it from your history and generate a new key.

---

Let me know if you want this README saved to your project, or if you want to customize any section!