#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from fastapi import FastAPI, HTTPException, Body
import uvicorn

# Директория, которую мы синхронизируем
if len(sys.argv) < 2:
    print("Usage: library.py <source_directory>")
    sys.exit(1)
SRC_DIR = os.path.abspath(sys.argv[1])

app = FastAPI()


@app.get("/library")
def list_files():
    files = sorted(
        f for f in os.listdir(SRC_DIR)
        if os.path.isfile(os.path.join(SRC_DIR, f))
    )
    return {"papka": files}


@app.get("/library/{fname}")
def read_file(fname: str):
    path = os.path.join(SRC_DIR, fname)
    if not os.path.isfile(path):
        raise HTTPException(status_code=404, detail="File not found - ${path}")
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except OSError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"file_stih": content}

'''
@app.post("/library/{fname}")
def create_or_overwrite_file(fname: str, data: bytes = Body(b"")):
    path = os.path.join(SRC_DIR, fname)
    try:
        with open(path, "wb") as f:
            if data:
                f.write(data)
    except OSError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"file_stih": data.decode("utf-8", "ignore")}
'''

@app.post("/library/{fname}")
def create_file(fname: str, data: bytes = Body(b"")):
    path = os.path.join(SRC_DIR, fname)
    if os.path.exists(path):
        raise HTTPException(
            status_code=409, 
            detail="File already exists"
            )
    
    try:
        with open(path, "wb") as f:
            f.write(data)
        return{
            "status": "created",
            "path": path,
            "size": len(data)
        }
    except OSError as e:
        raise HTTPException(status_code=500, detail="Creation failed " + str(e))
    #return {"file_stih": data.decode("utf-8", "ignore")}

@app.put("/library/{fname}")
def update_file(fname: str, data: bytes = Body(b"")):
    path = os.path.join(SRC_DIR, fname)
    if not os.path.exists(path):
        raise HTTPException(
            status_code=404, 
            detail="File not found - ${path}"
            )
    
    try:
        with open(path, "wb") as f:
            f.write(data)
        return{
            "status": "updated",
            "path": path,
            "size": len(data)
        }
    except OSError as e:
        raise HTTPException(status_code=500, detail="Update failed " + str(e))

@app.delete("/library/{fname}")
def delete_file(fname: str):
    path = os.path.join(SRC_DIR, fname)
    if not os.path.isfile(path):
        raise HTTPException(status_code=404, detail="File not found - ${path}")
    try:
        os.remove(path)
    except OSError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"deleted": fname}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)