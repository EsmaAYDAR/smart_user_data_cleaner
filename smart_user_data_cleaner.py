#!/usr/bin/env python
# coding: utf-8

# In[1]:


raw_data ="  AhMeT  yILMAZ ;  23 ;  1.78 ;  ahmetYILMAZ@GMAIL.Com   "

newData=raw_data.strip().split()


# In[24]:


##name
nameData=newData[:2]
firstName=nameData[0].lower().title()
lastName=nameData[1].lower().title()
fullName=firstName+" "+lastName
print("Kullanıcı Adı:"+fullName)


# In[23]:


##age
ageData=newData[3]
newAgeData=int(ageData)
futureAgeData=float(newAgeData)+10.0
print("10 yıl sonra yaş:",futureAgeData)


# In[28]:


##heigh
heighData=newData[5]
cmheihgData=float(heighData)*100
print("Boy cm cinsinden:",cmheihgData)


# In[39]:


##email
mailData=newData[7]
newMailData=mailData.lower().strip()
print("Mail Kodu:",newMailData[:3])


# In[ ]:




