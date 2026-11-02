# simulate spark-like behavior using python's pandas
import pandas as pd

# step 1: load data (simulating spark dataframes)
# sample transaction data
data = {'CustomerID': ['Alice', 'Bob', 'Alice', 'Bob', 'Charlie'],  
        'Amount': [20, 50, 30, 20, 40]}  

df = pd.DataFrame(data)  # Simulating a Spark DataFrame  
print(df) 