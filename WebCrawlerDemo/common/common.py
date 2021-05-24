import re
import openpyxl
import pprint
def get_phone_number(input):
    regex = r"tel:(?P<phone_number>\d*)"
    m = re.match(regex, input)
    if m:
        return m.group('phone_number')
    return ""

def clean_data(input):
    regex = r"^\s|\s$|(?<=\B)\s|\s(?=\B)"
    if type(input) is list:
        return_list = []
        for item in input:
            item = item.replace('\n', '')
            item = re.sub(regex, "", item)
            return_list.append(item.strip())
        return return_list

    return input.strip()
    # return re.sub(r"[\n]*", input.strip())

def get_district(input):
    return input.split(",")[-2]

def get_school_id(input):
    m = re.match(r"school-(?P<id>\d+)", input)
    if m:
        return m.group('id')
    return 0

def write_to_file(input_list):
    print("Write FIle")
    wb = openpyxl.load_workbook('DanhSachTruongMamNonDN.xlsx')
    sheet = wb['result']

    current_row = 6
    for i in range (6, 140):
        if sheet['B' + str(i)].value is None:
            print("Set current_row: " + str(i))
            current_row = i
            break

    for row in input_list:
        print("Start Row: " + str(current_row))
        # sheet['A' + str(current_row)] = row['school_id']
        sheet['B' + str(current_row)] = row['name']
        sheet['C' + str(current_row)] = row['school_type']
        sheet['D' + str(current_row)] = row['address']
        sheet['E' + str(current_row)] = row['district']
        sheet['F' + str(current_row)] = row['age_range']
        sheet['G' + str(current_row)] = row['school_fee']

        sheet['Q' + str(current_row)] = row['internal_link']
        sheet['N' + str(current_row)] = ",".join(row['options'])

        current_row += 1

    wb.save('DanhSachTruongMamNonDN.xlsx')