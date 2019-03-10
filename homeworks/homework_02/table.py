import sys
import json

# Ваши импорты

encoding = ["utf-8", "cp1251", "utf-16"]


def checking_enc(x):
    for enc in encoding:
        try:
            open(x, encoding=enc).read()
            return enc
        except:
            continue


if __name__ == '__main__':
    filename = sys.argv[1]
print(checking_enc(filename))

    # Ваш код


