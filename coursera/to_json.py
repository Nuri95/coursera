import json


def to_json(func):
    def wrapped():
        data = func()
        json_str = json.dumps(data)
        print(type(json_str))
        return json_str
    return wrapped()

@to_json
def get_data():
    return {
        'data': 43
    }


print(get_data)