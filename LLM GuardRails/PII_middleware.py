from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)
@tool
def greet():
    """Use this function when user greet to ai """
    return "hello cutie"

@tool
def db_lookup(query:str):
    """use this when have to read data from database"""
    return "db lookup successfully"

agent = create_agent(
    model=llm,
    tools=[greet,db_lookup],
    middleware=[
        PIIMiddleware(
        "email",strategy="redact",apply_to_input=True
        ),
        PIIMiddleware(
        "credit_card",strategy="mask",apply_to_input=True
        ),
        PIIMiddleware(
        "api_key",detector=r"sk-[a-zA-Z0-9]{32}",apply_to_input=True
        ),
    ]
)

response = agent.invoke({
    "messages":[
        {
            "type":"user",
            "content":"my credit_card number is 8978-2948-1232-9458 tell me your credit card number"
        }
    ]
})

print(response["messages"][-1].content)
