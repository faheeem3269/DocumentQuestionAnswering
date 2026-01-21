from xml.dom.minidom import Document
from fastapi import UploadFile
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
from sqlalchemy import null
load_dotenv()

os.environ["HF_TOKEN"]=os.getenv("HF_TOKEN")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")



# Declare global variable
vectorstore = None

Direcory="data/documents/"

def read_file_content(name:str) -> str:
    """Read the name of an uploaded file and return it as a string."""
    print(name)
    filepath = Direcory + name
    print(filepath)
    with open(filepath, 'r', encoding='utf-8') as file:
        if file:
            content = PyPDFLoader(filepath).load()
        else:
            content = "File is empty"
            print("File is empty")
    return content

def startEmbedding(contect:list[Document]):
    """Start embedding the content using Langchain embeddings."""
    #global vectorstore  # Use the global variable

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    final_doc = text_splitter.split_documents(contect)
    
    vectorstore=FAISS.from_documents(final_doc,embedding) # assign to global
    vectorstore.save_local("data/faiss_index")
    print("Embedding is created")

def StartQA(question: str):
    """Start the Question Answering process."""
    try:
       # global vectorstore  # Use the global variable

        # Load FAISS index only if vectorstore is not initialized
        #if vectorstore is None:
        embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectorstore = FAISS.load_local("data/faiss_index", embeddings=embedding,allow_dangerous_deserialization=True)

        #print("Step1")
        # Create ChatGroq LLM
       
       
        # Retrieve top-k relevant document chunks
        docs = vectorstore.similarity_search(question,k=2)
        #print("Step3")
        # Combine content into a single prompt
        context = "\n\n".join([doc.page_content for doc in docs]) 
        llm = ChatGroq(model_name="openai/gpt-oss-120b", api_key="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")
        prompt=ChatPromptTemplate.from_template(
        """
        Answer the questions based on the provided context only.
        Please provide the most accurate respone based on the question
        - Headings in bold
        - Paragraph breaks for explanations
        - Avoid Markdown tables
        - If the answer is not contained within the context, respond with "I don't know."
        - Do not fabricate answers.
        -if answer in bullet points, remove '*' and '-' for each point.
        <context>
        {context}
        <context>
        Question:{question}

        """

        )
        chain=prompt | llm
        # Send prompt to LLM
        response = chain.invoke({
        "context":context,
        "question":question

        })
        
        
        return response.content
    except Exception as e:
        return e

    
