import json
import yaml


def json_to_text(file_name: str):
    """
    Convert json file to txt file
    :param file_name:
    :return:
    """
    with open(file_name, "r") as can:
        data = str(json.load(can))
    print(data)
    with open(file_name.split(".")[0] + ".txt", "w") as text:
        text.write(data)


# json_to_text("me_json.json")


def json_to_yaml(file_name: str):
    """
    Convert json to yaml
    :param file_name:
    :return:
    """
    with open(file_name, "r") as json_name:
        data_2 = json.load(json_name)

    with open(file_name.split(".")[0] + ".yaml", "w") as yaml_file:
        yaml.dump(data_2, yaml_file)

# json_to_yaml("me_json.json")

def yaml_to_json(file_name: str):
    """
    Convert yaml to json
    :param file_name:
    :return:
    """
    with open(file_name, "r") as yf:
        data_3 = yaml.load(yf, Loader=yaml.Loader)

    with open(file_name.split(".")[0] + ".json", "w") as jf:
        json.dump(data_3, jf)

# yaml_to_json("me_json.yaml")

def yaml_to_text(file_name: str):
    """
    Convert yaml to text
    :param file_name:
    :return:
    """
    with open(file_name, "r") as yf:
        data_4 = yaml.load(yf, Loader=yaml.Loader)

    with open(file_name.split(".")[0] + ".txt", "w") as jf:
        jf.write(str(data_4))


yaml_to_text("3")