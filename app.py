from flask import Flask
from website.site.routes import site
from website.api.routes import api

app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)
