# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, render_template, request, session
import json
import sys
import os
import random

app = Flask(__name__)


todo_db = {  # todo  map, id:text
    1429: "Buy milk",
    3821: "Walk my dog",
    2952: "Do some exercise"
}


@app.after_request
def apply_caching(response):
    response.headers["Content-Type"] = "application/json"
    return response


@app.route("/todo/<int:todo_id>", methods=["GET"])
def get_specific_todo(todo_id):
    """Return information on a specific ToDo item.

    .. :quickref: Get specific ToDo; Gets the information about a specific ToDo.

    **Example request:**

    .. sourcecode:: http

<<<<<<< HEAD
        GET /todo/4278 HTTP/1.1
=======
        GET /post/123123 HTTP/1.1
>>>>>>> 5d8184718ec5e72919f18f6ef479522a271912db
        Host: example.com
        Accept: application/json


    **Example response:**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Vary: Accept
        Content-Type: application/json

        {
            "id": 4278,
            "text": "Work on SDE project"
        }

    :query post_id: The id of the todo we want to get specific information about
    :status 200: todo found
    :status 404: todo with given id not found
    """

    if todo_id in todo_db.keys():
        return json.dumps({"id": todo_id, "text": todo_db[todo_id]}), 200

    else:
        return json.dumps({"error": "ToDo not found."}), 404


@app.route('/todos', methods=['GET'])
def get_todos():
    """Return all todos.

    .. :quickref: ToDo collection; Get all ToDos.

    **Example request**:

    .. sourcecode:: http

        GET /todos HTTP/1.1
        Host: example.com
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Vary: Accept
        Content-Type: application/json

        [
            {
                "id": 2231,
                "text": "Take a shower",
            },
            {
                "id": 2243,
                "text": "Bake some cookies",
            },
        ]

    :query sort: direction of sort, either `asc` or `desc`. Elements are sorted by `id`. Default is `asc`
    :status 200: posts found
    :status 204: Returned when there are no todos 
    :status 400: If sort parameter is not valid
    """

    sortdir = request.args.get("sort", "asc")

    if sortdir not in ["desc", "asc"]:
        return json.dumps({"error": "Sort parameter is invalid, must be either `asc` or `desc`"}), 400

    ids = sorted(todo_db.keys(), reverse=(sortdir == "desc"))

    return json.dumps(list({"id": id, "text": todo_db[id]} for id in ids))


@app.route('/todo', methods=['POST'])
def create_todo():

    if "text" not in request.form.keys():
        return json.dumps({"error": "No text provided for the new todo!"}), 400
    
    else:
        new_id = random.randint(1000, 9999) # note: no check for id clashes
        todo_db[new_id] = request.form.get("text")
        return json.dumps({"id": new_id}), 201 # successfully created


@app.route("/todo/<int:todo_id>", methods=["PUT"])
def update_specific_todo(todo_id):

    if todo_id not in todo_db.keys():
        return json.dumps({"error": "ToDo not found."}), 404
        
    elif "text" not in request.form.keys():
        return json.dumps({"error": "No text was provided to update the TodDo!"}), 400

    else:
        todo_db[todo_id] = request.form.get("text")
        return get_specific_todo(todo_id)[0], 202



@app.route("/todo/<int:todo_id>", methods=["DELETE"])
def delete_specific_todo(todo_id):

    if todo_id not in todo_db.keys():
        return json.dumps({"error": "ToDo not found."}), 404
        
    else:
        todo_db.pop(todo_id)
        return get_todos(), 202


@app.route("/todos", methods=["DELETE"])
def delete_all_todos():

    todo_db.clear()
    return "[]", 202




# ======== Main ============================================================== #
if __name__ == "__main__":

    os.environ["FLASK_ENV"] = "development"
    app.secret_key = os.urandom(12)  # Generic key for dev purposes only
    app.run(debug=True, use_reloader=True)
