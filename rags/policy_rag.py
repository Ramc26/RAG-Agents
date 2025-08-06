from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader("./data/policy.pdf")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
chunks = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

def query_policy_rag(query):
    docs = vectorstore.similarity_search(query)
    context = "\n\n".join([doc.page_content for doc in docs])
    prompt_template = "Context: {context}\n\nQuestion: {question}\n\nAnswer:"
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    llm = OpenAI(temperature=0.7)
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(context=context, question=query)
    return response

# while True:
#     query = input("Enter your query: ")
#     if query.lower() == "exit":
#         break
#     response = get_response(query)
#     print(response)