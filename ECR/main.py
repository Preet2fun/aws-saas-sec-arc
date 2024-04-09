#!/usr/bin/env python3
'''simple API server that returns Hello World'''
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}