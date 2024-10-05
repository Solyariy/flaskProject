import json


def get_data():
    data = []
    try:
        with open('datafile.txt', 'r') as file:
            for line in file:
                data.insert(0, json.loads(line))
            file.close()
            print(data)
            return data
    except FileNotFoundError:
        with open('datafile.txt', 'w'):
            return []


def push_data(info):
    with open('datafile.txt', 'a') as file:
        json.dump(info, file)
        file.write('\n')
        file.close()

def update_with_new(info):
    clear_data()
    with open('datafile.txt', 'w') as file:
        print(info, 'update_with_new')
        for line in info:
            json.dump(line, file)
            file.write('\n')

        file.close()

def clear_data():
    with open('datafile.txt', 'w') as file:
        file.truncate(0)
        file.close()


def find_user(username: str, data: list[dict]):
    print(data)
    for person in data:
        if person['username'] == username:
            return person
    return False
