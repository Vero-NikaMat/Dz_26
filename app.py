
from flask import Flask, request, render_template
from functions import open_file, post_and_comment, comment_post_id

posts, comments, bookmarks = open_file()
app = Flask(__name__)


@app.route('/')
def home_page():
    posts = post_and_comment()
    return render_template('index.html', posts=posts)


@app.route('/posts/<pk>')
def posts():
    posts, comments, bookmarks = open_file()
    pk = request.values.get('pk')
    post = posts[pk]
    comments_pk = comment_post_id(pk)

    return render_template('post.html', comments=comments_pk, post=post)



if __name__ == "__main__":
    app.run(debug=True)
