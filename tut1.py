from flask import Flask, render_template, request , session , redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
import os
from datetime import datetime
from werkzeug import secure_filename
import math

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = params["upload_location"]
app.secret_key = 'super-secret-key'
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD=  params['gmail-password']
)
mail = Mail(app)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)


class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)


class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    add_pic = db.Column(db.String(12), nullable=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    tagline = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(12), nullable=True)


@app.route("/")
def home():
    posts = Posts.query.filter_by().all()
    last = math.ceil (len(posts)/int(params['no_of_posts']))
    #[0:params['no_of_posts']]
    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts= posts[(page-1)*int(params['no_of_posts']): (page-1)*int(params['no_of_posts'])+ int(params['no_of_posts'])]
    if (page==1):
        prev = "#"
        Next = "/?page="+ str(page + 1)
    elif (page==last):
        prev = "/?page=" + str(page - 1)
        Next = "#"
    else:
        prev = "/?page=" + str(page - 1)
        Next = "/?page=" + str(page + 1)
        
        


    return render_template('index.html', params=params, posts=posts,prev = prev, Next = Next)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)

@app.route("/about")
def about():
    return render_template('about.html', params=params)


@app.route("/uploader", methods = ['GET' , 'POST'])
def uploader():
    if ('user' in session and session ['user'] == params['admin_user']):
        if (request.method=='POST'):
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename) ))
            return "uploaded successfully"



@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('dashboard')

@app.route("/delete/<string:sno>", methods=['GET','POST'])  
def delete(sno):
    if ('user' in session and session ['user'] == params['admin_user']):
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()

    return redirect('dashboard')  

@app.route("/dashboard", methods = ['GET' , 'POST'])
def dashboard():

    if ('user' in session and session ['user'] == params['admin_user']):
        posts = Posts.query.all()
        return render_template('dashboard.html' , params = params, posts = posts)



    if request.method == 'POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username == params['admin_user'] and userpass == params['admin_password']):
            #set the session
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html' , params = params , posts = posts)


        # redirect to admin panel    
    return render_template('login.html', params=params,)


@app.route("/edit/<string:sno>", methods = ['GET' , 'POST'])    
def edit(sno):
    if ('user' in session and session ['user'] == params['admin_user']):
        if request.method == 'POST':
            box_title = request.form.get('title')
            tline = request.form.get("tline")
            slug = request.form.get("slug")
            content = request.form.get("content") 
            img_file = request.form.get("img_file")
            add_pic = request.form.get("add_pic")
            date = datetime.now()

            if sno == "0":
                post = Posts(add_pic= add_pic , title = box_title, slug = slug, content = content, tagline = tline, img_file = img_file, date = date)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = box_title
                post.slug = slug
                post.content = content
                post.tagline = tline
                post.img_file = img_file
                post.date = date
                db.session.commit()
                return redirect('/edit/'+ sno)


    post = Posts.query.filter_by(sno=sno).first() 
    return render_template("EDIT.HTML", params = params, post=post)



       


@app.route("/contacts", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contact(name=name, phone_num = phone, msg = message, date= datetime.now(),email = email )
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients = [params['gmail-user']],
                          body = message + "\n" + phone
                          )
    return render_template('contacts.html', params=params)


app.run(debug=True)


