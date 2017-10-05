import os

from marvel.request import MarvelRequest


class BaseIterable(object):
    def __init__(self, **kwargs):
        self.current_page = 0
        self.items = []
        self.limit_pages = os.environ.get("TC_LIMIT_PAGES", None)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit_pages is not None and self.current_page == int(self.limit_pages):
            raise StopIteration
        if not self.items:
            self.current_page = self.current_page + 1
            items = self.get_items()
            if items:
                self.items = items
            else:
                raise StopIteration
        return self.items.pop(0)


class CharactersIterable(BaseIterable):
    def get_items(self):
        return MarvelRequest().characters(page=self.current_page)


class StoriesByCharacterIterable(BaseIterable):
    def get_items(self):
        return MarvelRequest().stories_by_character(self.identifier, self.current_page)


class ComicsByCharacterIterable(BaseIterable):
    def get_items(self):
        return MarvelRequest().comics_by_character(self.identifier, self.current_page)


class CharacteresByComicIterable(BaseIterable):
    def get_items(self):
        return MarvelRequest().characters_by_comic(self.identifier, self.current_page)
