# dashboard
CICD Dashboard

## Create venv in the current working directory

```
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

## Useful links

* <https://pythonhow.com/python-tutorial/flask/How-a-Flask-app-works/>
* <https://flask.palletsprojects.com/en/2.2.x/quickstart/#accessing-request-data>
* <https://www.geeksforgeeks.org/python-flask-request-object/>
* <https://hackersandslackers.com/flask-sqlalchemy-database-models/>

## JWT

* <https://www.geeksforgeeks.org/json-web-token-jwt/>
* <https://www.geeksforgeeks.org/using-jwt-for-user-authentication-in-flask/>