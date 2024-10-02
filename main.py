import sys
import mysql.connector
import json
from bs4 import BeautifulSoup
from BookDepository import BooksDepository
from BooksToScrape import BooksToScrape
from QuotesToScrape import QuotesToScrape

#   TODO NAPRAVITI KLASE ZA SVAKU VRSTU HTML-A
#   TODO SVAKA OD TIH KLASA TREBA IMATI METODU parse() KOJA PRIMA SOUP IZ MAIN-A I VRAĆA ARRAY OBJEKATA

#   TODO SVAKA OD KLASA TREBA DA VRATI LISTU OBJEKATA SA ODREĐENOM STRUKTUROM, OVISNO O KOJOJ SE STRANICI RADI

#   ZADATAK 1:
#   http://quotes.toscrape.com/
#   quotes_to_scrape_test.html MORA VRATITI LISTU OBJEKTA KOJI SVI IMAJU:
#                                                                        url -> URL NA KOJEM SE MOGU VIDJETI DETALJI AUTORA
#                                                                        author -> IME AUTORA
#                                                                        text -> TEXT QUOTE-A
#                                                                        tags -> ARRAY (LISTA) SA TEXTOM SVIH TAGOVA U QUOTE-U

#   ZADATAK 2
#   https://books.toscrape.com/
#   books_to_scrape_test.html i MORAJA VRATITI LISTU OBJEKTA KOJI SVI IMAJU:
#                                                                            url -> URL NA KOJEM SE MOGU VIDJETI DETALJI TE KNJIGE
#                                                                            title -> TITLE TE KNJIGE (PO MOGUĆNOSTI UZETI CIJELI TITLE)
#                                                                            stock -> 0 ILI 1 OVISNO O JELI KNJIGA DOSTUPNA ZA KUPITI (0-NE, 1-DA)
#                                                                            price -> CIJENA KJNIGE (MORA BITI float TIP)
#                                                                            rating -> RATING KNJIGE (OD 0-5, OVISNO KOLIKO ZVIJEZDA IMA KNJIGA)

#   ZADATAK 3
#   https://www.bookdepository.com/category/2638/History-Archaeology
#   books_depository_test.html i MORAJA VRATITI LISTU OBJEKTA KOJI SVI IMAJU:
#                                                                            url -> URL NA KOJEM SE MOGU VIDJETI DETALJI TE KNJIGE
#                                                                            title -> TITLE TE KNJIGE (PO MOGUĆNOSTI UZETI CIJELI TITLE)
#                                                                            stock -> 0 ILI 1 OVISNO O JELI KNJIGA DOSTUPNA ZA KUPITI (0-NE, 1-DA)
#                                                                            price -> CIJENA KJNIGE (MORA BITI float TIP)
#                                                                            low_price -> NAJNIŽA CIJENA KJNIGE U 30 DANA (30-day low price), AKO NE POSTOJI MORA BITI ISTI KAO I PRICE (MORA BITI float TIP)
#                                                                            rating -> RATING KNJIGE (OD 0-5, OVISNO KOLIKO ZVIJEZDA IMA KNJIGA)
#                                                                            category -> KATEGORIJA U KOJOJ JE KNJIGA SVRSTANA (New and recent, Bestselling History Titles, ...)


def create_database():
    # Povezivanje s MySql serverom
    connection = mysql.connector.connect(host="localhost", user="root", passwd="1234")

    cursor = connection.cursor()

    # Kreiranje baze podataka
    cursor.execute("CREATE DATABASE IF NOT EXISTS book_scraper_db")

    cursor.execute("SHOW DATABASES")

    for _ in cursor:
        print(_)

    # Zatvori vezu
    cursor.close()
    connection.close()


def create_tables():
    connection = mysql.connector.connect(
        host="localhost", user="root", passwd="1234", database="book_scraper_db"
    )

    cursor = connection.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS quotes_to_scrape (
        id INT AUTO_INCREMENT PRIMARY KEY,
        url VARCHAR(255),
        author VARCHAR(255),
        text TEXT,
        tags JSON
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS books_to_scrape (
        id INT AUTO_INCREMENT PRIMARY KEY,
        url VARCHAR(255),
        title VARCHAR(255),
        stock TINYINT(1),
        price FLOAT,
        rating INT
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS book_depository (
        id INT AUTO_INCREMENT PRIMARY KEY,
        url VARCHAR(255),
        title VARCHAR(255),
        stock TINYINT(1),
        price FLOAT,
        low_price FLOAT,
        rating INT,
        category VARCHAR(255)
    )
    """
    )

    connection.commit()
    cursor.execute("DESCRIBE quotes_to_scrape")

    for _ in cursor:
        print(_)

    cursor.execute("DESCRIBE books_to_scrape")

    print(cursor.fetchall())

    cursor.execute("DESCRIBE book_depository")

    print(cursor.fetchall())

    cursor.close()
    connection.close()


def insert_books_to_scrape_data(results):
    connection = mysql.connector.connect(
        host="localhost", user="root", passwd="1234", database="book_scraper_db"
    )

    cursor = connection.cursor()

    for item in results:
        sql = "INSERT INTO books_to_scrape (url, title, stock, price, rating) VALUES (%s, %s, %s, %s, %s)"
        val = (item["url"], item["title"], item["stock"], item["price"], item["rating"])
        cursor.execute(sql, val)
    connection.commit()

    cursor.execute("select * from books_to_scrape")
    for _ in cursor:
        print(_)

    cursor.close()
    connection.close()


def insert_quotes_to_scrape_data(results):
    connection = mysql.connector.connect(
        host="localhost", user="root", passwd="1234", database="book_scraper_db"
    )
    cursor = connection.cursor()

    for item in results:
        sql = "INSERT INTO quotes_to_scrape (url, author, text, tags) VALUES (%s, %s, %s,%s)"
        val = (item["url"], item["author"], item["text"], json.dumps(item["tags"]))
        cursor.execute(sql, val)
    connection.commit()

    cursor.execute("select * from quotes_to_scrape")

    for _ in cursor:
        print(_)
    cursor.close()
    connection.close()


def insert_book_depository_data(results):

    connection = mysql.connector.connect(
        host="localhost", user="root", passwd="1234", database="book_scraper_db"
    )
    cursor = connection.cursor()

    for item in results:
        sql = "INSERT INTO book_depository (url, title, stock, price, low_price, rating, category) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (
            item["url"],
            item["title"],
            item["stock"],
            item["price"],
            item["low_price"],
            item["rating"],
            item["category"],
        )
        cursor.execute(sql, val)
    connection.commit()

    cursor.execute("select * from book_depository")

    for _ in cursor:
        print(_)
    cursor.close()
    connection.close()


QUOTES_TO_SCRAPE = "quotes_to_scrape_test.html"
BOOKS_TO_SCRAPE = "books_to_scrape_test.html"
BOOK_DEPOSITORY = "book_depository_test.html"


# Osigurava da se kod unutar njega izvršava samo kada se datoteka pokreće direktno, a ne kad je uvezena kao modul u drugi Python program.
if __name__ == "__main__":
    # Kreiranje baze podataka
    # create_database()

    # Kreiraj tablice
    # create_tables()

    # Provjera broja argumenata - provjera koliko argumenata je proslijeđeno prilikom pokretanja programa
    # sys.argv je lista argumenata koji su proslijeđeni programu putem naredbenog retka.
    # sys.argv[0] je naziv skripte, a sys.argv[1] je prvi argument (ime datoteke koja se prosljeđuje
    # Ovaj dio provjerava je li korisnik dao barem jedan argument (ime datoteke).
    if len(sys.argv) < 2:
        print("Invalid number of arguments.")
    else:
        # uzima prvi argument s komandne linije (ime HTML datoteke koju korisnik prosljeđuje).
        file_name = sys.argv[1]

        # otvara tu HTML datoteku i čitamo njezin sadržaj. Otvaramo u načinu čitanja (read mode) s UTF-8 kodiranjem, osiguravajući da se znakovi pravilno očitavaju.
        with open(file_name, encoding="utf8") as fp:
            # Ovdje stvaramo objekt soup, koristeći BeautifulSoup i "lxml" parser. soup sada sadrži cjelokupan HTML dokument, strukturiran i spreman za daljnju obradu.
            soup = BeautifulSoup(fp, "lxml")
            #   TODO OVDJE NASTAVITI

            #   TODO OVISNO O IMENU FILE-A (file_name) TREBA DODIJELITI JEDNU KLASU KOJA TREBA BITI DEFINIRANA RANIJE U KODU

            #   TE IZ TE KLASE ZOVNUTI parse() FUNKCIJU KOJA ĆE VRATITI LISTU OBJEKATA I DODIJELITI GA VARIJABLI
            # Logika odabira parsera

            if file_name == BOOK_DEPOSITORY:
                # Instancira se odgovarajuća klasa (parser).
                parser = BooksDepository()
                # Zove se metoda parse() koja će obraditi sadržaj (HTML/XML) i vratiti rezultat.
                result = parser.parse(soup)
                insert_book_depository_data(result)
                # Ispisuje se rezultat na ekran pomoću print(result).
                print(result)
            elif file_name == BOOKS_TO_SCRAPE:
                parser = BooksToScrape()
                result = parser.parse(soup)
                insert_books_to_scrape_data(result)
                # print(result)
            elif file_name == QUOTES_TO_SCRAPE:
                parser = QuotesToScrape()
                result = parser.parse(soup)
                insert_quotes_to_scrape_data(result)
                print(result)
            else:
                #   TODO AKO SE ZATRAŽI FILE KOJI NE POSTOJI TREBA SE ISPISATI PORUKA KOJA TO KAŽE
                # Ako ime datoteke ne odgovara nijednom od navedenih, ispisuje se poruka o grešci:
                print("ERROR: File {} doesn't exists!".format(file_name))

    # za pokretanje programa: python main.py quotes_to_scrape_test.html
    """
    python – Ova naredba pokreće Python interpretator. U terminalu, kada napišeš python, to znači da želiš pokrenuti Python program.

    main.py – Ovo je naziv tvoje skripte, tj. Python datoteke koju pokrećeš. U ovom slučaju, main.py je tvoj program i to je sys.argv[0], što znači da je to prvi argument koji Python automatski dodeljuje kao naziv pokrenutog programa. Ne treba ga definirati u bloku

    quotes_to_scrape_test.html – Ovo je sys.argv[1], što je prvi argument koji ti prosljeđuješ svom programu iz naredbenog retka. U ovom slučaju, to je naziv HTML datoteke koju želiš obraditi pomoću svog programa.
    """
