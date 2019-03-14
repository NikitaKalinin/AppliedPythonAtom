import json
import csv
import sys


def encoding_check(file):
    for e in ['utf-16', 'utf8', 'cp1251']:
        try:
            with open(file, "r", encoding=e) as file_c:
                file_c.readlines()
                file_c.close()
            return e
        except UnicodeError:
            continue
    return False


def file_valid_check():
    try:
        open(sys.argv[1])
        return sys.argv[1]
    except FileNotFoundError:
        return False


def json_check(file, e):
    with open(file, encoding=e) as file_c:
        try:
            list_of_key = []
            checker = json.load(file_c)
            list_of_key.append(list(checker[0].keys()))
            for key in checker:
                if list(key.keys()) != list_of_key[0] or list(key.keys()) == []:
                    return False
                list_of_key.append(list(key.values()))
            return True
        except (json.JSONDecodeError, KeyError, IndexError):
            return False


def tsv_check(file, e):
    with open(file, encoding=e) as file_c:
        data_list = csv.reader(file_c, delimiter='\t')
        for key in data_list:
            if len(key) == 0:
                return False
    return True


def check_int(x):
    try:
        a = int(x)
        return True
    except:
        return False
