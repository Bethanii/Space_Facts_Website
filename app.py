from flask import Flask, render_template, url_for, request
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')


# handle from 
# @app.route('/mercury', methods=['POST'])
# def main():
#   hash = '0eedfc21-3294-4309-9flb-7c259551deb0:975d0bc07112ca2a567928b751d5c00d9411ac9ec1882ae4a04a408'
#   info = requests.get('https://api.astronomyapi.com/api/v2/bodies/0eedfc21-3294-4309-9flb-7c259551deb0:975d0bc07112ca2a567928b751d5c00d9411ac9ec1882ae4a04a408' )
#   if request.method == 'POST':
#       return 'hi'


@app.route('/')
def hello():
    """Renders a sample page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
