from langchain.agents import  create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

@tool
def send_email(content:str):
    """use this tool when user need to send mail"""
    return "mail sended successfully "


@tool
def delete_email(content:str):
    """use this tool when user want to delete email"""
    return "mail sended successfully "

@tool
def update_email(content:str):
    """use this tool when user want to update email"""
    return "mail sended successfully "

agent = create_agent(
    model=llm,
    tools=[send_email,delete_email,update_email],
    middleware=[HumanInTheLoopMiddleware(
        interrupt_on={
            "send_email":True,
            "delete_email":True,
            "update_email":True,
        }
    )]
)

response = agent.invoke({
    "messages":[
        {
            "type":"user",
            "content":"send mail to sir "
        }
    ]
})

print(response["messages"][-1].content)