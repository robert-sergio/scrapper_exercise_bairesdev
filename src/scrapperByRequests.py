from threading import Thread
from crawlers.istockphoto import IstockPhoto
from export.export import Export


class Extractor(IstockPhoto):
    def __init__(self) -> None:
        self.itens = []
        self.status = "initiated"
        super().__init__()

    def __str__(self) -> str:
        return self.status

    def run(self, num_pages):
        self.iterate(num_pages)
        self.status = f"finished"

    def iterate(self, num_pages):
        p = []
        for self.page in range(1, num_pages + 1):
            b = Thread(target=self.dogs, args=[], daemon=False)
            b.start()
            p.append(b)

        for x in p:
            x.join()

    def export(self):
        return Export(self.itens).as_sqlite()


if __name__ == "__main__":
    bot = Extractor()
    bot.run(num_pages=1)
    bot.export()