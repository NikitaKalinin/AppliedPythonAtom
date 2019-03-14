import sys
import json
import csv

# Ваши импорты


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


def print_tabs(s, len_of, out):
    c = 0
    if len(list(s.values())) != 0:
        while c < len(min(list(s.values()), key=len)):
            tab = "|"
            for key in s:
                k = len_of[key] - len(s[key][c]) - 3
                if check_int(s[key][c]):
                    tab = tab + " " * k + s[key][c] + "  " + "|"
                else:
                    tab = tab + "  " + s[key][c] + " " * k + "|"
            c += 1
            out.append(tab)


def to_table_json(data, out):
    s = {}
    len_of = {}
    for d in data:
        for key in d:
            if key in s:
                s[key].append(str(d[key]))
            else:
                s[key] = [str(d[key])]
            len_of[key] = max(s[key], key=len)
            len_of[key] = len(len_of[key])
            if len(str(key)) > len_of[key]:
                len_of[key] = len(str(key))
            len_of[key] += 5
    sum = 0
    for key in len_of:
        sum += len_of[key]
    out.append("-"*(sum+1))
    title = "|"
    for key in len_of:
        title = title + " "*((len_of[key]-len(key)-1)//2) + key + " "*((len_of[key]-len(key)-1)//2)+'|'
    out.append(title)
    print_tabs(s, len_of, out)
    out.append("-"*(sum+1))


def to_table_tsv(file, e, out):
    len_of = []
    c = 0
    reader = open(file, encoding=e)
    data = csv.reader(open(file, encoding=e), delimiter="\t")
    for row in data:
        if c == 0:
            for r in row:
                len_of.append(len(str(r)))
            c = 1
        else:
            for i in range(len(row)):
                if len_of[i] < len(str(row[i])):
                    len_of[i] = len(str(row[i]))
    for i in range(len(len_of)):
        len_of[i] += 5
    s = 0
    for key in len_of:
        s += key
    out.append("-" * (s + 1))
    c = 0
    reader.close()
    data = csv.reader(open(file, encoding=e), delimiter="\t")
    for row in data:
        tab = "|"
        if c == 0:
            for i in range(len(row)):
                tab = tab + " "*((len_of[i]-len(row[i])-1)//2) + row[i] + " "*((len_of[i]-len(row[i])-1)//2)+'|'
            c = 1
        else:
            for i in range(len(row)):
                k = len_of[i] - len(row[i]) - 3
                if check_int(row[i]):
                    tab = tab + " " * k + row[i] + "  " + "|"
                else:
                    tab = tab + "  " + row[i] + " " * k + "|"
        out.append(tab)
    out.append("-"*(s+1))
    reader.close()


if __name__ == '__main__':
    to_out = ""
    f = file_valid_check()
    if f is not False:
        enc = encoding_check(f)
        if enc is not False:
            if json_check(f, enc) or tsv_check(f, enc):
                o = []
                if json_check(f, enc):
                    to_table_json(json.load(open(f, encoding=enc)), o)
                elif tsv_check(f, enc):
                    to_table_tsv(f, enc, o)
                for line in o:
                    print(line)
            else:
                print('Формат не валиден')
        else:
            print('Формат не валиден')
    else:
        print('Файл не валиден')
else:
    print('Файл не валиден')
# Ваш код
