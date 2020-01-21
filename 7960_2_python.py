#Bonus Q1
#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np


# In[82]:


df = pd.read_csv('imdb.csv',escapechar='\\')


# In[83]:


col = list(df)
l=(len(col))
li=[]
o=[]
k=0
for i in df.itertuples():
    for j in range (16,l):
        if i[j+1] == 1:
            o.append(col[j])
            
    li.append(o)
    o=[]


# In[84]:


df['GenreCombo']=li


# In[85]:


nl=[]
combo=df.groupby(['year','type'])['GenreCombo'].apply(pd.Series.tolist).tolist()


# In[86]:


nl=[]
i=0
for a in combo:
    for b in a:
        if b not in nl:
            nl.append(b)
    combo[i]=nl
    i=i+1
    nl=[]
        


# In[87]:


combo1=[]
l2=[]
i=0
for a in combo:
    for b in a:
        if b != []:
             l2.append(b)
    combo1.append(l2)
    l2=[]
combo=combo1


# In[88]:


min=df.groupby(['year','type'])['imdbRating'].min().reset_index()
avg=df.groupby(['year','type'])['imdbRating'].mean().reset_index()
max=df.groupby(['year','type'])['imdbRating'].max().reset_index()
sum=df.groupby(['year','type'])['duration'].sum().reset_index()


# In[89]:


newdf=pd.DataFrame()
newdf['Year']=min['year']
newdf['Type']=min['type']
newdf['Genre_Combo']=combo
newdf['Avg_Rating']=avg['imdbRating']
newdf['Min_Rating']=min['imdbRating']
newdf['Max_Rating']=max['imdbRating']
newdf['Total_Time']=sum['duration']
newdf






#Bonus Q2
#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


df = pd.read_csv('imdb.csv',escapechar='\\')


# In[4]:


l=[]
for i in df.itertuples():
    l.append(len(i[3])-7)
df['TitleLength']=l   


# In[5]:


quan= df['TitleLength'].quantile([.25, .5, .75, 1])


# In[6]:


df25=df[df['TitleLength']<quan[.25]]['year'].reset_index()
df25['25Percentile']=1
df25=df25.groupby('year')['25Percentile'].sum().reset_index()


# In[7]:


df50=df[df['TitleLength']<quan[.50]]['year'].reset_index()
df50['50Percentile']=1
df50=df50.groupby('year')['50Percentile'].sum().reset_index()


# In[8]:


df75=df[df['TitleLength']<quan[.75]]['year'].reset_index()
df75['75Percentile']=1
df75=df75.groupby('year')['75Percentile'].sum().reset_index()


# In[9]:


df100=df[df['TitleLength']<quan[1.00]]['year'].reset_index()
df100['100Percentile']=1
df100=df100.groupby('year')['100Percentile'].sum().reset_index()


# In[10]:


min=df.groupby('year')['TitleLength'].min().reset_index()
max=df.groupby('year')['TitleLength'].max().reset_index()


# In[71]:


quandf=pd.DataFrame()
quandf['year']=df['year'].unique()
quandf=quandf.sort_values(by ='year' )
quandf['Min_Length']=min['TitleLength']
quandf['Max_Length']=max['TitleLength']
quandf=pd.merge(quandf,df25,how='outer',on='year')
quandf=pd.merge(quandf,df50,how='outer',on='year')
quandf=pd.merge(quandf,df75,how='outer',on='year')
quandf=pd.merge(quandf,df100,how='outer',on='year')
quandf






#BonusQ3
#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


df=pd.read_csv('diamonds.csv')


# In[4]:


df['z']=pd.to_numeric(df['z'],errors='coerce')
vol=[]
for i in df.itertuples():
    if i[5]>60:
        vol.append(i[8]*i[9]*i[10])
    else:
        vol.append(8)
df['Volume']=vol  


# In[5]:


df['Bins']=pd.qcut(df['Volume'],q=10)


# In[8]:


newdf=pd.crosstab(df['Bins'],df['cut']).apply(lambda x:x/x.sum(),axis=1)


# In[9]:


s=df['Bins'].value_counts().sum()
newdf['PercentageTotal']=df['Bins'].value_counts().apply(lambda x: (100 * x) / s )
newdf


# In[ ]:





# In[ ]:



#BonusQ5
#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[4]:


df = pd.read_csv('imdb.csv',escapechar='\\')


# In[5]:


df['Decile'] = pd.qcut(df['duration'], 10, labels=False)


# In[6]:


gn=df.groupby('Decile').sum().reset_index()
gn.to_csv('decile.csv')


# In[7]:


col = list(gn)
l=(len(col))
gl=[]
for i in gn.itertuples():
    li=[]
    o=[]
    r=np.arange(11,l)
    for j in range (11,l):
        o.append(i[j+1])
    a=np.argsort(o)
    li.append(col[a[l-11-1]+11])
    li.append(col[a[l-2-11]+11])
    li.append(col[a[l-3-11]+11])
    gl.append(li)


# In[8]:


win=df.groupby('Decile')['nrOfWins'].sum().reset_index()
nom=df.groupby('Decile')['nrOfNominations'].sum().reset_index()


# In[9]:


df['Flag']=1
cou=df.groupby('Decile')['Flag'].sum().reset_index()


# In[10]:


newdf=pd.DataFrame()
newdf['Decile']=nom['Decile']
newdf['Nominations']=nom['nrOfNominations']
newdf['Wins']=win['nrOfWins']
newdf['Count']=cou['Flag']
newdf['Top3_Genres']=gl
newdf


# In[ ]:




