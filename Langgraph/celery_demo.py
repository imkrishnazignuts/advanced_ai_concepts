from fastapi import FastAPI
app = FastAPI()
from celery import Celery
import time

celery = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery.task
def write_into_log(email:str,message:str):
    time.sleep(30)
    with open("logs.txt","a") as file:
        file.write(f'{message} is sended the sender is {email} \n')

@app.post('/')
def send_mail(email:str,message:str):
    write_into_log.delay(email,message)
    return {"email sended successfully"}

