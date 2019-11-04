from flask import Flask, render_template, jsonify, request, Response
import json
from settings import *
# app = Flask(__name__)

books = [
    {
        'name': 'aaaa',
        'price': 2222,
        'ISBN': 23234
    },
    {
        'name': 'dddddd',
        'price': 2232,
        'ISBN': 3453353
    }
]

DEFAULT_PAGE_LIMIT = 3


@app.route("/books/page/<int:page_number>")
def get_paginated_books(page_number):
    print(type(request.args.get("limit")))
    LIMIT = request.args.get("limit", DEFAULT_PAGE_LIMIT, int)
    startIndex = page_number * LIMIT - LIMIT
    endIndex = page_number * LIMIT
    print(startIndex)
    print(endIndex)
    return jsonify({"books": books[startIndex, endIndex]})


@app.route("/books")
def get_book():
    return jsonify({"books": books})


def vailBookObject(BookObject):
    if "name" in BookObject and "price" in BookObject and "ISBN" in BookObject:
        return True
    else:
        return False


@app.route("/books", methods=["post"])
def add_book():
    # return jsonify(request.get_json())
    request_data = request.get_json()
    if vailBookObject(request_data):
        new_book = {
            "name": request_data['name'],
            "price": request_data['price'],
            "ISBN": request_data['ISBN']
        }
        books.insert(0, new_book)
        response = Response("", "201", mimetype="application/json")
        response.headers["Location"] = "/books/" + str(new_book["ISBN"])
        # return "True"
        return response
    else:
        invalidBookObjectErrorMsg = {
            "error": "Invalid book passed in request ",
            "helpString": "The data should same ['name','price','isbn']"
        }
        response = Response(json.dumps(invalidBookObjectErrorMsg), status=400, mimetype="application/json")
        return response
        # return "False"


@app.route("/books/<int:isbn>")
def get_isbn(isbn):
    return_value = {}
    for book in books:
        if book["ISBN"] == isbn:
            return_value = {
                "name": book["name"],
                "price": book["price"]
            }
    return jsonify(return_value)


# Put
@app.route('/books/<int:isbn>', methods=["PUT"])
def replace_book(isbn):
    # return jsonify(request.get_json())
    request_data = request.get_json()
    if not vailBookObject(request_data):
        InvalidBookObjectErrorMSG = {
            "Error": "Valid Book Object must pass to in the request",
            "helpString": "The data should same ['name','price','isbn']"
        }
        response = Response(json.dumps(InvalidBookObjectErrorMSG), status=400, mimetype="application/json")
        return response
    new_book = {
        "name": request_data["name"],
        "price": request_data["price"],
        "ISBN": isbn
    }
    i = 0
    for book in books:
        CurrentIsbn = book["ISBN"]
        if CurrentIsbn == isbn:
            books[i] = new_book
        i += 1
    response = Response("", status=204)
    return response


@app.route("/books/<int:isbn>", methods=["PATCH"])
def update_book(isbn):
    request_data = request.get_json()
    updated_book = {}
    if "name" in request_data:
        updated_book["name"] = request_data["name"]
        if "price" in request_data:
            updated_book["price"] = request_data["price"]
    for book in books:
        if book["isbn"] == isbn:
            book.update(updated_book)
    response = Response("", status=204)
    response.headers["location"] = "/book/" + str(isbn)
    return response


@app.route("/books/<int:isbn>", methods=["DELETE"])
def delete_book(isbn):
    i = 0
    for book in books:
        if book["isbn"] == isbn:
            books.pop(i)
            response = Response("", status=204)
            return response
        i += 1
    invalidBookObjectErrorMSG = {
        "error":"isbn not fund"
    }
    response = Response(json.dumps(invalidBookObjectErrorMSG), status=404 , mimetype="application/json")
    return response
    return ""


if __name__ == "__main__":
    app.run(debug=True, port=5005)
