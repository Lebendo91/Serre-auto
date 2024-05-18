from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///serre.db'
db = SQLAlchemy(app)

class Serre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    light = db.Column(db.Float, nullable=False)

@app.route('/')
def index():
    data = Serre.query.all()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    temperature = request.form['temperature']
    humidity = request.form['humidity']
    light = request.form['light']
    
    new_entry = Serre(temperature=temperature, humidity=humidity, light=light)
    db.session.add(new_entry)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
