from phi.agent import Agent, RunResponse
from rich.pretty import pprint
from pydantic import BaseModel, Field
from phi.model.google import Gemini
from phi.tools.tavily import TavilyTools 
import os
from dotenv import load_dotenv
from instructions import SYSTEM_PROMPT,INSTRUCTIONS
from typing import Iterator 
import json

load_dotenv()

#image analysing google model
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
#image data seach tool
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY') 

#function to analyze the image and give the nutrional guidence 
def nutrition_agent(image:str):
    try:
        agent = Agent(
        model = Gemini(id="gemini-2.0-flash-exp"),
        tool = [TavilyTools()],
        markdown = True,
        system_prompt = SYSTEM_PROMPT,
        instruction = INSTRUCTIONS,
        structured_outputs=True,
        )

       # Initialize response accumulator
        full_response = ""
        
        # Get streaming response
        stream = agent.run(
            "analyse the product image",
            images=[image],
            stream=True
        )

        # Process the stream
        for chunk in stream:
            if isinstance(chunk, RunResponse):
                # Extract content from RunResponse object
                if hasattr(chunk, 'content'):
                    full_response += chunk.content
                elif hasattr(chunk, 'message') and isinstance(chunk.message, dict):
                    full_response += chunk.message.get('content', '')
            elif isinstance(chunk, str):
                full_response += chunk
            elif isinstance(chunk, dict):
                full_response += chunk.get('content', '')

        if not full_response:
            return {"status": "error", "message": "No response generated"}

        # Clean up the response and format it properly
        cleaned_response = {
            "status": "success",
            "analysis": {
                "content": full_response.strip(),
                "format": "markdown"
            }
        }

        return cleaned_response
     
    except Exception as e:
        # Handle any errors and log them
        print(f"An error occurred: {e}")
        return {"error": str(e)}




