# iWork-test
## EndPoints for Api
```
api roots are 
  1. http://localhost:8000/items
  2. http://localhost:8000/signup/
  3. http://localhost:8000/login/
For  end point http://localhost:8000/items there are  
      GET http://localhost:8000/items - list all items 
      POST http://localhost:8000/items/ (with body of json file request using name and quantity) - create new item
      PUT http://localhost:8000/items/<:id> (with body of json file request using name and quantity) - update the existing item specified by the id provided
      DELETE http://localhost:8000/items/<:id> delete the item 

For  end point http://localhost:8000/signup/ 
      POST  http://localhost:8000/signup/ (with body of json file request using username and password) create user with provided info and return token for the user

For  end point http://localhost:8000/login/
      POST  http://localhost:8000/login/ (with body of json file request using username and password) return token for the user

```

## Used Tool 
  - [Django](https://www.djangoproject.com/) 
  - [Django Restframework](https://www.django-rest-framework.org/)
  - [dotenv](https://github.com/theskumar/python-dotenv)
  - [psycopg2](https://github.com/psycopg/psycopg2)
### Used Database - PostgreSQL
