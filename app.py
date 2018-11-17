# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, render_template, request, session
import json
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

#######################################################################################


@app.route("/todo/<int:todo_id>", methods=["GET"])
def get_specific_todo(todo_id):
    """Return information on a specific ToDo item.

    .. :quickref: Get specific ToDo; Gets the information about a specific ToDo.

    **Example request:**

    .. sourcecode:: http

        GET /todo/4278 HTTP/1.1
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
    :status 400: If `sort` parameter is not valid
    """

    sortdir = request.args.get("sort", "asc")

    if sortdir not in ["desc", "asc"]:
        return json.dumps({"error": "Sort parameter is invalid, must be either `asc` or `desc`"}), 400

    ids = sorted(todo_db.keys(), reverse=(sortdir == "desc"))

    return json.dumps(list({"id": id, "text": todo_db[id]} for id in ids))


@app.route('/todo', methods=['POST'])
def create_todo():
    """Create a new ToDo.

    .. :quickref: Create ToDo; Creates a new ToDo Item.

    **Example request**:

    .. sourcecode:: http

        POST /todos HTTP/1.1
        Host: example.com
        Accept: application/json

        {
            "text": "Study for Complexity"
        }

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 201 OK
        Vary: Accept
        Content-Type: application/json

        {
            "id": 4393
        }

    :query text: (mandatory) - The text we want to add to our new ToDo
    :status 201: New ToDo has been created successfully. 
    :status 400: No `text` parameter was passed
    """
    if "text" not in request.form.keys(): # when no "text" was passed in the body request
        return json.dumps({"error": "No text provided for the new todo!"}), 400
    
    else: 
        new_id = random.randint(1000, 9999) # note: naivley create random ID
        while new_id in todo_db.keys(): # very unlikely, but this ensures that there are no duplicate ids
            new_id = random.randint(1000, 9999) 
            
        todo_db[new_id] = request.form.get("text") # create todo in DB with specified tet
        return json.dumps({"id": new_id}), 201 # return new id:todo, successfully created


@app.route("/todo/<int:todo_id>", methods=["PUT"])
def update_specific_todo(todo_id):

    if todo_id not in todo_db.keys(): # If the specified ID doesn't exist
        return json.dumps({"error": "ToDo not found."}), 404
        
    elif "text" not in request.form.keys(): # if "text" was not passed in the body request
        return json.dumps({"error": "No text was provided to update the TodDo!"}), 400 

    else:

        todo_db[todo_id] = request.form.get("text") # modify the todo with ID
        specific_todo = get_specific_todo(todo_id)[0] # get specific ToDo with ID 
        return specific_todo, 202 # return modified todo, success



@app.route("/todo/<int:todo_id>", methods=["DELETE"])
def delete_specific_todo(todo_id):

    if todo_id not in todo_db.keys(): # id specified ID not in the DB
        return json.dumps({"error": "ToDo not found."}), 404
        
    else:
        todo_db.pop(todo_id) # delete specific todo
        all_todos = get_todos() # get all todos after deleting 

        return all_todos, 202


@app.route("/todos", methods=["DELETE"])
def delete_all_todos():

    # just clear todo DB
    todo_db.clear()
    return "[]", 202



# ======== Main ============================================================== #
if __name__ == "__main__":

    os.environ["FLASK_ENV"] = "development"
    
    app.secret_key = os.urandom(12)  # Generic key for dev purposes only
    app.run(debug=True, use_reloader=True)
