from flask import Flask, render_template
from json import loads
import urllib.request


def get_user_data():
    url = "https://randomuser.me/api/"
    url_response = urllib.request.urlopen(url)
    data = loads(url_response.read())['results'][0]
    random_user = {
        'name': data['name']['first'],
        'last_name': data['name']['last'],
        'location': data['location']['street'],
        'phone': data['phone'],
        'email': data['email'],
        'picture': data['picture']['large']
    }

    return random_user


app = Flask(__name__)


@app.route('/')
def display_random_user():
    user_details = get_user_data()
    return render_template("index.html", user_data=user_details)


if __name__ == '__main__':
    app.run()
