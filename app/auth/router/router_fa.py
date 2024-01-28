from fastapi import Depends, UploadFile,status
from . import router

@router.get("/get")
def get_answer(

):
    return {"msg":"right"}