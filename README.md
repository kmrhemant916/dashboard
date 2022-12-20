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

* 

## Module and package

* <https://www.scaler.com/topics/module-and-package-in-python/>