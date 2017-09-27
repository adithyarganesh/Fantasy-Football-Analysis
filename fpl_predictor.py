
# coding: utf-8

# In[11]:

import pandas as pd
from pandas import Series,DataFrame

# numpy, matplotlib, seaborn
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
#get_ipython().magic('matplotlib inline')

# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB


# In[12]:

df = pd.read_csv("fpl_data.csv")

df.head()


# In[13]:

for col in df.columns:
    df.rename(columns={col : col[3:]}, inplace=True)


# In[14]:

df.info()


# In[15]:

df = df.drop(["Goalkeeping","Attack","Defence","Discipline","Team Play","Successful 0/0s","Successful /s","Successful 50/50s","Successful 5/5s"], axis = 1)


# In[16]:

df.info()


# In[17]:

df.to_csv('dead0.csv', index=False)


# In[18]:

df[''].dropna()
df.head()


# In[19]:

df["Names"]=df[""]


# In[20]:

df.info()


# In[21]:

df.drop(1, inplace=True)


# In[22]:

df.info()


# In[23]:

df = df[pd.notnull(df['Names'])]


# In[24]:

df.info()


# In[25]:

df[''].dropna()


# In[26]:

df.info()


# In[ ]:




# In[34]:

df.info()


# In[36]:

#df.drop([''], axis = 1, inplace = True)


# In[37]:

for col in df.columns:
    df[col] = df[col].fillna("0")


# In[38]:

df.head()


# In[48]:

df.drop(['Headed Clearance'], axis = 1, inplace = True)


# In[49]:

df.head()


# In[51]:

df.info()


# In[52]:

dummies  = pd.get_dummies(df['Position'])


# In[53]:

dummies.head()


# In[54]:

df = df.join(dummies)


# In[55]:

df.info()


# In[56]:

df.drop(['Position'], axis = 1, inplace = True)


# In[57]:

df.head()


# In[61]:

defender = df[df["Defender"] == 1]
goalkeeper = df[df["Goalkeeper"] == 1]
forward = df[df["Forward"] == 1]
midfielder = df[df["Midfielder"] == 1]


# In[65]:

defender = defender.drop(["Goalkeeper","Forward","Midfielder"], axis = 1)
defender.head()


# In[66]:

goalkeeper = goalkeeper.drop(["Defender","Forward","Midfielder"], axis = 1)
goalkeeper.head()


# In[67]:

forward = forward.drop(["Goalkeeper","Defender","Midfielder"], axis = 1)
forward.head()


# In[68]:

midfielder = midfielder.drop(["Goalkeeper","Forward","Defender"], axis = 1)
midfielder.head()


# In[78]:

forward.to_csv('forwards_data.csv')


# In[94]:

for col in forward.columns:
    if (forward[col] == '0').all() == True:
        forward = forward.drop([col],axis = 1)


# In[89]:

print (forward["Throw Outs"] is '0')


# In[95]:

cols = list(forward)
nunique = forward.apply(pd.Series.nunique)
cols_to_drop = nunique[nunique == 1].index
forward = forward.drop(cols_to_drop, axis=1)


# In[97]:

forward.to_csv('for_cons.csv')


# In[98]:

cols = list(midfielder)
nunique = midfielder.apply(pd.Series.nunique)
cols_to_drop = nunique[nunique == 1].index
midfielder = midfielder.drop(cols_to_drop, axis=1)

cols = list(defender)
nunique = defender.apply(pd.Series.nunique)
cols_to_drop = nunique[nunique == 1].index
defender = defender.drop(cols_to_drop, axis=1)

cols = list(goalkeeper)
nunique = goalkeeper.apply(pd.Series.nunique)
cols_to_drop = nunique[nunique == 1].index
goalkeeper = goalkeeper.drop(cols_to_drop, axis=1)


# In[103]:

midfielder.to_csv('midfielder_train.csv')
forward.to_csv('forward_train.csv')
goalkeeper.to_csv('goalkeeper_train.csv')
defender.to_csv('defender_train.csv')


# In[106]:

goalkeeper.info()


# In[107]:

gk_df = pd.read_csv('goalkeeper_train.csv')

