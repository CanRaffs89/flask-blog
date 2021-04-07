import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import NewPostForm, RegisterForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '40014fa522110b5a21b52cca'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    subtitle = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    date_created = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    image_alt_text = db.Column(db.String, nullable=False)

today = datetime.date.today().strftime("%b %d, %Y")

@app.route("/")
def home():
    all_posts = Post.query.order_by(Post.date_created).all()
    return render_template("index.html", posts=all_posts)

@app.route("/post/<int:post_id>")
def get_post(post_id):
    selected_post = Post.query.get(post_id)
    return render_template("post.html", post=selected_post)

@app.route("/add", methods=["GET", "POST"])
def add_post():
    form = NewPostForm()
    if form.validate_on_submit() and request.method == "POST":
        new_post = Post(
            title=request.form["title"],
            author=request.form["author"],
            subtitle=request.form["subtitle"],
            content=request.form["content"],
            date_created=today,
            image=request.form["image"],
            image_alt_text=request.form["image_text"]
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=form)

@app.route("/login")
def login():
    form = RegisterForm()
    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
