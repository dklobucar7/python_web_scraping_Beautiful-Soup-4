from ClassTemplate import ClassTemplate
    

class QuotesToScrape(ClassTemplate):
    """
    Ova klasa nasljeđuje ClassTemplate klasu i služi za parsiranje podataka s quotes_to_scrape_test.html

    Klasa dohvaća informacije o knjigama:
        url -> URL NA KOJEM SE MOGU VIDJETI DETALJI AUTORA
        author -> IME AUTORA
        text -> TEXT QUOTE-A
        tags -> ARRAY (LISTA) SA TEXTOM SVIH TAGOVA U QUOTE-U


    Atributi:
    - results: Lista koja sadrži rezultate parsiranja

    Metode:
    - parse: Parsira HTML i dohvaća podatke
    """

    def __init__(self):
        super().__init__(self)

    def parse(self, soup):
        # Osnovni URL
        BASE_URL = "http://quotes.toscrape.com"
        
        for quote in soup.find_all('div', {"class":"quote"}):
            # url
            url_href = quote.find('a')['href']
            url = f"{BASE_URL}{url_href}"
            
            # author
            # .text dohvaća samo tekst unutar odabranog HTML elementa, ignorirajući sve HTML tagove. 
            author = quote.find('small', {"class":"author"}).text.strip()
            
            # text
            text = quote.find("span", {"class":'text'}).text.strip()
            
            # tags
            tags = quote.find_all("a", {"class": 'tag'})
            tag_list = []
            for tag in tags:
                tag_list.append(tag.text.strip())
                
            # Dodavanje rezultata u listu
            self.results.append({"url":url, "author":author, "text":text, "tags": tag_list})
            
        return self.results
    
    