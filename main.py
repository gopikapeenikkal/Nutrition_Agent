import os
from fastapi import FastAPI, File, UploadFile 
from nutrition_guide import nutrition_agent
from dotenv import load_dotenv


load_dotenv() 

app = FastAPI()

#api to post the image to generate the nutrional data return the data 
@app.post("/captured_image")
async def image_analysis(image:str):
    try:
        print(image)
        data = nutrition_agent(image)
        
        return {"message": data} 
    except Exception as e:
        print (f'Error: {e}')

