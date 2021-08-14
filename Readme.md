# JSON-SERVER
An easy-to-use application to create a database api. The data will be saved in json files.

# Installation
The main dependencies of this library are `fastapi` and `uvicorn`. Simply `pip install` the requirements file:

`$ pip install -r requirements.txt`

# Run Server
To run the api server simply run the following command:

`$ uvicorn server:app --reload`


```python
import requests
```

# Documentation
You can use auto-generated documentation by opening 'http://127.0.0.1:8000/docs' in the browser to see how the API can be used.

# POST

## POST `/root/schema`
Without payload (data) to create an empty schema


```python

resp = requests.post(
    'http://127.0.0.1:8000/test',
)
print(resp.content.decode())
```

    {"state":"Successful","content":{}}
    

With payload (data) to add data to database. It will create the schema if it doesn't exist.


```python
data = json.dumps({'Name': 'Bob', 'Age':23})
resp = requests.post(
    'http://127.0.0.1:8000/team',
    data=data,
)
print(resp.content.decode())
```

    {"state":"Successful","content":{}}
    


```python
data = json.dumps({'Name': 'Alice', 'Age':28})
resp = requests.post(
    'http://127.0.0.1:8000/team',
    data=data,
)
print(resp.content.decode())
```

    {"state":"Successful","content":{}}
    

# GET

## GET `/root`
Get a list of available schemas.


```python
resp = requests.get('http://127.0.0.1:8000/')
content = json.loads(resp.content.decode())
print(content)
```

    {'state': 'Successful', 'content': {'schemas': ['team', 'test']}}
    

## GET `/root/schema`
Get all the data in a schema


```python
resp = requests.get('http://127.0.0.1:8000/team')
content = json.loads(resp.content.decode())
print(content)
```

    {'state': 'Successful', 'content': {'1f15ed87835e467e9539c5cf1fa5a0f5': {'data': {'Name': 'Bob', 'Age': 23}, 'inserted': '2021-08-14T01:08:00.948487', 'last_updated': '2021-08-14T01:08:00.948487'}, '6fb389b8d39747a5b05de4d3c06a5710': {'data': {'Name': 'Alice', 'Age': 28}, 'inserted': '2021-08-14T01:08:01.844790', 'last_updated': '2021-08-14T01:08:01.844790'}}}
    

## GET `/root/schema/id`
Get data from a schema using ID


```python
resp = requests.get('http://127.0.0.1:8000/team/1f15ed87835e467e9539c5cf1fa5a0f5')
print(resp.content.decode())
```

    {"state":"Successful","content":{"data":{"Name":"Bob","Age":23},"inserted":"2021-08-14T01:08:00.948487","last_updated":"2021-08-14T01:08:00.948487"}}
    

# PUT
To update data


```python
data = json.dumps({'Name': 'Bob', 'Age':25})
resp = requests.put(
    f'http://127.0.0.1:8000/team/1f15ed87835e467e9539c5cf1fa5a0f5',
    data=data,
)
print(resp.content.decode())
```

    {"state":"Successful","content":{}}
    


```python
resp = requests.get('http://127.0.0.1:8000/team/1f15ed87835e467e9539c5cf1fa5a0f5')
print(resp.content.decode())
```

    {"state":"Successful","content":{"data":{"Name":"Bob","Age":25},"inserted":"2021-08-14T01:08:00.948487","last_updated":"2021-08-14T01:08:41.791998"}}
    

# DELETE

## DELETE `/root/schema`
Delete a schema from database


```python
resp = requests.delete(f'http://127.0.0.1:8000/test')

print(resp.content.decode())
```

    {"state":"Successful","content":{}}
    

## DELETE `/root/schema/id`
Delete data from schema using ID


```python
resp = requests.delete(f'http://127.0.0.1:8000/team/1f15ed87835e467e9539c5cf1fa5a0f5')

print(resp.content.decode())
```

    {"state":"Successful","content":{}}
    


```python
resp = requests.get('http://127.0.0.1:8000/team')
content = json.loads(resp.content.decode())
print(content)
```

    {'state': 'Successful', 'content': {'6fb389b8d39747a5b05de4d3c06a5710': {'data': {'Name': 'Alice', 'Age': 28}, 'inserted': '2021-08-14T01:08:01.844790', 'last_updated': '2021-08-14T01:08:01.844790'}}}
    
