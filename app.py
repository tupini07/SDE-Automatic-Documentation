# -*- coding: utf-8 -*-

from scripts import tabledef
from scripts import forms
from scripts import helpers
from flask import Flask, redirect, url_for, render_template, request, session
import json
import sys
import os


app = Flask(__name__)


# ======== Routing =========================================================== #
# -------- Login ------------------------------------------------------------- #
@app.route('/posts', methods=['GET'])
def get_posts():
    """Return collection of posts.

    .. :quickref: Posts Collection; Get collection of posts.

    **Example request**:

    .. sourcecode:: http

        GET /posts/ HTTP/1.1
        Host: example.com
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Vary: Accept
        Content-Type: application/json

        [
        {
            "post_id": 12345,
            "author": "/author/123/",
            "tags": ["sphinx", "rst", "flask"],
            "title": "Documenting API in Sphinx with httpdomain",
            "body": "How to..."
        },
        {
            "post_id": 12346,
            "author": "/author/123/",
            "tags": ["python3", "typehints", "annotations"],
            "title": "To typehint or not to typehint that is the question",
            "body": "Static checking in python..."
        }
        ]

    :query sort: sorting order e.g. sort=author,-pub_date
    :query q: full text search query
    :resheader Content-Type: application/json
    :status 200: posts found
    """
    if not session.get('logged_in'):
        form = forms.LoginForm(request.form)
        if request.method == 'POST':
            username = request.form['username'].lower()
            password = request.form['password']
            if form.validate():
                if helpers.credentials_valid(username, password):
                    session['logged_in'] = True
                    session['username'] = username
                    return json.dumps({'status': 'Login successful'})
                return json.dumps({'status': 'Invalid user/pass'})
            return json.dumps({'status': 'Both fields required'})
        return render_template('login.html', form=form)
    user = helpers.get_user()
    return render_template('home.html', user=user)



# ======== Main ============================================================== #
if __name__ == "__main__":
    app.secret_key = os.urandom(12)  # Generic key for dev purposes only
    app.run(debug=True, use_reloader=True)
