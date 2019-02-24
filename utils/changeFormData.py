import re

def change(form_data):
    data_list = form_data.split("\n")
    for d in data_list:
        d = re.sub("\s", '":"', d)
        d = '"' + d + '",'
        print(d)
