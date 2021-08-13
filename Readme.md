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

# POST

## POST `/root/schema`
Without payload (data) to create an empty schema


```python

resp = requests.post(
    'http://127.0.0.1:8000/test4',
)
resp.status_code, resp.content.decode()
```




    (200, '{"state":"Unsuccessful","message":"Schema Exists","content":{}}')



With payload (data) to add data to database. It will create the schema if it doesn't exist.


```python
data = json.dumps({'message': 'Hello There!'})
resp = requests.post(
    'http://127.0.0.1:8000/test3',
#     header='application/json',
    data=data,
)
resp.status_code, resp.content.decode()
```




    (200, '{"state":"Successful","content":{}}')



# GET

## GET `/root`

## GET `/root/schema`
Get all the data in a schema


```python
resp = requests.get('http://127.0.0.1:8000/test')
resp.status_code, json.loads(resp.content.decode())
```




    (200,
     {'state': 'Successful',
      'content': {'6b837aa1be094d37b62f8b5addf4e662': {'data': {'message': 'Hello There!'},
        'inserted': '2021-08-13T22:35:01.363723',
        'last_updated': '2021-08-13T22:35:01.363723'},
       'b72682e1772b4f4cbe12fe4b9b6e83ef': {'data': {'message': 'Hello There!'},
        'inserted': '2021-08-13T22:35:11.954140',
        'last_updated': '2021-08-13T22:35:11.954140'}}})



## GET `/root/schema/id`
Get data from a schema using ID


```python
resp = requests.get('http://127.0.0.1:8000/test/6b837aa1be094d37b62f8b5addf4e662')
resp.status_code, resp.content.decode()
```




    (200,
     '{"state":"Successful","content":{"data":{"message":"Hello There!"},"inserted":"2021-08-13T22:35:01.363723","last_updated":"2021-08-13T22:35:01.363723"}}')



# PUT
To update data


```python
resp = requests.get('http://127.0.0.1:8000/test')
content = json.loads(resp.content.decode())
ids = list(content['content'].keys())
print(ids)
```

    ['6b837aa1be094d37b62f8b5addf4e662', 'b72682e1772b4f4cbe12fe4b9b6e83ef', 'a33d90990eef48e489f5fd456bddc206']
    


```python
data = json.dumps({'message': 'Hello Again!'})
resp = requests.put(
    f'http://127.0.0.1:8000/test/{ids[0]}',
    data=data,
)
resp.status_code, resp.content.decode()
```




    (200, 'null')



# DELETE

## DELETE `/root/schema`
Delete a schema from database


```python
resp = requests.delete(f'http://127.0.0.1:8000/test')

resp.status_code, resp.content.decode()
```




    (200, 'null')




```python

```

## DELETE `/root/schema/id`
Delete data from schema using ID


```python
resp = requests.delete(f'http://127.0.0.1:8000/test/{ids[0]}')

resp.status_code, resp.content.decode()
```




    (200, 'null')




```python

```
