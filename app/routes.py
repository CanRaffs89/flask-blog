import datetime
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from app import app, db, bcrypt
from app.forms import NewPostForm, RegisterForm, LoginForm
from app.models import User, Post

@app.route("/")
def home():
    all_posts = Post.query.order_by(Post.date_created).all()
    return render_template("index.html", posts=all_posts)

@app.route("/post/<int:post_id>")
def get_post(post_id):
    selected_post = Post.query.get(post_id)
    return render_template("post.html", post=selected_post)

@app.route("/add", methods=["GET", "POST"])
@login_required
def add_post():
    form = NewPostForm()
    if form.validate_on_submit() and request.method == "POST":
        new_post = Post(
            title=request.form["title"],
            author=request.form["author"],
            subtitle=request.form["subtitle"],
            content=request.form["content"],
            date_created=datetime.date.today().strftime("%b %d, %Y"),
            image=request.form["image"],
            image_alt_text=request.form["image_text"]
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully!")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Login error - please check email and password")
    return render_template("login.html", form=form)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))