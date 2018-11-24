# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, render_template, request, session
import json
import os
import random

app = Flask(__name__)


todo_db = {  # todo  map, id:text
    1429: "Buy milk",
    3821: "Walk my dog",
    2952: "Do some exercise",
    3019: "Destroy the One ring",
}

@app.after_request
def apply_caching(response):
    response.headers["Content-Type"] = "application/json"
    return response

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return json.dumps({"error": "requested resource does not exist on server"}), 404

#######################################################################################


@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_specific_todo(todo_id):
    """Return information on a specific ToDo item.

    .. :quickref: Get specific ToDo; Gets the information about a specific ToDo.

    **Example request:**

    .. sourcecode:: http

        GET /todos/4278 HTTP/1.1
        Host: http://tupini07.pythonanywhere.com
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

    if todo_id in todo_db.keys(): # if we have the todo with the specified ID in our database then return it
        return json.dumps({"id": todo_id, "text": todo_db[todo_id]}), 200

    else: # if the specified todo was not found then return not found error
        return json.dumps({"error": "ToDo not found."}), 404


@app.route('/todos', methods=['GET'])
def get_todos():
    """Return all todos.

    .. :quickref: ToDo collection; Get all ToDos.

    **Example request**:

    .. sourcecode:: http

        GET /todos HTTP/1.1
        Host: http://tupini07.pythonanywhere.com
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

    sortdir = request.args.get("sort", "asc") # Check if a `sort` get parameter was specified, if yes then use it, else use `asc`

    if sortdir not in ["desc", "asc"]: # check that specified `sort` parameter is in the accepted set, if not return error
        return json.dumps({"error": "Sort parameter is invalid, must be either `asc` or `desc`"}), 400

    # sort todos
    ids = sorted(todo_db.keys(), reverse=(sortdir == "desc"))
    return_code = 200 if len(todo_db.keys()) > 0 else 204

    # return list of sorted todos
    return json.dumps(list({"id": id, "text": todo_db[id]} for id in ids)), return_code


@app.route('/todos', methods=['POST'])
def create_todo():
    """Create a new ToDo.

    .. :quickref: Create ToDo; Creates a new ToDo Item.

    **Example request**:

    .. sourcecode:: http

        POST /todos HTTP/1.1
        Host: http://tupini07.pythonanywhere.com
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
            
        todo_db[new_id] = request.form.get("text") # create todo in DB with specified text
        return json.dumps({"id": new_id}), 201 # return new id:todo, successfully created


@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_specific_todo(todo_id):
    """This endpoing has been documented for other developers, so here you need to convert this documentation
    into an a "formal" API doc (follow same format used in the previous endpoints.
    [in other words: you need to transform this into the sphinx format and add request/response examples]

    This endpoint is used to modify existing ToDos. It recieves as a URL parameter the "todo_id" which is the 
    id of the todo we want to modify, and expects to find a `text` parameter in the request body. 

    It returns error (404) if there is no ToDo corresponding with the specified ID
    or error (400) if no `text` was provided in the request parameters
    or success (202) if the todo is modified correctly
    """

    if todo_id not in todo_db.keys(): # If the specified ID doesn't exist
        return json.dumps({"error": "ToDo not found."}), 404
        
    elif "text" not in request.form.keys(): # if "text" was not passed in the body request
        return json.dumps({"error": "No text was provided to update the TodDo!"}), 400 

    else:

        todo_db[todo_id] = request.form.get("text") # modify the todo with ID

        return json.dumps({"id": todo_id, "text": todo_db[todo_id]}), 202 # return modified todo, success



@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_specific_todo(todo_id):
    # Todo: for this endpoint you'll have to create the `docstring` (method documentation) from scratch
    # You can take the documentation of the previous methods as reference. The documentation for this method
    # should be very similar to the "get_specific_todo" doc. 

    #? What does this endpoint do? 
    #?
    #? this endpoint is used to delete a single todo, it expects the `todo_id` of the todo to delete
    #? as a URL parameter. 
    #?
    #? It can return:
    #?      error (404) - when todo with specified ID does not exist
    #?      success (202) - when the todo is found and deleted

    if todo_id not in todo_db.keys(): # id specified ID not in the DB
        return json.dumps({"error": "ToDo not found."}), 404
        
    else:
        todo_db.pop(todo_id) # delete specific todo
        all_todos = get_todos() # get all todos after deleting 

        return all_todos, 202


@app.route("/todos", methods=["DELETE"])
def delete_all_todos():
    # Todo: also for this one you'll have to create the docstring manually

    #? What does this endpoint do? 
    #?
    #? this endpoint is used to delete all todos
    #?
    #? It can return:
    #?      success (202) - when the todo DB is cleared
    #? 
    #? Note, this is not a very safe method so you might want to add an alert box
    #? telling the user to be careful (see the `docs/source/directives_example.rst` for 
    #? an exmaple of this directive)

    # just clear todo DB
    todo_db.clear()
    return "[]", 202



# ======== Main ============================================================== #
if __name__ == "__main__":

    os.environ["FLASK_ENV"] = "development"
    
    app.secret_key = os.urandom(12)  # Generic key for dev purposes only
    app.run(debug=True, use_reloader=True)
