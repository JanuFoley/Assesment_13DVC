from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Home_Page():
    return render_template('index.html')

@app.route('/Accessability')
def Accessability_page():
    return render_template('Accessability.html')

@app.route('/Location')
def Location_page():
    return render_template('Location.html')

if __name__ == '__main__':
    app.run()
