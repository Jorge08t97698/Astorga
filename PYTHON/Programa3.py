#!/usr/bin/env python
# coding: utf-8

# In[44]:


receta ={

       "Receta":"Tarta de Queso",
        "Mantequilla":{"valor1":100,"units1":"gramos"},
        "Azucar":{"valor1":100,"units1":"gramos"},
        "Galletas":{"valor1":400,"units1":"gramos","valor2":2,"units":"paquetes"},        
        "Queso de untar":{"valor1":400,"units1":"gramos"},
        "Cuajada":{"valor1":24,"units1":"gramos","valor2":2,"units":"sobres"}, 
        "Nata Liquida":{"valor1":400,"units1":"gramos"} }            
print(receta["Mantequilla"]["units1"])


# In[22]:


d = {'uno': 1, 'dos': 2, 'tres': 3}
d['dos']


# In[26]:


d = {'uno': 1, 'dos': 2, 'tres': 3}
for e in d:
   print(e)


# In[ ]:




