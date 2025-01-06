import os
from phi.agent import Agent
from phi.knowledge.text import TextKnowledgeBase
from phi.vectordb.pgvector import PgVector
from phi.model.google import Gemini
from dotenv import load_dotenv 

load_dotenv 

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

knowledge = TextKnowledgeBase (
    path = "https://uat.freshivores.com/v1/products",
    vector_db = PgVector(
        table_name = 'text_file',
        db_url = 'postgresql+psycopg2://ai:freshi_ai@localhost:5532/freshi'   
    ),  
)
web_Agent = Agent(
    knowledge_base = knowledge,
    model = Gemini(id="gemini-1.5-flash"),
    search_knowledge = True,
    system_prompt = SYSTEM_PROMPT,
    instruction = INSTRUCTIONS,
    structured_outputs=True,
) 
web_Agent.print_response(
    "get the ingredients for making biriyani from the provided text",
    stream = True
)

# db_url = 'postgresql+psycopg://ai:freshi_ai@localhost:5532/freshi'



## product page --> 
## take the product title --> 
## collect the product details from the api --> 
# pass that to LLM --> 
# Instruction to take the text and modify it with *a comparision to the other packled products commomly avilable *highlight nutrition benefit of this product in short --> 
# structured response 
