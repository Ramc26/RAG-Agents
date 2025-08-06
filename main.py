import streamlit as st
from crewai import Agent, Task, Crew
from crewai.tools import BaseTool
from rags.mcp_rag import query_mcp_rag
from rags.policy_rag import query_policy_rag
from dotenv import load_dotenv

load_dotenv()

class MCPTool(BaseTool):
    name: str = "MCP Tool"
    description: str = "This tool answers questions about the MCP document. Use it for any query related to MCP."
    def _run(self, query: str) -> str:
        return query_mcp_rag(query)

class PolicyTool(BaseTool):
    name: str = "Policy Tool"
    description: str = "This tool answers questions about the company policy document. Use it for queries about policies, rules, or guidelines."
    def _run(self, query: str) -> str:
        return query_policy_rag(query)

mcp_tool = MCPTool()
policy_tool = PolicyTool()

agent = Agent(
    role="Document Researcher",
    goal="Answer user questions by using the most relevant RAG tool.",
    backstory="You are an expert at selecting the correct document to answer a question. You have access to a tool for MCP and a tool for the company policy.",
    tools=[mcp_tool, policy_tool],
    verbose=True,
    allow_delegation=False
)

task = Task(
    description="Answer the user's question: {query}",
    expected_output="A clear and accurate answer based on the relevant document.",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True
)

st.title("Document-Based AI Assistant")
st.write("Ask a question about the MCP or Policy documents.")

user_query = st.text_input("Enter your query here:")

if st.button("Get Answer"):
    if user_query:
        with st.spinner("Thinking..."):
            result = crew.kickoff(inputs={"query": user_query})
            st.write("---")
            st.subheader("Answer:")
            st.write(result.tasks_output[0].raw)
            with st.expander("Show full output"):
                st.write(result)
    else:
        st.warning("Please enter a query.")