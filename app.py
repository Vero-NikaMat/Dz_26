
from flask import Flask, request, render_template, abort

from functions import open_file, post_and_comment, comment_post_id, one_post, user_posts, serch_post

posts, comments, bookmarks = open_file()
app = Flask(__name__)


@app.route('/')
def home_page():
    posts = post_and_comment()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:pk>')
def posts_uno(pk):
    posts, comments, bookmarks = open_file()
    post = one_post(pk)
    comments_pk = comment_post_id(pk)
    count = len(comments_pk)

    return render_template('post.html', comments=comments_pk, post=post, count=count)


@app.route('/users/<username>')
def posts_name(username):
    posts = user_posts(username)
    return render_template('user-feed.html', posts=posts)


@app.route('/search/')
def search_posts():
    s = request.args.get("word")
    if not s:
        abort(400)
    posts = serch_post(s)
    return render_template('search.html', posts=posts, count=len(posts))


if __name__ == "__main__":
    app.run(debug=True, port=8080)
