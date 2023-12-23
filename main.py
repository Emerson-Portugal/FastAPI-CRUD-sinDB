from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime
from uuid import uuid4 as uuid
import uvicorn

app = FastAPI()

DB = []

# Post model
class Post(BaseModel):
    name: str
    content: Text

# Clase extendida para incluir un campo "id"
class ItemWithID(Post):
    id: str


@app.get('/')
def read_root():
    return {"welcome": "Welcome to my API"}

@app.get('/posts')
def get_posts():
    return DB

@app.post('/posts')
def save_post(post: Post):
    item_id = str(uuid())
    item_with_id = ItemWithID(id=item_id, **post.dict())
    DB.append(item_with_id)
    return DB[-1]

@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in DB:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Item not found")

