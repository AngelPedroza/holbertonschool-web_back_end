#!/usr/bin/env python3
"""My flask app
"""
from flask import (Flask, render_template,
                   request, g)
from flask_babel import Babel


class Config(object):
    """The config class"""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict or None:
    """Get the user
    """
    user_id: str or None = request.args.get('login_as')
    user_id: int or None = user_id if user_id is None else int(user_id)
    if user_id is None or user_id not in list(users.keys()):
        return None

    return users.get(user_id)


@app.route('/', methods=['GET'], strict_slashes=False)
def main():
    """Main function to test i18n
    """
    return render_template('6-index.html', user=g.get('user'))


@babel.localeselector
def get_locale():
    """Get locale
    """
    user: dict = get_user()
    if user:
        locale: str or None = user.get('locale')
        if locale is not None and locale in app.config['LANGUAGES']:
            return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """Execution before to call the endpoint
    """
    user: dict = get_user()
    if user is not None:
        g.user: dict = user


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
