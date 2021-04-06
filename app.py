from flask import Flask, render_template, url_for
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def hello():
    """Renders a sample page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
