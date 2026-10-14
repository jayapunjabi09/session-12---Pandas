import pandas as pd

data = {
    'category': ['Mobile', 'Laptop', 'Mobile', 'Laptop', 'Shoes'],
    'region': ['West', 'North', 'West', 'North', 'South'],
    'sales': [10000, 20000, 15000, 25000, 5000],
    'units_sold': [5, 2, 7, 3, 10]
}

df = pd.DataFrame(data)

result = df.groupby(['category', 'region']).agg({
    'sales': 'sum',
    'units_sold': 'mean'
})

print("Total Sales and Average Units Sold:")
print(result)