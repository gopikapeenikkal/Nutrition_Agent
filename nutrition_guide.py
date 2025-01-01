from phi.agent import Agent, RunResponse
from rich.pretty import pprint
from pydantic import BaseModel, Field
from phi.model.google import Gemini
from phi.tools.tavily import TavilyTools 
import os
from dotenv import load_dotenv
from training import SYSTEM_PROMPT,INSTRUCTIONS
from typing import Iterator 
import json

load_dotenv()

#image analysing google model
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
#image data seach tool
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY') 

#function to analyze the image and give the nutrional guidence 
async def nutrition_agent(image: str):
    try:
        agent = Agent(
            model=Gemini(id="gemini-2.0-flash-exp"),
            tool=[TavilyTools()],
            markdown=True,
            system_prompt=SYSTEM_PROMPT,
            instruction=INSTRUCTIONS,
            structured_outputs=True,
        )

        # Get streaming response
        stream = agent.run(
            "analyse the product image",
            images=[image],
            stream=True
        )

        for chunk in stream:
            if isinstance(chunk, (str, dict, RunResponse)):
                content = (
                    chunk.content if hasattr(chunk, 'content')
                    else chunk.get('content', '') if isinstance(chunk, dict)
                    else str(chunk)
                )
                yield content

    except Exception as e:
        yield f"Error: {str(e)}"




