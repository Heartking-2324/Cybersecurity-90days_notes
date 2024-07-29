import pandas as pd
import numpy as np

# Number of rows in the CSV
num_rows = 1000

# Possible values for categories and products
categories = ['Fiction', 'Non-Fiction', 'Science', 'Biography', 'Children', 'Fantasy'] # you can change accorfingly to usage 
products = ['Book ' + str(i) for i in range(1, num_rows + 1)]

# Generate random data
data = {
    'category': np.random.choice(categories, num_rows),
    'product': np.random.choice(products, num_rows),
    'price': np.random.uniform(5, 100, num_rows).round(2)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('books_scraped_data.csv', index=False) # create your own file with .CSV and add their 

print('CSV file generated successfully.')
