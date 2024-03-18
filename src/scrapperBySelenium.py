from threading import Thread
from src.seleniumScrapper.freeImages import FreeImages
from src.export.export import Export


class ExtractorSelenium(FreeImages):

    def __init__(self) -> None:
        self.itens = []
        self.status = "initiated"
        self.path_db = "db\\db_crawlers.sqlite"
        self.tb_db = "crawlers_selenium"
        super().__init__()

    def __str__(self) -> str:
        return self.status

    def run(self, num_pages):
        self.handle_login()
        self.iterate(num_pages)
        # self.handle_logout()
        self.status = f"finished, {len(self.itens)} itens found in website"

    def iterate(self, num_pages):
        for self.page in range(1, num_pages + 1):
            self.dogs()

    def export(self):
        return Export(self.itens).as_sqlite(path=self.path_db, tb_name=self.tb_db)
