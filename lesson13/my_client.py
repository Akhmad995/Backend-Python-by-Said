# Делаем запросы к нашему приложению.
from requests import get, post


print(get('http://localhost:8080/posts').json())

print(post(
    'http://localhost:8080/posts',
    json={
        'title': 'Заголовок 2',
        'text': 'Текст публикации',
        'author_id': 4,
        }).json()
)

# print(get('http://localhost:8080/posts/1').json())
# print(put('http://localhost:8080/posts/1', json={'name': 'Saeed'}).json())
# print(delete('http://localhost:8080/posts/1').json())
