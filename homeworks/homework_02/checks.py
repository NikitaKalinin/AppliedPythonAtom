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
    try:
        json.loads(open(file, encoding=e).read())
        return True
    except json.JSONDecodeError:
        return False


def tsv_check(file, e):
    try:
        data = csv.reader(open(file, encoding=e), delimiter='\t')
        check_list = []
        for i in list(data):
            check_list.append(len(i))
        if check_list.count(check_list[0]) == len(check_list):
            return True
    except:
        return False


def check_int(x):
    try:
        a = int(x)
        return True
    except:
        return False
