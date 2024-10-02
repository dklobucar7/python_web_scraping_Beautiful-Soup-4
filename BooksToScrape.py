from ClassTemplate import ClassTemplate




class BooksToScrape(ClassTemplate):
    """
    Ova klasa nasljeđuje ClassTemplate klasu i koristi se za parsiranje podataka s books_to_scrape_test.html.

    Klasa dohvaća informacije o knjigama:
        - url -> URL NA KOJEM SE MOGU VIDJETI DETALJI TE KNJIGE
        - title -> TITLE TE KNJIGE (PO MOGUĆNOSTI UZETI CIJELI TITLE)
        - stock -> 0 ILI 1 OVISNO O JELI KNJIGA DOSTUPNA ZA KUPITI (0-NE, 1-DA)
        - price -> CIJENA KJNIGE (MORA BITI float TIP)
        - rating -> RATING KNJIGE (OD 0-5, OVISNO KOLIKO ZVIJEZDA IMA KNJIGA)


    Atributi:
    - results: Lista koja sadrži rezultate parsiranja

    Metode:
    - parse: Parsira HTML i dohvaća podatke
    """

    def __init__(self):
        super().__init__(self)

    def parse(self, soup):
        # Osnovni URL
        BASE_URL = "https://books.toscrape.com/"
        
        for list_item in soup.find_all('li', {"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"}):
            
            article = list_item.find("article" , {"class": "product_pod"})
            h3 = article.find('h3')
            tag_a = h3.find('a')
            
            # url
            url_href = tag_a["href"]
            url= f"{BASE_URL}{url_href}"
            
            # title
            title = tag_a["title"].strip()
            
            # stock
            stock_p = list_item.find('p', {"class":"instock availability"})
            stock_text = stock_p.text.strip().lower()
            
            if stock_text == "in stock":
                stock = 1
            else:
                stock = 0
                
            #price
            sale_price_p = list_item.find('p', {"class":"price_color"})
            sale_price_text = sale_price_p.text.strip()[1:]
            sale_price = float(sale_price_text)
            
            #raiting
            rating_p = list_item.find('p', class_='star-rating')['class']
            rating_word = rating_p[1]
            
            rating_map = {
                'One': 1,
                'Two': 2,
                'Three': 3,
                'Four': 4,
                'Five': 5
            }
            rating = rating_map.get(rating_word, 0)
            
            # Dodavanje rezultata u listu
            self.results.append({"url":url, "title":title,"stock":stock,"price":sale_price, "rating": rating})
        return self.results

