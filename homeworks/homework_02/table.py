import sys
import json
import csv

# Ваши импорты
encode = ["utf-8", "cp1251", "utf-16"]


def encoding_check(file):
    for e in encode:
        try:
            open(file, encoding=e).read()
            return e
        except:
            continue
    return False


def file_valid_check():
    try:
        open(sys.argv[1])
        return sys.argv[1]
    except:
        return False


def json_check(file, e):
    try:
        json.loads(open(file, encoding=e).read())
        return True
    except:
        return False


def tsv_check(file, e):
    try:
        csv.DictReader(open(file, encoding=e), delimiter="\t")
        return True
    except:
        return False


def print_tabs(s, len_of, out):
    c = 0
    while c < len(min(list(s.values()), key=len)):
        tab = "|"
        for key in s:
            k = (len_of[key]-len(s[key][c])-1)//2
            m = abs(len(" " * k + s[key][c] + " " * k + "|") - len_of[key])
            tab = tab + " "*k + s[key][c] + " "*k+ " "*m + "|"
        c += 1
        out.append(tab)


def to_table(data, out):
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
            len_of[key] += 1
    sum = 0
    for key in len_of:
        sum += len_of[key]
    out.append("-"*(sum+1))
    title = "|"
    for key in len_of:
        title = title + " "*((len_of[key]-len(key)-1)//2) + key + " "*((len_of[key]-len(key)-1)//2)+'|'
    out.append(title)
    out.append("-"*(sum+1))
    print_tabs(s, len_of, out)
    out.append("-"*(sum+1))


if __name__ == '__main__':
    f = file_valid_check()
    if f is not False:
        enc = encoding_check(f)
        if enc is not False:
            if json_check(f, enc) or tsv_check(f, enc):
                o = []
                if json_check(f, enc):
                    to_table(json.loads(open(f, encoding=enc).read()), o)
                elif tsv_check(f, enc):
                    to_table(csv.DictReader(open(f, encoding=enc), delimiter="\t"), o)
                for l in o:
                    print(l)
            else:
                print("Формат не валиден")
        else:
            print("Формат не валиден")
    else:
        print("Файл не валиден")
else:
    print("Файл не валиден")


# Ваш код
