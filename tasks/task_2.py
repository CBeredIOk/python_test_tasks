
class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = -1

    def __str__(self):
        str_of_book = (
            f'Title: {self.title}, '
            f'Author: {self.author}, '
            f'Pages: {self.pages}, '
            f'Current Page: {self.current_page}'
        )
        return str_of_book

    def turn_page(self, flip_pages: int = 1) -> None:
        try:
            self.current_page += flip_pages
            if self.current_page > self.pages:
                self.current_page = self.pages
            elif self.current_page < 0:
                self.current_page = -1
        except TypeError:
            print('Only an integer must be entered')
