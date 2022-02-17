import json


def dec_dec_log(file_name):
    def decorated_log(func):
        def wrapper(*args, **kwargs):
            data_1 = func(*args, **kwargs)
            with open(file_name, "r") as pas:
                data = json.load(pas)
                if data_1[0] in data.keys():
                    if data[data_1[0]] == data_1[1]:
                        print("Welcome to the cloud")
                    else:
                        print("Wrong password")
                else:
                    print("Wrong username")

        return wrapper
    return decorated_log


@dec_dec_log("me_json.json")
def log_in():
    login = input("Enter your login: ")
    password = input("Enter your password: ")

    return login, password


log_in()
