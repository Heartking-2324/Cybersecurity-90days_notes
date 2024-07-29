# Web Scraping with Python and BeautifulSoup

## Day 25: Building a Web Scraper

This repository contains a step-by-step guide on how to build a web scraper using Python and BeautifulSoup. Follow the instructions below to get started.

## Getting Started

To build a web scraper using Python and BeautifulSoup, follow these steps:

### Step 1: Install BeautifulSoup Library

First, you need to install the BeautifulSoup library. Open your terminal and run the following command:

```bash
pip install beautifulsoup4
```

### Step 2: Import Necessary Libraries

In your Python script, import the necessary libraries:

```python
import requests
from bs4 import BeautifulSoup
```

### Step 3: Fetch HTML Content

Fetch the HTML content of the website you want to scrape:

```python
url = 'https://example.com'
response = requests.get(url)
html_content = response.text
```

### Step 4: Create a BeautifulSoup Object

Create a BeautifulSoup object to parse the HTML:

```python
soup = BeautifulSoup(html_content, 'html.parser')
```

### Step 5: Extract Data

Use BeautifulSoup to extract the desired data. For example, extracting product prices and reviews:

```python
# Example: Extracting product prices
prices = []
for product in soup.find_all('div', class_='product'):
    price = product.find('span', class_='price').text
    prices.append(price)

# Example: Extracting reviews
reviews = []
for review in soup.find_all('div', class_='review'):
    review_text = review.find('p').text
    reviews.append(review_text)
```

### Step 6: Store Scraped Data

Store the scraped data in a CSV or JSON file:

```python
import csv
import json

# Write data to a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Price', 'Review'])
    for price, review in zip(prices, reviews):
        writer.writerow([price, review])

# Write data to a JSON file
data = {'prices': prices, 'reviews': reviews}
with open('scraped_data.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
```

### Example Script

Here's an example of a web scraper script that scrapes product prices and reviews from a sample website:

```python
import requests
from bs4 import BeautifulSoup
import csv

# Specify the URL
url = 'http://books.toscrape.com/'

# Fetch the HTML content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Lists to store titles and prices
    titles = []
    prices = []
    
    # Iterate over book elements
    for product in soup.find_all('article', class_='product_pod'):
        title = product.h3.a['title']
        price = product.find('p', class_='price_color').text
        
        titles.append(title)
        prices.append(price)
    
    # Check if any data was found
    if titles and prices:
        # Write data to a CSV file
        with open('books_scraped_data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title', 'Price'])
            for title, price in zip(titles, prices):
                writer.writerow([title, price])
        print("Data saved to books_scraped_data.csv")
    else:
        print("No data found. Check the HTML structure and class names.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
```
The report which will be generated will look like this
![]()
## Alternative Libraries

There are several alternative libraries for web scraping in Python:

- **Scrapy**: A powerful web scraping framework
- **Selenium**: Automates web browser interaction for dynamic content
- **Requests-HTML**: Provides an alternative syntax to BeautifulSoup for scraping

## Conclusion

This script demonstrates how to scrape data from a website using BeautifulSoup. You can modify the code to extract different types of data based on the structure of the website you are scraping. Happy scraping!
---
