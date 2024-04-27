from flask import Flask, render_template ,request
from postdata import posts
from flask_mail import Mail,Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

app.config['MAIL_USERNAME'] = 'g4project.se421@gmail.com'
app.config['MAIL_PASSWORD'] = 'g4project.se421@2020'

mail = Mail(app)




@app.route("/")
def home():
   return render_template('index.html')


@app.route("/money")
def about():
    return render_template('money.html')

@app.route("/clothes")
def about():
    return render_template('clothes.html')


@app.route("/contact" , methods = ['GET','POST'])
def contactUs():
    if request.method == 'POST' : 
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(subject='Contact Form Submission', sender=email, recipients=['your_email@example.com'])
        msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        mail.send(msg)

        return 'Message sent successfully!'
    return render_template('index.html')


@app.route("/posts")
def home():
    return render_template('post-all.html', title='all posts', posts=posts)

@app.route('/posts/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        return render_template('postsingle.html', post=post)
    else:
        return 'Post not found', 404
    


#debug tool
if __name__ == '__main__':
	app.run( debug=True )