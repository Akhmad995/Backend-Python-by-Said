from flask import jsonify, request
from flask_restful import Resource, reqparse

from models import Post, db

parser = reqparse.RequestParser()
parser.add_argument('title', required=True, type=str)
parser.add_argument('text', required=True, type=str)
parser.add_argument('author_id', required=True, type=int)


# Класс для управления списком объектов.
class PostListResource(Resource):
    # Метод получения списка объектов публикаций
    def get(self):
        posts = Post.query.all()
        return jsonify(
            {
                'posts': [
                    post.to_dict(only=('title',))
                    for post in posts
                ]
            }
        )

    # Метод добавления объекта публикации
    def post(self):
        args = parser.parse_args()
        post = Post(
            title = args['title'],
            text = args['text'],
            author_id = args['author_id']
        )
        db.session.add(post)
        db.session.commit()
        return jsonify(
            {
                'posts': post.to_dict(only=('title',))
                #'success': 'OK'
            }
        )


# Класс для управления отдельным объектом.
class PostResource(Resource):
    # Получение отдельного объекта статьи
    def get(self, post_id):
        return {'message': f'Get {post_id}'}

    # Замена существующего объекта статьи
    def put(self, post_id):
        return {'message': f'Put {post_id}'}

    # Удаление объекта статьи
    def delete(self, post_id):
        return {'message': f'Delete {post_id}'}