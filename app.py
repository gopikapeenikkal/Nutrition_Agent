import os
from phi.agent import Agent, RunResponse
from phi.knowledge.csv import CSVKnowledgeBase
from phi.vectordb.pgvector import PgVector, SearchType
from phi.model.google import Gemini
from phi.embedder.google import GeminiEmbedder
from dotenv import load_dotenv
from train import SYSTEM_PROMPT,INSTRUCTIONS
from phi.utils.pprint import pprint_run_response

# Load the environment variables
load_dotenv()

# Get the Google API key from the environment variables
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY') 

# Creating the agent           
def dietplan_agent(): 
    try:
        # Create a knowledge base with the CSV file
        knowledge_base = CSVKnowledgeBase(
            path = ("output_reports/product list.csv"),
            vector_db = PgVector (
                table_name = 'productlist',
                db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai",
                embedder = GeminiEmbedder(
                        dimensions=768,
                    )),)
        
        return Agent(
            model = Gemini(id = "gemini-2.0-flash-exp"),
            knowledge = knowledge_base,
            search_knowledge = True,
            add_context = True,
            markdown = True,
            description = SYSTEM_PROMPT,
            instruction = INSTRUCTIONS,
            debug_mode = True,   
        )
    except Exception as e:
        print(f'exception in dietplan_agent -->{e}')       


def get_details():
    try:
        #user input
        user_data = {} 
            
        #details to be collected form the user    
        questions = ["Gender(M,F,O)","Age","Wight(gain/loss/same)","Current weight","Veg/non-veg/vegan","Activity level(very active, moderatly_active, not_active)","Health conditions if any","Preferred meal type(South_Indian, North_Indian, Western)"] 
        for quest in questions: 
            response = input(quest + ": ") 
            #stores question as key and reponse as value
            user_data[quest] = response 
                 
            return user_data   
    except Exception as e:
        print(f'Exception in get_details --> {e}')  
                

def instructions(): 
    try: 
        # getting the user details 
        details = get_details() 
        
        # getting the user responses in variable
        gender = details['Gender(M,F,O)']
        age = details['Age']
        weight_goal = details['Wight(gain/loss/same)']
        weight = details["Current weight"]
        category = details['Veg/non-veg/vegan']
        activity_level = details['Activity level(very active, moderatly_active, not_active)']
        health_condition = details['Health conditions if any']
        meal_type = details['Preferred meal type(South_Indian, North_Indian, Western)'] 


        # generating the input for the agent with the user inputs
        prompt = f"""
                Based on the following user information, create a personalized diet plan using products list:
                Gender: {gender}
                Age: {age}
                Weight gaining/loss/same: {weight_goal}
                Weight : {weight}
                Veg/non-veg/vegan: {category}
                Activity level(very active, moderatly active, not active): {activity_level}
                Health conditions: {health_condition}
                Preferred meal type: {meal_type}  
                
                
                
               Create a detailed diet plan considering the following points:
               - Daily Caloric Requirements: Calculate based on the individual's activity level, weight, and health condition and show the requied calory requirement.
               - Meal Plan: Design a meal plan that incorporates products from knowledge.
               - Meal Structure & Variety:
                  * Divide the meals in a day to 4 breakfast, lunch, mid day snak and dinner.
                  * mention the calory of each meal.
                  * Provide six different meal options to offer variety.
               - Ingredient List: At the end of the diet plan, list all product list given in knowledge base used as ingredients in making the diet dishes.
               - User Feedback: Conclude by asking the user if they are satisfied with the plan or if they would like any modifications.
               - Ensure the plan is nutritionally balanced and practical.
                
                Format the response in a clear, structured way using markdown.
                """
        # Call the dietplan_agent       
        diet_agent = dietplan_agent()
        
        # Create a run with input
        diet_agent.print_response(prompt, stream = True) 
        
    except Exception as e:
        print(f'Exception in function instruction --> {e}') 

instructions()