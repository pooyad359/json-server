import json


def create_empty_file(filepath):
    with open(filepath, "w") as fp:
        json.dump({}, fp)


def read_json(filepath):
    with open(filepath, "r") as fp:
        return json.load(fp)


def write_json(content, filepath):
    with open(filepath, "w") as fp:
        return json.dump(content, fp, indent=2)