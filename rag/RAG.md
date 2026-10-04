# Deep Dive: Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation (RAG) is an open-book technique that lets an AI model search your private data and use it to answer questions accurately.

---

## 💡 What is RAG?
Instead of relying solely on an LLM's pre-trained data or spending massive resources on fine-tuning, RAG connects a language model to an external knowledge source. 

* **Search first, answer second:** The system finds the exact file or text segment that matches a user question.
* **No hallucination:** The AI relies on the retrieved text to write an accurate, source-backed answer.

---

## 🔄 The RAG Pipeline
A standard RAG workflow includes five main phases:

* **Load:** Read raw files like Markdown (`.md`) notes or PDFs.
* **Chunk:** Split long text into smaller, manageable pieces to fit into the LLM's context window.
* **Embed:** Turn text chunks into numeric vectors (lists of numbers) that represent meaning.
* **Store:** Save these vectors in a specialized vector database like Chroma or FAISS for quick similarity searches.
* **Retrieve & Generate:** Find the closest chunks to a user query, pass them to the LLM as context, and let the model generate a tailored answer.

---

## 🐍 Python Code Implementation with LangChain

Below is a complete script using **LangChain** and **Chroma** to load local Markdown (`.md`) files, chunk them, embed them, and query them.

```python
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Load Markdown documents from a local folder
loader = DirectoryLoader(
    "./my_notes", glob="**/*.md", loader_cls=TextLoader, loader_kwargs={"encoding": "utf-8"}
)
docs = loader.load()

# 2. Chunk the documents into smaller pieces
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(docs)

# 3. Create vector embeddings and store them in Chroma
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vector_store = Chroma.from_documents(chunks, embeddings, persist_directory="./chroma_db")

# 4. Create a retriever from the vector database
retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)  # Get top 3 matching chunks

# 5. Define the LLM and prompt template
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the provided context below:
{context}

Question: {question}
""")


# Format retrieved documents into a single string
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# 6. Build the RAG chain
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
)

# 7. Ask a question based on your .md files
response = rag_chain.invoke("What are my key project goals outlined in the notes?")
print(response.content)
```

## ***Summary***:

### **RAG (Retrieval Augmented Generation)**
#### **Why third?**

***This is the most practical real-world AI skill right now Learn***
- Embeddings
- Vector databases
- Chunking data
- Retrieval + generation flow

**Tools**
- FAISS / Chroma
- LangChain or LlamaIndex

**Build**
- Chatbot with your own data (PDF, notes, etc.)

***👉 Goal: Make AI use your data***