#!/usr/bin/env python
# coding: utf-8

# In[ ]:


[
   {
       "Receta":"Tarta de Queso",
    "Ingredientes":{
        "Mantequilla":{
            "valor":100,
            "units":"gramos"
        },
            "Azucar":{
            "valor":100,
            "units":"gramos"                
        },
            "Galletas":{
            "valor":2,
            "units":"paquetes"
            "valor":400
            "units":"gramos"               
        },
            "Queso de untar":{
            "valor":400,
            "units":"gramos"               
        },
            "Cuajada":{
            "valor":24,
            "units":"gramos"
            "valor":2
            "units":"sobres"        
        },
            
            "Nata Liquida":{
            "valor":400,
            "units":"gramos"         
        },  
    
 }      
   } 
      
        
]   


# In[3]:


import json
with open("C:/Users/jorge/OneDrive/Escritorio/Curso preuniversitario/receta.json") as f:
#     contents = f.read()
#     print(contents)
    y = json.load(f)
print (y)
 


# In[ ]:




