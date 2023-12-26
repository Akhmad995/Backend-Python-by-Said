
from config import app, api, db
from posts_resurces import PostListResource, PostResource
from analytics import analytics_blueprint

# Добавление данных о классах и соответствующих им URL в API.
api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<int:post_id>')
app.register_blueprint(analytics_blueprint)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run('127.0.0.1', 8080)
