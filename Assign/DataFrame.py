import random as rd
import pandas as pd
import random as rd

yn = ['yes', 'no']
df2 = pd.DataFrame({
    'name': ['A', 'B', 'C', 'D'],
    'score': [float(rd.randint(0, 40)) / 2 for i in range(4)],
    'attempts': [rd.randint(1, 3) for i in range(4)],
    'qualify': [rd.choice(yn) for i in range(4)]  
})
df2.info
print(df2.info)
