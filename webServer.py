from app import app
import os

import logging
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)


# Init after installation
# >> pip install Flask-Login
# >> pip install flask_bootstrap
# >> pip install bootstrap-flask
# >> pip install flask_wtf

# Eir....
# vi ~/.bash_profile

# Run
# >> flask run --cert=adhoc