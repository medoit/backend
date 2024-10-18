from datetime import datetime
from .models import Sub, Snls

def load_sub():
    Sub.objects.all().delete()
    filepath = "../source/sub/t_data_sub.txt"
    with open(filepath) as file:
        for line in file:
            el = line.split(';')
            sub = Sub.objects.get_or_create(
                id_sub = int(el[0]),
                serias = int(el[1]),
                since = format_date(el[2]),
                till = format_date(el[3]),
                sale_date = format_date(el[4]),
                pan = el[5].replace('"', '').strip()
            )

def load_snls():
    Snls.objects.all().delete()
    filepath = "../source/snls/SNLS.txt"
    with open(filepath) as file:
        for line in file:
            new_line = []
            for i in range(len(line)):
                if line[i] == '\0':
                    new_line.append(line[i - 1])
                    new_line[i - 1] = '0'
                else:
                    new_line.append(line[i])
            new_line = ''.join(map(str, new_line))
            snls = Snls.objects.get_or_create(
                pan = new_line[:-3],
                serias = new_line[-3: -1]
            )

def format_date(str):
    fromats = [
        '"%Y-%m-%d %H:%M:%S"',
        '"%Y-%m-%d %H:%M:%S.%f"',
        '%d.%m.%Y',
        '%d.%m.%y',
        '%H:%M:%S'
    ]
    for el in fromats:
        try:
            result = bool(datetime.strptime(str, el))
        except:
            result = False
        if result:
            return datetime.strptime(str, el)