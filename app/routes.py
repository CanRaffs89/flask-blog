import datetime
from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_user, current_user, logout_user, login_required
from app import app, db, bcrypt
from app.forms import NewPostForm, RegisterForm, LoginForm
from app.models import User, Post

@app.route("/")
def home():
    all_posts = Post.query.order_by(Post.date_created).all()
    return render_template("index.html", posts=all_posts)

@app.route("/add", methods=["GET", "POST"])
@login_required
def add_post():
    form = NewPostForm()
    if form.validate_on_submit():
        new_post = Post(
            title=form.title.data,
            subtitle=form.subtitle.data,
            content=form.content.data,
            author=current_user,
            date_created=datetime.date.today().strftime("%b %d, %Y"),
            image=form.image.data
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=form, title="Add New Post")

@app.route("/post/<int:post_id>")
def get_post(post_id):
    selected_post = Post.query.get_or_404(post_id)
    return render_template("post.html", post=selected_post)

@app.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = NewPostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.content = form.content.data
        post.image = form.image.data
        db.session.commit()
        flash("Your post has been edited successfully!")
        return redirect(url_for("get_post", post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.subtitle.data = post.subtitle
        form.content.data = post.content
        form.image.data = post.image
    return render_template("add.html", form=form, title="Edit Post")

@app.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been successfully deleted!")
    return redirect(url_for("home"))

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
@login_required
def dashboard():
    user_posts = current_user.posts
    return render_template("dashboard.html", posts=user_posts)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))