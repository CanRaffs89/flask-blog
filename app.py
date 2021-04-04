from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy


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

class NewPostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    date = StringField("Today's Date", validators=[DataRequired()])
    image = StringField("Image URL", validators=[DataRequired()])
    image_text = StringField("Image Description", validators=[DataRequired()])
    submit = SubmitField("Submit")

# db.create_all()

# new_post = Post(title="Montreal's Best Hidden Bars", author="John Smith", subtitle="Ad veniam aut quisquam. Molestias et deserunt ex inventore molestiae ab delectus. Hic accusamus voluptatem unde soluta tenetur non quaerat. Labore officiis minima explicabo consectetur quo repellendus voluptates fuga.", content="Qui quos quasi ad consectetur facere. Ad veniam aut quisquam. Molestias et deserunt ex inventore molestiae ab delectus. Hic accusamus voluptatem unde soluta tenetur non quaerat. Labore officiis minima explicabo consectetur quo repellendus voluptates fuga. Dicta excepturi totam optio ea vero eligendi molestias. Unde ut dolorum praesentium similique consequatur tenetur dolorem amet. Qui eum vitae assumenda consequatur aut nesciunt. Hic beatae et totam. Et quibusdam qui consequatur sint aut accusantium quis. Qui sed aut assumenda et dolore nihil quia. Nemo ipsam rerum ad id autem voluptatem quidem in.", date_created="Dec 15, 2020", image="../static/img/montreal.jpg", image_alt_text="Montreal skyline at sunset")

# db.session.add(new_post)
# db.session.commit()

all_posts = Post.query.all()

@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/post/<int:post_id>")
def get_post(post_id):
    selected_post = all_posts[post_id - 1]
    return render_template("post.html", post=selected_post)

@app.route("/add", methods=["GET", "POST"])
def add_post():
    form = NewPostForm()
    # if form.validate_on_submit():
    #     new_post = {
    #         "id": (len(posts) + 1),
    #         "title": form.title.data,
    #         "author": form.author.data,
    #         "subtitle": form.subtitle.data,
    #         "content": form.content.data,
    #         "date_created": form.date.data,
    #         "image": form.image.data,
    #         "image_alt_text": form.image_text.data
    #     }

    #     posts.append(new_post)
    #     return redirect(url_for("home"))
    return render_template("add.html", form=form)

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)

# DONE WED 31
# Set up Python dev environment
# Installed Flask
# Changed HTML files to Jinja templates
# Set up Flask routes for index, get post, new post and login pages
# Added temporary dictionary of posts for testing purposes
# Index page and page for each post working

# DONE THURS 1
# Added a basic New Post form for testing
# Set up Flask WTForms

# DONE SUN 4
# Added SQLite database to store blog posts

# DO TODAY
# Set up POST route for sending posts to database
# Start working on login functionality

