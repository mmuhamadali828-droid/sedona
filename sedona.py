from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('sedona.html')

if __name__ == 'main':
    app.run()