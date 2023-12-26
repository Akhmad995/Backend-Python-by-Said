
from config import app, api, db
from posts_resurces import PostListResource, PostResource


# Добавление данных о классах и соответствующих им URL в API.
api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<int:post_id>')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run('127.0.0.1', 8080)
