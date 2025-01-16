import os
import json
import requests
import re
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
# from app.services.product import create_index, get_product_data
from dotenv import load_dotenv
from typing import List, TypedDict, Optional

#gets product title,short_descrption,additional_info using api
def get_product_detail(product_id:int):
    try:
        # load json module
        json_data_module = requests.get(f'https://uat.freshivores.com/v1/products/{product_id}') 

        # Ensure the request was successful
        # if response.status_code != 200:
        #     print(f"Failed to fetch data. Status code: {response.status_code}")
        #     return None
        
        # Extract data from the loaded file
        product = json_data_module.json() 
        
        #storing the product details in list 
        if product.get("id") == product_id: 
            title = product["title"] or '',
            short_description = product["short_description"] or '',
            additional_info = product["additional_info"] or '',
            #storing the details in product details for return
            


            product_details={
                "title":title,
                "short_description":short_description,
                "additional_info":additional_info
                }
            print(product_details)
            return(product_details) 
        else:
            print("product not found")
            return None  
             
    except Exception as e:
        print(f"Exception error in --> get_product_detail{e}") 

# get_product_detail()

#to get all product data


def all_products():
    #loads json
    products_json = requests.get ("https://uat.freshivores.com/v1/products")
    
    #extract json data
    products = products_json.json()
    for product in products:
        title = product['title'] or '',
        short_description = product['short_description'] or '',
        description = product['description'] or '',
        additional_info = product['additional_info'] or ''
        product_data = {"Title":title,
                        "Short_description":short_description,
                        "Description":description,
                        "Additional_info":additional_info
        }
        print(product_data)
        return product_data 
# all_products() 


#spliting the inputs for the nutrition diet 
# a,b,c,d = input("Enter the following details Age,Gender,Height,Weight:").split() 
# A = "Age:",a
# B = "Gender:",b
# C = "Height:",c
# D = "Weight:",d
# print(A)
# print(B)
# print(C)
# print(D)
# print()

#storing product data as csv file 

load_dotenv()

  
    
    
class Media2(TypedDict):
    file_path: str
    thumb_file_path: str

class Category(TypedDict):
    title: str
    slug: str
    priority: int
    menu_priority: int
    media2: Media2

class Media(TypedDict):
    file_path: str

class Product(TypedDict):
    id: int
    slug: str
    title: str
    show_in_website: bool
    short_description: str
    media: Media

class ProductResponse(TypedDict):
    items: List[Product]
    total: int
    page: int
    size: int
    pages: int

class MillingVariant(TypedDict):
    id: int
    name: str
    description: str
    sku_code: str

class ItemMilling(TypedDict):
    is_default: bool
    milling_variants: MillingVariant

class ItemVariants(TypedDict):
    name: str
    item_millings: List[ItemMilling]

class UnitType(TypedDict):
    name: str
    short_name: str

class PurchaseType(TypedDict):
    name: str

class ProductPurchasable(TypedDict):
    purchase_type: PurchaseType
    is_possible: bool
    reason: str

class ProductVariant(TypedDict):
    id: int
    sku_code: str
    primary_variant_id: int
    mrp: float
    sale_price: float
    is_default: bool
    show_in_website: bool
    status: bool
    quantity: int
    is_primary_product: bool
    item_variants: ItemVariants
    unit_types_prod: UnitType
    product_purchasable: List[ProductPurchasable]

class ProductMedia(TypedDict):
    medias: Media

class ProductDetail(TypedDict):
    title: str
    short_description: str
    description: str
    additional_info: str
    id: int
    is_featured: bool
    is_new: bool
    browser_title: str
    og_title: str
    meta_description: str
    bottom_description: str
    og_description: str
    meta_keywords: str
    product_type: str
    is_loose_packing: bool
    is_millable: bool
    product_variants: List[ProductVariant]
    media: Media
    search_keyword: str
    product_media: List[ProductMedia]

CSV_OUTPUT_DIR = "output_reports"

# Helper function to ensure output directory exists
def ensure_output_directory():
    """Create output directory if it doesn't exist"""
    if not os.path.exists(CSV_OUTPUT_DIR):
        os.makedirs(CSV_OUTPUT_DIR)
   

def get_products() -> JSONResponse: 
    try:  
    
         # Ensure output directory exists
        ensure_output_directory()
        
        # Update file paths to use output directory
        pdt_data_file = os.path.join(CSV_OUTPUT_DIR, f"product list.csv")
        
        # Create CSV files with headers
        with open(pdt_data_file, 'a') as f:
            f.write("title") 
    
        #loads json
        products_json = requests.get ("https://uat.freshivores.com/v1/products") 
        
        #extract json data
        products = products_json.json() 
        
        #html tag cleaner
        CLEANR = re.compile('<.*?>') 
        # Initialize the counter for id
        # add_id = 1
        
        #taking each product data
        for product in products:
            #getting the data form the json
            title = product.get('title')or ''
            short_description = product.get('short_description') or ''
            description = product.get('description') or ''
            additional_info = product.get('additional_info') or ''
            
            
            #removing the HTML tags from the data
            c_title = re.sub(CLEANR,'',title)
            c_short_description = re.sub(CLEANR,'',short_description)
            c_description = re.sub(CLEANR,'',description) 
            c_additional_info = re.sub(CLEANR,'',additional_info) 
            
            # Increment the id counter for the next entry
            # add_id += 1
            
            #storing the HTML tag removed data into csv file 
            with open(pdt_data_file, 'a') as f:
                f.write(f'{c_title}\n')
                # f.write(f'{c_title},{c_short_description},"{c_description}","{c_additional_info}"\n') 
    except Exception as e:
        print (f'Error in function get_product--> {e}')
      
get_products() 

    

    
