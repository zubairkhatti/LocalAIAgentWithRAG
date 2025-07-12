from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template="""
You are an expert in answering questions about a pizza restaurant

Here are some relevent reviews: {reviews}

Here is question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n---------------------------------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n")
    if question == "q":
        break

    review = retriever.invoke(question)
    result = chain.invoke({"reviews": review, "question": question})
    print(result)