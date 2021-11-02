import json

class ParseWiki:

    def __init__(self, path):
        self.file = open(path)
        with open(path, encoding='utf-8') as f:
            self.file = json.load(f)

    def __iter__(self):
        return self

    def __next__(self):

        data = self.file.pop()
        item_wiki_page = data['name']['common'] + ' ' + 'https://en.wikipedia.org/wiki/' + data['name']['common'].replace(' ', '_')
        return item_wiki_page

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self




with ParseWiki('countries.json') as wiki_iter:
    with open('result.txt', "w", encoding="utf-8") as result_file:
        for item in wiki_iter:
            result_file.write(item+'\n')

