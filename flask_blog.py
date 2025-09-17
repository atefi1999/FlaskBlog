from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Simple list for keeping posts
posts = []


@app.route("/")
def home():
    return render_template_string("""
        <h1>📖 My Simple Flask Blog</h1>
        <a href="{{ url_for('add_post') }}">➕ Add New Post</a>
        <ul>
        {% for post in posts %}
            <li><strong>{{ post.title }}</strong>: {{ post.content }}</li>
        {% else %}
            <p>No posts yet.</p>
        {% endfor %}
        </ul>
    """, posts=posts)


@app.route("/add", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        posts.append({"title": title, "content": content})
        return redirect(url_for("home"))

    return render_template_string("""
        <h2>Add Post</h2>
        <form method="post">
            Title: <input name="title"><br>
            Content:<br><textarea name="content"></textarea><br>
            <button type="submit">Save</button>
        </form>
        <a href="{{ url_for('home') }}">Back</a>
    """)


if __name__ == "__main__":
    app.run(debug=True)
