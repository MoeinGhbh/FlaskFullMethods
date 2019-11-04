from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    data = ['Index Page', 'My Header', 'red']
    return render_template('index.html', data=data)


@app.route("/hello")
def hello():
    data = ['Hello Page', 'My Header', 'orange']
    return render_template('index.html', data=data)


@app.route('/user/&lt;username&gt;')
def show_user(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/&lt;int:post_id&gt;')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)