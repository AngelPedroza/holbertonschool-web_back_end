#!/usr/bin/env python3
"""My flask app
"""
from flask import (Flask, render_template,
                   request, g)
from flask_babel import Babel
import pytz


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
    user_id: str = request.args.get('login_as')

    if user_id is None or user_id == '':
        user_id = None
    else:
        user_id = int(user_id)

    if user_id is None or user_id not in list(users.keys()):
        return None

    return users.get(user_id)


@app.route('/', methods=['GET'], strict_slashes=False)
def main():
    """Main function to test i18n
    """
    return render_template('7-index.html', user=getattr(g, 'user', None))


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


@babel.timezoneselector
def get_timezone():
    """Get time zone
    """
    user: dict = get_user()
    default_tz: str = app.config['BABEL_DEFAULT_TIMEZONE']
    if user:
        tz: str or None = user.get('timezone')
        print(tz)
        try:
            correct_tz = pytz.timezone(tz)
        except pytz.exceptions.UnknownTimeZoneError:
            return eval('pytz.' + default_tz.lower())

        return correct_tz.zone

    return eval('pytz.' + default_tz.lower())


@app.before_request
def before_request():
    """Execution before to call the endpoint
    """
    user: dict = get_user()
    g.user: dict = user if user is not None else None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
