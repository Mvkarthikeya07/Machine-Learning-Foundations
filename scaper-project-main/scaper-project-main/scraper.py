import requests
from bs4 import BeautifulSoup
import csv

# Conversion rate
GBP_TO_INR = 107

# Create the CSV file
with open('books_data_inr.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price (₹)', 'Rating', 'Availability'])

    # Loop through all pages
    for page in range(1, 51):
        url = f'https://books.toscrape.com/catalogue/page-{page}.html'
        response = requests.get(url)
        response.encoding = 'utf-8'  # ✅ Fix encoding issue

        if response.status_code != 200:
            print(f"❌ Failed to fetch page {page}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('article', class_='product_pod')

        for book in books:
            title = book.h3.a['title']

            # ✅ Remove £ and any stray characters
            price_text = book.find('p', class_='price_color').text.strip()
            price_clean = price_text.replace('£', '').replace('Â', '')
            price_inr = round(float(price_clean), 2) * GBP_TO_INR

            rating_classes = book.find('p', class_='star-rating')['class']
            rating = rating_classes[1] if len(rating_classes) > 1 else 'Not Rated'

            availability = book.find('p', class_='instock availability').get_text(strip=True)

            writer.writerow([title, f'₹{price_inr}', rating, availability])
            print(f"✔️ {title} | ₹{price_inr} | {rating} | {availability}")

print("\n✅ Done! Data saved in books_data_inr.csv")


