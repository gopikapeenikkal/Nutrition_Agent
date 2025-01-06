import os
from phi.agent import Agent
from phi.knowledge.json import JSONKnowledgeBase
from phi.vectordb.pgvector import PgVector
from phi.model.google import Gemini
from dotenv import load_dotenv
# from products import all_products
# from train import SYSTEM_PROMPT,INSTRUCTIONS

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# knowledge = JSONKnowledgeBase (
#     path = "https://uat.freshivores.com/v1/products",
#     vector_db = PgVector(
#         table_name = 'freshi_json',
#         db_url = 'postgresql+psycopg2://ai:freshi_ai@localhost:5432/freshi'   
#     ),  
# )

# agent = Agent(
#     knowledge_base = knowledge,
#     model=Gemini(id="gemini-1.5-pro"),
#     markdown=True,
#     debug_mode=True,
#     # search_knowledge = True,
#     system_prompt="you are an agent who provides information about the products in the knowledge, if any other questions asked then say you do not have any information about it",
#     instruction="take the information of that product from knowledge_base these all are the products provided by the brand freshivores, and give a brif idea about the product",
#     structured_outputs=True,
# ) 
# agent.knowledge.load(recreate=False) 
# agent.print_response("jackfruit dried")
# web_Agent.print_response(
#     "jack fruit dried",
#     stream = True
# )

# db_url = 'postgresql+psycopg://ai:freshi_ai@localhost:5532/freshi'



## product page --> 
## take the product title --> 
## collect the product details from the api --> 
## pass that to LLM --> 
#taking input to amke the diet plan

# Instruction to take the text and modify it with *a comparision to the other packled products commomly avilable *highlight nutrition benefit of this product in short --> 
# structured response 

agent = Agent(
    model=Gemini(id="gemini-1.5-flash"),
    markdown=True,
)

agent.print_response("Share a 2 sentence horror story.")