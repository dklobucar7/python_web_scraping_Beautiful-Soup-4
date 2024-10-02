from ClassTemplate import ClassTemplate

class BooksDepository(ClassTemplate):
    
    """
    Ova klasa nasljeđuje ClassTemplate klasu i služi za parsiranje podataka s book_depository_test.html.

    Klasa dohvaća informacije o knjigama:
        - url -> URL NA KOJEM SE MOGU VIDJETI DETALJI TE KNJIGE
        - title -> TITLE TE KNJIGE (PO MOGUĆNOSTI UZETI CIJELI TITLE)
        - stock -> 0 ILI 1 OVISNO O JELI KNJIGA DOSTUPNA ZA KUPITI (0-NE, 1-DA)
        - price -> CIJENA KJNIGE (MORA BITI float TIP)
        - low_price -> NAJNIŽA CIJENA KJNIGE U 30 DANA (30-day low price), AKO NE POSTOJI MORA BITI ISTI KAO I PRICE (MORA BITI float TIP)
        - rating -> RATING KNJIGE (OD 0-5, OVISNO KOLIKO ZVIJEZDA IMA KNJIGA)
        - category -> KATEGORIJA U KOJOJ JE KNJIGA SVRSTANA (New and recent, Bestselling History Titles, ...)


    Atributi:
    - results: Lista koja sadrži rezultate parsiranja

    Metode:
    - parse: Parsira HTML i dohvaća podatke
    """
    def __init__(self):
        super().__init__(self)

    def parse(self, soup):
        # Osnovni URL
        BASE_URL = "https://www.bookdepository.com"

        for carousel in soup.find_all('div', class_="carousel-wrap"):
            # category
            category_a = carousel.find('a', {"class": "next-btn"})
            category = category_a["data-title"].strip() if category_a else "None"

            # tražimo podatke o knjigama
            tab_wrap = carousel.find('div', class_="tab-wrap")
            if tab_wrap:
                for book_item in tab_wrap.find_all('div', {"class": "book-item"}):
                    title_h3 = book_item.find('h3', {"class": "title"})
                    title_a = title_h3.find('a')
                    
                    # url
                    url = f"{BASE_URL}{title_a['href']}"
                    
                    # title
                    title = title_a.text.strip()
                    
                    #stock
                    add_to_basket_btn = book_item.find('a', class_='add-to-basket')
                    stock = 1 if add_to_basket_btn else 0
                    
                    # price
                    sale_price_span = book_item.find('span', {"class": "sale-price"})
                    sale_price_text = sale_price_span.text.strip().split(" ")[0].replace(",", ".")
                    sale_price = float(sale_price_text)
                    
                    # low price
                    price_save_span = book_item.find('span', {"class": "price-save"})
                    if price_save_span:
                        price_save_text = price_save_span.text.strip().split(" ")[0].replace(",", ".")
                        price_save = float(price_save_text)
                    else:
                        price_save = sale_price
                    
                    # rating
                    rating_tag = book_item.find("div", class_="stars")
                    rating = len(rating_tag.find_all("span", class_="full-star")) if rating_tag else 0
                    
                    # Dodavanje rezultata u listu
                    self.results.append({
                        "url": url,
                        "title": title,
                        "stock":stock,
                        "price": sale_price,
                        "low_price": price_save,
                        "rating": rating,
                        "category": category  
                    })

        return self.results
