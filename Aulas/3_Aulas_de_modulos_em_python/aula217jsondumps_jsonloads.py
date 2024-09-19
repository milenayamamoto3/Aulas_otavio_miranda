# json.dumps -> pra fora (python -> json) com str
# json.loads -> pra dentro (json -> python) com str
# typing.TypedDict

# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null
import json
# from pprint import pprint #pretty print
from typing import TypedDict


class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


string_json_py = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''
movie: Movie = json.loads(string_json_py)
# pprint(movie, width=40)  #width = largura
# print(movie['title'])
# print(movie['characters'][0])
# print(movie['year'] + 10)

string_py_json = json.dumps(movie, ensure_ascii=False, indent=2) #indent = indentação
print(string_py_json)