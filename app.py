from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página about.html
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
