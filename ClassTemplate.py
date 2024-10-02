# Definicija klase
class ClassTemplate:
    def __init__(self, name="ClassTemplate"):
        # Kreira se prazan atribut self.results, koji je lista, a koristi se za pohranu rezultata parsiranja ili dummy podataka. 
        # Ovo je glavni atribut koji druge klase, poput QuotesToScrape, mogu nadograditi vlastitim rezultatima parsiranja.
        # To znači da kada stvoriš objekt iz te klase, automatski se stvara prazan popis koji možeš kasnije popuniti podacima.
        self.results = []

    def parse(self, soup):
        print("CODE HERE")

        #   PRIMJER LISTE OBJEKATA (ATRIBUTI SU DUMMY PODATCI, SLUŽI SAMO KAO PRIMJER STRUKTURE OUTPUTA)
        self.results = [
            {
                "title": "Object 1",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas bibendum nisl eu maximus convallis. Maecenas suscipit, augue eu viverra suscipit, quam est luctus neque, vel consequat eros felis eu eros. Ut mollis suscipit vulputate. Aliquam erat volutpat. Phasellus nec dui aliquet, ornare urna vitae, placerat justo. Fusce mauris ipsum, porttitor sed cursus id, venenatis a erat. Nulla dui urna, semper sit amet porta in, dapibus eget ante. Sed consequat lacinia vestibulum. Donec porttitor nisl vel dui congue vulputate. Quisque hendrerit neque vel libero lobortis efficitur.",
                "price": 100,
            },
            {
                "title": "Object 2",
                "description": "Proin ac tortor et nisl pretium hendrerit eu sit amet arcu. Integer risus purus, varius eget dui auctor, dictum mollis lacus. Etiam sit amet metus ante. Donec et tortor mattis, efficitur purus vitae, porta arcu. Phasellus dictum, felis viverra euismod tristique, libero lorem facilisis odio, non luctus diam nisl vitae turpis. Aliquam at turpis quis nisl placerat tincidunt. Nam a hendrerit elit. Vivamus eget mi porta, pulvinar massa in, eleifend augue. ",
                "price": 150,
            },
            {
                "title": "Object 2",
                "description": "Integer neque ex, tincidunt in suscipit in, elementum sit amet neque. Quisque pulvinar dui eget tellus porttitor, sed fringilla ligula imperdiet. Sed eu sem justo. Etiam a ullamcorper ipsum. Pellentesque varius orci vel velit cursus suscipit. Proin at congue nisl. Suspendisse vitae dolor in risus molestie tempor. Suspendisse nec metus magna. Proin sed quam lectus. Proin scelerisque dui purus, aliquam vehicula purus commodo id. Praesent fermentum ante semper erat rhoncus, eu congue ligula sollicitudin. Pellentesque viverra vehicula auctor. Sed quis lacus sem. ",
                "price": 250,
            },
        ]

        return self.results
