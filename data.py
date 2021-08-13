import uuid
from datetime import datetime


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


def new_timestamp():
    return datetime.now().isoformat()