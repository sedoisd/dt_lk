from requests import get, post, delete

print(delete('http://localhost:8080/api/news/999').json())
# новости с id = 999 нет в базе

print(delete('http://localhost:8080/api/news/5').json())