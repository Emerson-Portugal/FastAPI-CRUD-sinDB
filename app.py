from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime

app = FastAPI()


DB = []

## Al no tener una DB, creamos una estructura 

class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now
    published_at: Optional[datetime]
    published: bool = False




@app.get('/')
def read_root():
    return {"welcome": "Hola Mundo Emer"}

@app.get('/database')
def get_posts():
    return DB


@app.post('/datapost')
def save_post(post: Post):
    print(post)
    return "received"
