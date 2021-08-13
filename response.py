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