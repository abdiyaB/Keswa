from flask import Flask, render_template ,request
from postdata import posts
from flask_mail import Mail,Message
from config import mail_username, mail_password
from waitress import serve
from concurrent.futures import thread

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password


mail = Mail(app)


@app.route('/')
def home():
   return render_template('index.html')

@app.route("/money")
def money():
    return render_template('money.html')

@app.route("/clothes")
def clothes():
    return render_template('clothes.html')

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('first-name')
        lastName = request.form.get('last-name')
        email = request.form.get('email')
        message = request.form.get('message')

        msg = Message(subject=f"Mail from {name}", body = f"Name: {name} {lastName}\nE-Mail: {email}\n\n\n{message}", sender=mail_username, recipients=['keswa.421@gmail.com'])
        mail.send(msg)
        return render_template('contact.html', success=True)

    return render_template('contact.html')

@app.route("/index" , methods = ['GET','POST'])
def contactUs():
    if request.method == 'POST' : 
        name = request.form.get('volunteer-name')
        email = request.form.get('volunteer-email')
        number = request.form.get('volunteer-subject')
        file = request.form.get('inputGroupFile02')
        message = request.form.get('volunteer-message')
        msg = Message(subject=f"Mail from {name}", body = f"Name: {name}\nEmail: {email}\nPhone number: {number}\n\n\nMessage: {message}\nattachement: {file}", sender=mail_username, recipients=['keswa.421@gmail.com'])
        mail.send(msg)
        return "sent email"
    return render_template('index.html')



@app.route("/mobile")
def mobile():
    return render_template('mobile.html')

@app.route("/reqres-data")
def reqresData():
    return render_template('reqres-data.html')

@app.route("/posts")
def post():
    return render_template('post-all.html', title='all posts', posts=posts)

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    if post_id < len(posts):
       p = posts[post_id]
       return render_template('post-single.html',
       title= f"Post#{post_id}", p = p )
    else:
        return render_template('404.html'), 404

#debug tool


if __name__ == '__main__':
	serve(app, host='0.0.0.0', port=50100, threads=2, url_prefix="/my-app")
