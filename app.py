# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, render_template, request, session
import json
import sys
import os


app = Flask(__name__)


@app.route("/post/<int:post_id>", methods=["GET"])
def get_specific_post(post_id):
    """Return information on a specific post.

    .. :quickref: Get specific post; Gets the information about a specific potst.

    **Example request:**

    .. sourcecode:: http

        GET /post/123123 HTTP/1.1
        Host: example.com
        Accept: application/json
    

    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Vary: Accept
        Content-Type: application/json

        {
            "post_id": 123123,
            "author": "/author/123/",
            "tags": ["python3", "typehints", "annotations"],
            "title": "To typehint or not to typehint that is the question",
            "body": "Static checking in python..."
        }

    :query post_id: The id of the post we want to get specific information of
    :status 200: post found
    :status 404: post with given id not found
    """
    return json.dumps({
        "post_id": post_id,
        "author": "/author/123/",
        "tags": ["python3", "typehints", "annotations"],
        "title": "To typehint or not to typehint that is the question",
        "body": "Static checking in python..."
    })



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
    return json.dumps([
        {
            "post_id": 12346,
            "author": "/author/123/",
            "tags": ["python3", "typehints", "annotations"],
            "title": "To typehint or not to typehint that is the question",
            "body": "Static checking in python..."
        }
    ])


@app.route('/posts', methods=['POST'])
def create_post():
    """Create a post.

    .. :quickref: Create a post; Creates a post with the specified content.

    **Example request**:

    .. sourcecode:: http

        POST /posts/ HTTP/1.1
        Host: example.com
        Accept: application/json

        {
            "content": "Some content for the post",
            "author_id": 39,
            "publishing_date": "30/9/2019"
        }

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Vary: Accept
        Content-Type: application/json

        {
            "post_id": 39203,
        }


    :query content: Textual content
    :query author_id: ID of the author that created the post.
    :query publishing_date: The date we want the post to be published.

    :resheader Content-Type: application/json
    :status 201: post created
    """
    return json.dumps({"post_id": 23213})


# ======== Main ============================================================== #
if __name__ == "__main__":
    app.secret_key = os.urandom(12)  # Generic key for dev purposes only
    app.run(debug=True, use_reloader=True)
