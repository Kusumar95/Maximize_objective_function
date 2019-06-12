#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
from scipy.optimize import minimize, rosen, rosen_der
def cost_function(x):
    a1=100
    a2=150
    a3=300
    return -(a1*math.exp(-(x[0]/a1))*x[0]+a2*math.exp(-(x[1]/a2))*x[1]+a3*math.exp(-(x[2]/a3))*x[2])


# In[2]:


def constraint_function(x):
    a1=100
    a2=150
    a3=300
    return (a1*math.exp(-(x[0]/a1))+a2*math.exp(-(x[1]/a2))+a3*math.exp(-(x[2]/a3)))-150


# In[3]:


x=[3,3,3]
cons = ({'type': 'eq', 'fun':constraint_function})


# In[4]:


res = minimize(cost_function,x , method='SLSQP',constraints=cons)


# In[5]:


p1=res.x[0]
p2=res.x[1]
p3=res.x[2]


# In[6]:


print("The optimal prices are : p1="+str(res.x[0])+" p2= "+ str(res.x[1])+" p3= "+ str(res.x[2]))


# In[7]:


print("The number of person for price p1 = "+str(int((100*math.exp(-(p1/100))))))
print("The number of person for price p2 = "+str(int(150*math.exp(-(p2/150)))))
print("The number of person for price p3 = "+str(int((300*math.exp(-(p3/300))))))


# In[8]:


def constraint_function2(x):
    a1=100
    a2=150
    a3=300
    return (a1*math.exp(-(x[0]/a1))+a2*math.exp(-(x[1]/a2))+a3*math.exp(-(x[2]/a3)))-153


# In[9]:


x=[3,3,3]
cons2 = ({'type': 'eq', 'fun':constraint_function2})


# In[10]:


res2 = minimize(cost_function,x , method='SLSQP',constraints=cons2)


# In[11]:


print("Change in revenue:"+str(res2.fun-res.fun))


# In[12]:


print("Change in each price to increase")
print("P1:"+ str(res.x[0]-res2.x[0]))
print("P2:"+ str(res.x[1]-res2.x[1]))
print("P3:"+ str(res.x[2]-res2.x[2]))





