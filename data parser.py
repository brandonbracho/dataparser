#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pdfplumber


def parse_data(file):
    all_tables=[]
    with pdfplumber.open(file) as pdf:
        page=pdf.pages
        for page in pdf.pages:
            text=page.extract_text()
            all_tables.append(page.extract_tables())
    for table in all_tables:
        for t in table:
            for b in t:
                for c in b:
                    if c==None or c=="":
                        b.remove(c)
    machine_names=[]
    data=[]
    totals=[]
    for table in all_tables:
        for t in table:
            machine_names.append(t[0])
            data+=[l[0::3] for l in t[2:-1]]
            totals+=[t[-1][0::3]]
            
    return machine_names, data, totals 


        
parse_data('/Users/brandonbracho/Desktop/2014AnnualCasinoWin.pdf')


# In[4]:





# In[5]:



   


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




