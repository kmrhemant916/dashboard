# dashboard

## Create venv in the current working directory

```sh
python3.9 -m venv .venv
```

command + shift +p -> type ``` > Python: select interpreter```
restart the terminal

## run the app

``` flask run ```

## run in debug mode

``` flask run --debugger --reload ```

## Run flask app inside docker

``` docker run --name dashboard -p 5000:5000 -v $(pwd):/opt -d dashboard:latest ```

## Flask

* <https://pythonbasics.org/what-is-flask-python/>

## jsonify

* <https://www.educba.com/flask-jsonify/>

## make_response

* <https://www.educative.io/answers/what-is-flaskmakeresponse>

## Useful links

* <https://pythonhow.com/python-tutorial/flask/How-a-Flask-app-works/>
* <https://flask.palletsprojects.com/en/2.2.x/quickstart/#accessing-request-data>
* <https://www.geeksforgeeks.org/python-flask-request-object/>
* <https://hackersandslackers.com/flask-sqlalchemy-database-models/>

## JWT

* <https://www.geeksforgeeks.org/json-web-token-jwt/>
* <https://www.geeksforgeeks.org/using-jwt-for-user-authentication-in-flask/>

## Flask-Smorest

* <https://flask-smorest.readthedocs.io/en/latest/#:~:text=flask%2Dsmorest%20(formerly%20known%20as,to%20serialize%20and%20deserialize%20data.>

## marshmallow

* <https://marshmallow.readthedocs.io/en/stable/>

## Module and package

* <https://www.scaler.com/topics/module-and-package-in-python/>

## MethodView

* <https://flask.palletsprojects.com/en/2.1.x/views/>

## What is an ORM

* <https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools/>

## Context

* <https://overiq.com/flask-101/contexts-in-flask/>
* <https://www.askpython.com/python-modules/flask/flask-application-request-context>
* Flask pushes(or activates) the Application Context automatically when a particular request comes in and removes it once the request is handled.
