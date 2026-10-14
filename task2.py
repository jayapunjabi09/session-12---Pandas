import pandas as pd

data = {
    'city': ['Ahmedabad', 'Surat', 'Ahmedabad', 'Surat', 'Ahmedabad'],
    'restaurant': ['KFC', 'Dominos', 'KFC', 'Dominos', 'Pizza Hut'],
    'order_amount': [500, 600, 700, 800, 900]
}

df = pd.DataFrame(data)

result = df.groupby(['city', 'restaurant'])['order_amount'].mean()

print("Average Order Amount:")
print(result)