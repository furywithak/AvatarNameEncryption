
import hashlib
import sys
from openpyxl import load_workbook


def encrypt_avatarname(avatarname):
    '''

    :param avatarname: string
    :return: uppercase SHA-3 string

    Example:
    encrypt_avatarname("queen123")
    e9a5f8e9acbdbd74f9bc3aeb33ef7728204e7471682ff111915e2cc8

    '''
    enc_s = hashlib.sha256(avatarname.encode('utf-8')).hexdigest()
    return enc_s

def read_excelfile(excelfile_name):
    wb = load_workbook(excelfile_name)
    sheet = wb.active

    # A refers to column, replace with column number
    for cell in sheet["A"]:
        print(encrypt_avatarname(cell.value))

def main():
    read_excelfile("test_file.xlsx")


if __name__ == "__main__":
    main()
