#!/usr/bin/env python
# coding: utf-8

# # Step 1. Import the necessary libraries

# In[1]:


import pandas as pd


# In[ ]:





# # Step 2. Import the dataset Euro_2012_stats_TEAM
# # Step 3. Assign it to a variable called euro12.

# In[140]:


euro12 = pd.read_csv("Euro_2012_stats_TEAM.csv", skipfooter=4, engine='python')

print("data-frame shape: ", euro12.shape)
print("---------------------")
print("Columns: ", euro12.columns.values)


# # Step 4. Select only the Goal column.

# In[141]:


print(euro12["Goals"])
print("---------------------")
print(euro12.Goals)


# # Step 5. How many team participated in the Euro2012?

# In[148]:



print(len(euro12["Team"]))
print("------------------")
print(euro12["Team"])


# # Step 6. What is the number of columns in the dataset?

# In[79]:


len(euro12.columns)


# # Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline

# In[143]:


discipline = pd.DataFrame(euro12[["Team", "Yellow Cards", "Red Cards"]])


print(discipline)


# # Step 8. Sort the teams by Red Cards, then to Yellow Cards

# In[144]:


discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending=False)


# # Step 9. Calculate the mean Yellow Cards given per Team

# In[81]:


discipline["Yellow Cards"].mean() 


# # Step 10. Filter teams that scored more than 6 goals

# In[77]:


euro12[euro12.Goals > 6]


# # Step 11. Select the teams that start with G

# In[87]:



euro12[euro12.Team.str[0] == 'G']


# # Step 12. Select the first 7 columns

# In[145]:


euro12.iloc[:, 0:7]


# # Step 13. Select all columns except the last 3.

# In[146]:


euro12.iloc[:, 0:32]


# # Step 14. Present only the Shooting Accuracy from England, Italy and Russia

# In[147]:


euro12.iloc[[3,7,12], [0,4]]


# # Step 15. Use apply method on Goal Column to make a new column called Performance, using following conditions
# 1 - If Goals are less than or equal to 2, peformance is Below Avg
# 2 - If Goals are more than 2 and less than or equal to 5, peformance is Average
# 3 - If Goals are more than 5 and less than or equal to 10, peformance is Above Average
# 4 - If Goals are more than 10 then peformance is Excellent

# In[159]:


def condition(Goals):
    if Goals > 10:
        return "Excellent"
    elif Goals > 5:
        return "Above Average"
    elif Goals > 2:
        return "Average"
    else:
        return "Below Average"
    
euro12['Performance'] = euro12.Goals.apply(condition)

euro12[["Team", "Goals", "Performance"]]


# In[ ]:





# In[ ]:





# In[ ]:




