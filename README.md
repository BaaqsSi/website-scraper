# website-scraper
ეს პროეკტი არის მარტივი web scraper -ი რომელიც website - იდან ინფორმაციას იღებს და ათავსებს csv file -ში

#როგორ მუშაობს...
ეს პროეკტი არის დაწერილი პითონში და არის გამოყენებული requests ,time , csv და bs4 მოდულები ის იღებს html კოდს და ანაწილებს წიგნების ფასსა და სახელს შემდეგ კი გადააქ books.csv ში.
ამ ყველაფერს აკეთებს 5 გვერდზე -ზე და თითოეული გვერდის scrap - ის მერე აქვს 15 წამიანი delay რომ სერვერი ზედმეტი request-ებით არ გადატვირთოს.

საიტი კი ავირჩიე:
http://books.toscrape.com
ტესტირებისათვის
