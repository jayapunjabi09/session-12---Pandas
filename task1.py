import pandas as pd

data = {
    'team': ['CSK', 'MI', 'RCB', 'CSK', 'MI', 'RCB'],
    'runs': [180, 200, 170, 190, 160, 210]
}

df = pd.DataFrame(data)

result = df.groupby('team')['runs'].sum()

print("Total Runs by Team:")
print(result)