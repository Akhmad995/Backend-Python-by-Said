# Делаем запросы к нашему приложению.
from requests import get, post, put, patch, delete


# print(get('http://localhost:8080/posts').json())

# print(post(
#     'http://localhost:8080/posts',
#     json={
#         'title': 'Изм. Заголовок',
#         'text': 'Изм. текст',
#         'author_id': 5,
#         }).json()
# )

print(get('http://localhost:8080/posts/6').json())
# print(put('http://localhost:8080/posts/1', json={'name': 'Saeed'}).json())
# print(delete('http://localhost:8080/posts/1').json())
