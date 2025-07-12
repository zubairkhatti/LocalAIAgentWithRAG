# Local AI Agent for Pizza Review RAG Bot

**Overview:**
This project is a RAG (Retrieval-Augmented Generation) system using Ollama (LLaMA3.2) and Chroma vector store. It answers user questions about a pizza restaurant based on customer reviews.

**Technologies Used:**
- LangChain (OllamaLLM, ChatPromptTemplate, Documents)
- Ollama for LLM and Embeddings (mxbai-embed-large)
- Chroma as vector store
- Pandas for CSV loading

**Flow:**
1. Reviews are read from a CSV file and converted into vector embeddings.
2. Vector data is stored in ChromaDB.
3. User asks a question via CLI.
4. System retrieves the top 5 most relevant reviews.
5. Reviews + question are sent to the LLaMA3.2 model.
6. Model generates a response based on the reviews.

**Purpose:**
To simulate a chatbot that uses real customer feedback to answer queries about a restaurant.
