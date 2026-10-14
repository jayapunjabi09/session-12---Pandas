import pandas as pd

data = {
    'region': ['North', 'South', 'North', 'South', 'West', 'West'],
    'revenue': [10000, 15000, 20000, 12000, 25000, 18000]
}

df = pd.DataFrame(data)

result = df.groupby('region').agg({
    'revenue': ['sum', 'max', 'min']
})

result = result.sort_values(
    by=('revenue', 'sum'),
    ascending=False
)

print("Revenue by Region:")
print(result)