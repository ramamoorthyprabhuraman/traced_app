from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompts = [
    "What is Generative AI?",
    "Explain Langchain in 5 bullet points.",
    "Write a detailed explanation of Retrieval-Augmented Generation (RAG) and its applications.",
]

for i, prompt in enumerate(prompts, start=1):
    print(f"\n----- Prompt {i}: ------")
    print("Question:", prompt)
    response = llm.invoke(prompt)
    print("\nAnswer:")
    print(response.content)