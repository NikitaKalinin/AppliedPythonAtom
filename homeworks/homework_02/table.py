import json

# Ваши импорты
from to_table import to_table_json, to_table_tsv
from checks import json_check, tsv_check, encoding_check, file_valid_check


# Ваш код
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
