from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text
from datetime import datetime
from uuid import uuid4 as uuid
import uvicorn

app = FastAPI()

posts = []

# Post model
class Post(BaseModel):
    id: str = str(uuid())
    title: str
    author: str
    content: Text
    created_at: datetime =  datetime.now()
    published_at: datetime
    published: bool = False

@app.get('/')
def read_root():
    return {"welcome": "Welcome to my API"}

# Mostramos toda la Data
@app.get('/posts')
def get_posts():
    return posts


# Guardamos la Data
@app.post('/posts')
def save_post(post: Post):
    posts.append(post.dict())
    return posts[-1]
