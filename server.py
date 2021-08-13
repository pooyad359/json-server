from fastapi import FastAPI, Request
import os
from pathlib import Path
import json
import uuid
from datetime import datetime


app = FastAPI()
# os.makedirs("./schemas", exist_ok=True)
path = Path("./schemas")
path.mkdir(exist_ok=True)

##################### GET ######################
@app.get("/")
async def get_schema_list():
    """Get a list of all available schemas"""
    return {"message": "You have received this message."}


@app.get("/{schema}")
async def get_schema(schema: str):
    """Retrieve all the data from a schema"""
    try:
        filepath = path / f"{schema}.json"
        if not filepath.exists():
            return create_fail_response("File doesn't exist")
        data = read_json(filepath)
        return create_success_response(data)
    except Exception as e:
        create_fail_response(str(e))


@app.get("/{schema}/{id}")
async def get_data_by_id(schema: str, id: str):
    """Retrieve data by ID from a schema"""
    try:
        filepath = path / f"{schema}.json"
        data = read_json(filepath)

        return create_success_response(data.get(id, {}))

    except FileNotFoundError:
        return create_fail_response("Schema does not exist")

    except KeyError:
        return create_fail_response("ID does not exist")

    except Exception as e:
        return create_fail_response(str(e))


##################### POST ######################
@app.post("/{schema}")
async def add_data(schema: str, request: Request):
    """Add data to the schema"""
    try:
        content = await request.body()
        file = path / f"{schema}.json"
        if not file.exists():
            create_empty_file(file)
            if not content:
                return create_success_response({})
        elif not content:
            return create_fail_response("Schema Exists")

        content_dict = json.loads(content)

        data = read_json(file)
        data.update(create_new_entry(content_dict))
        write_json(data, file)
        return create_success_response({})
    except Exception as e:
        return create_fail_response(str(e))


##################### PUT ######################
@app.put("/{schema}/{id}")
async def update_data_by_id(schema: str, id: str, request: Request):
    """Update data in schema using ID"""
    try:
        filepath = path / f"{schema}.json"
        data = read_json(filepath)
        content = await request.body()
        content_dict = json.loads(content)
        data[id] = update_entry(data, id, content_dict)
        write_json(data, filepath)
    except FileNotFoundError:
        return create_fail_response("Schema does not exist")

    except KeyError:
        return create_fail_response("ID does not exist")

    except Exception as e:
        return create_fail_response(str(e))


##################### DELETE ######################
@app.delete("/{schema}/{id}")
async def delete_data_by_id(schema: str, id: str):
    """Delete data from schema using ID"""
    try:
        filepath = path / f"{schema}.json"
        data = read_json(filepath)
        data.pop(id)
        write_json(data, filepath)

    except FileNotFoundError:
        return create_fail_response("Schema does not exist")

    except KeyError:
        return create_fail_response("ID does not exist")

    except Exception as e:
        return create_fail_response(str(e))


@app.delete("/{schema}")
async def delete_schema(schema: str):
    """Delete schema"""
    try:
        filepath = path / f"{schema}.json"
        if not filepath.exists():
            return create_fail_response("Schema does not exist")
        os.remove(filepath)
    except Exception as e:
        return create_fail_response(str(e))


def create_empty_file(filepath):
    with open(filepath, "w") as fp:
        json.dump({}, fp)


def read_json(filepath):
    with open(filepath, "r") as fp:
        return json.load(fp)


def write_json(content, filepath):
    with open(filepath, "w") as fp:
        return json.dump(content, fp, indent=2)


def create_new_entry(content_dict):
    timestamp = new_timestamp()
    id = uuid.uuid4().hex
    entry = {
        id: {
            "data": content_dict,
            "inserted": timestamp,
            "last_updated": timestamp,
        },
    }
    return entry


def update_entry(data, id, new_content):
    output = data[id]
    output["data"] = new_content
    output["last_updated"] = new_timestamp()
    return output


def create_fail_response(message):
    return {
        "state": "Unsuccessful",
        "message": message,
        "content": {},
    }


def create_success_response(content):
    return {
        "state": "Successful",
        "content": content,
    }


def new_timestamp():
    return datetime.now().isoformat()