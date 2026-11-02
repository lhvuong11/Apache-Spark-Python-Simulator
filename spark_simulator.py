# Simulating Spark Data Processing in Python
# Assignment 2 

import pandas as pd

# step 1: load data into pandas DF (simulating spark dataframes)
data = {  
    'UserID': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C'],  
    'Page': ['Home', 'About', 'Home', 'Contact', 'Home', 'About', 'Home', 'About'],  
    'Duration': [30, 40, 25, 35, 20, 15, 50, 45]  
}

df = pd.DataFrame(data) 
#print(df) 

# step 2: perform transformations

# 2.1: calculate the total time spent per user
total_time = df.groupby('UserID').sum()  # simulating Spark's groupBy().sum() operation  
user_list = total_time.index.tolist()  # saving the users ID into a list to print
print("\nTotal Time Spent Per User:")

for id in user_list:
    print(f"User {id}: {total_time.loc[id, 'Duration']} sec")
#print(f"User {user_list}: {total_time['Duration']}")

# 2.2: find the most visted page using a group-by operation
page_counts = df.groupby('Page').size()
highest_page = page_counts.idxmax()  #returns highest 'Page' element
print(f"\nMost Visted Page: {highest_page} ({page_counts.loc[highest_page]} visits)")


# 2.3: compute the average time spent per page
avg_time = df.groupby('Page')['Duration'].mean()

print("\nAverage Time Spent Per Page:")
for time in avg_time.index:
    print(f"{time} - {avg_time.loc[time]:.2f} sec")

