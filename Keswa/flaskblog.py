from flask import Flask, render_template ,request
from postdata import posts
from flask_mail import Mail,Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

app.config['MAIL_USERNAME'] = 'Keswa@charity.org'
app.config['MAIL_PASSWORD'] = 'keswa@charity'

mail = Mail(app)


@app.route('/')
def home():
   return render_template('index.html')


@app.route("/money")
def money():
    return render_template('money.html')

@app.route("/clothes")
def donate():
    return render_template('donate.html')


@app.route("/index" , methods = ['GET','POST'])
def contactUs():
    if request.method == 'POST' : 
        msg = Message("Hey" , sender='noreply@demo.com', recipients=['g4project.se421@gmail.com'])
        msg.body = " hey how are you"
        mail.send(msg)
        return "sent email"
    return render_template('index.html')

#debug tool
if __name__ == '__main__':
	app.run( debug=True )