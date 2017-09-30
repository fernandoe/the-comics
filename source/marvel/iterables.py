from marvel.request import MarvelRequest


class CharactersIterable(object):
    def __init__(self):
        self.current_page = 0
        self.items = []

    def __iter__(self):
        return self

    def __next__(self):
        if not self.items:
            self.current_page = self.current_page + 1
            items = MarvelRequest().characters(self.current_page)
            if items:
                self.items = items
            else:
                raise StopIteration
        return self.items.pop(0)


class StoriesByCharacterIterable(object):
    def __init__(self, character_id):
        self.character_id = character_id
        self.current_page = 0
        self.items = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_page == 5:
            raise StopIteration
        if not self.items:
            self.current_page = self.current_page + 1
            items = MarvelRequest().stories_by_character(self.character_id, self.current_page)
            if items:
                self.items = items
            else:
                raise StopIteration
        return self.items.pop(0)
