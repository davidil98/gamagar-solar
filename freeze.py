from app import app
from flask_frozen import Freezer
import os

app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
    
    cname_path = os.path.join('docs', 'CNAME')
    with open(cname_path, 'w') as f:
        f.write('gamagarsolar.com.mx')