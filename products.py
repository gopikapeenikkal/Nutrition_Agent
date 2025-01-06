import json
import requests

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



    
    

    