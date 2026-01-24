from app import app
from flask_frozen import Freezer

app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()