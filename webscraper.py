import requests
import time
import csv
from bs4 import BeautifulSoup

def scrapping(url):
    books = []#list -ი რომელშიც მოთავსდება ფასი და სახელი წიგნის
    try:
        # GET მოთხოვნა გაგზავნილია URL-ზე
        resp = requests.get(url)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text , "html.parser") # HTML კონტენტის  parsing
        # ყველა "article" ელემენტის მოძებნა "product_pod" კლასით
        items = soup.find_all("article",class_="product_pod")

        # წიგნის სათაურისა და ფასის გამოტანა თითოეული წიგნისთვის
        for item in items:
            name = item.h3.a["title"]
            price = item.find("p", class_="price_color").text.strip()
            books.append((name,price)) # სათაურისა და ფასის დამატება სიაში

    except requests.exceptions.RequestException as e:
        price(f"erroria {e}")

    return books #დააბრუნებს წიგნების სიას
def main():
    csv_file = "books.csv"
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        b_url = "http://books.toscrape.com/catalogue/page-{}.html"


        for page in range(1,6):
            url = b_url.format(page) # ამოწმებს url-ს ამ გვერდის ნომრით
            books = scrapping(url)
            
            # თითოეული წიგნის სათაურისა და ფასის ჩაწერა CSV ფაილში
            for book in books:
                writer.writerow([f"Name: {book[0]}", f"  Price: {book[1]}"])
                writer.writerow("") 
            print(f"saiti's page {page} daiscrapa ")
            time.sleep(15 + (5 * page))
        
    print(f"websites scrapping dasrulda da informacia motavsda {csv_file} - shi")


if __name__ == "__main__":
    main()
