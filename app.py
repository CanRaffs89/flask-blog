from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = '40014fa522110b5a21b52cca'

class NewPostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    date = StringField("Today's Date", validators=[DataRequired()])
    image = StringField("Image URL", validators=[DataRequired()])
    image_text = StringField("Image Description", validators=[DataRequired()])
    submit = SubmitField("Submit")


posts = [
    {
        "id": 1,
        "title": "10 Things To Do In Toronto",
        "author": "Jane Doe",
        "subtitle": "Laborum ullam quo quo quia nesciunt ut fuga illum. Ullam nihil nulla id consequatur minus autem beatae expedita. Rerum sed error id quas at quos est.",
        "content": "\nQui quos quasi ad consectetur facere.\nAd veniam aut quisquam. Molestias et deserunt ex inventore molestiae ab delectus. Hic accusamus voluptatem unde soluta tenetur non quaerat. Labore officiis minima explicabo consectetur quo repellendus voluptates fuga. Dicta excepturi totam optio ea vero eligendi molestias. Unde ut dolorum praesentium similique consequatur tenetur dolorem amet.\nQui eum vitae assumenda consequatur aut nesciunt. Hic beatae et totam. Et quibusdam qui consequatur sint aut accusantium quis.\nQui sed aut assumenda et dolore nihil quia. Nemo ipsam rerum ad id autem voluptatem quidem in.",
        "date_created": "Jan 1, 2021",
        "image": "../static/img/toronto.jpg",
        "image_alt_text": "Toronto City Hall with illuminated sign"
    },
    {
        "id": 2,
        "title": "5 Winter Kayaking Hotspots",
        "author": "John Smith",
        "subtitle": "Eveniet placeat animi quo tenetur possimus. Aut ea dignissimos quas sed sint saepe tempora et. Molestiae repellat quis nihil accusantium.",
        "content": "\nQui quos quasi ad consectetur facere.\nAd veniam aut quisquam. Molestias et deserunt ex inventore molestiae ab delectus. Hic accusamus voluptatem unde soluta tenetur non quaerat. Labore officiis minima explicabo consectetur quo repellendus voluptates fuga. Dicta excepturi totam optio ea vero eligendi molestias. Unde ut dolorum praesentium similique consequatur tenetur dolorem amet.\nQui eum vitae assumenda consequatur aut nesciunt. Hic beatae et totam. Et quibusdam qui consequatur sint aut accusantium quis.\nQui sed aut assumenda et dolore nihil quia. Nemo ipsam rerum ad id autem voluptatem quidem in.",
        "date_created": "Nov 6, 2020",
        "image": "../static/img/lake.jpg",
        "image_alt_text": "Two red canoes on a lake with snowy mountains and pine forests in the background"
    },
    {
        "id": 3,
        "title": "Montreal's Best Hidden Bars",
        "author": "John Smith",
        "subtitle": "Ad veniam aut quisquam. Molestias et deserunt ex inventore molestiae ab delectus. Hic accusamus voluptatem unde soluta tenetur non quaerat. Labore officiis minima explicabo consectetur quo repellendus voluptates fuga.",
        "content": "\nQui quos quasi ad consectetur facere.\nAd veniam aut quisquam. Molestias et deserunt ex inventore molestiae ab delectus. Hic accusamus voluptatem unde soluta tenetur non quaerat. Labore officiis minima explicabo consectetur quo repellendus voluptates fuga. Dicta excepturi totam optio ea vero eligendi molestias. Unde ut dolorum praesentium similique consequatur tenetur dolorem amet.\nQui eum vitae assumenda consequatur aut nesciunt. Hic beatae et totam. Et quibusdam qui consequatur sint aut accusantium quis.\nQui sed aut assumenda et dolore nihil quia. Nemo ipsam rerum ad id autem voluptatem quidem in.",
        "date_created": "Dec 15, 2020",
        "image": "../static/img/montreal.jpg",
        "image_alt_text": "Montreal skyline at sunset"
    }
]

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def get_post(post_id):
    selected_post = posts[post_id - 1]
    return render_template("post.html", post=selected_post)

@app.route("/add", methods=["GET", "POST"])
def add_post():
    form = NewPostForm()
    if form.validate_on_submit():
        new_post = {
            "id": (len(posts) + 1),
            "title": form.title.data,
            "author": form.author.data,
            "subtitle": form.subtitle.data,
            "content": form.content.data,
            "date_created": form.date.data,
            "image": form.image.data,
            "image_alt_text": form.image_text.data
        }

        posts.append(new_post)
        return redirect(url_for("home"))
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

# DO TODAY
# Start working on login functionality

