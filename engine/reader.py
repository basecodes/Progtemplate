import csv
import json
import glob

from json import JSONDecodeError

import xmltodict
from pathlib import Path
import yaml


def csv_reader(path):
    with open(path) as file:

        try:
            reader = csv.reader(file)
        except BaseException as error:
            print("解析CSV文件出错！")
            exit()

        array = list(reader)
        save = dict()
        for line in range(0, len(array)):
            tmp = dict()
            for col in range(len(array[0])):
                tmp[array[0][col]] = array[line][col]
            save[line] = Wrapper(tmp)

        wrapper = Wrapper(save)
        return wrapper


class Wrapper:
    def __init__(self, fields):
        self.__dict__ = fields

    def __getitem__(self, name):
        return self.__dict__[name]

    def __len__(self):
        return len(self.__dict__)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def items(self):
        return self.__dict__.items()


def object_hook(v):
    return Wrapper(v)


def json_reader(path):
    with open(path) as file:
        txt = file.read()
        if txt == "":
            print("%s 为空！" % path)
            return
        return json_reader_string(txt)


def json_reader_string(txt):
    try:
        reader = json.loads(txt, object_hook=object_hook)
        return reader
    except JSONDecodeError as error:
        print("json解析出错：行号(%s) !" % error.lineno)
        exit()


def yaml_reader(path):
    with open(path) as file:
        try:
            reader = yaml.safe_load(file)
            return json_reader_string(json.dumps(reader))
        except yaml.YAMLError as exc:
            print(exc)


def xml_reader(path):
    with open(path, "r") as file:
        try:
            doc = xmltodict.parse(file.read())
            return json_reader_string(json.dumps(doc))
        except BaseException as error:
            print("解析xml出错！")
            exit()


def directory_reader(directory, suffix):
    fmt = directory + '/*.' + suffix
    files = glob.glob(fmt)
    return files


def file_name(path):
    p = Path(path)
    return p.stem


def file_name_suffix(path):
    p = Path(path)
    return p.name


def file_reader(path):
    with open(path, "r") as file:
        txt = file.read()
        return txt
