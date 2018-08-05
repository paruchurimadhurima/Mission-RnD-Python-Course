__author__ = 'Kalyan'

max_marks = 20

notes = '''
This is the counterpart to the encrypt routine that you wrote in problem 3. 

You are given the encrypted string, the original key used to encrypt the original string.

Your job is to reconstruct the original string.

Notes:
1. raise TypeError if text is not a str or key is not EncryptKey
2. raise ValueError if the grid is invalid (ie) cannot accomodate the text  or if rows/cols are <= 0 
3. returns the original string (remove the padding chars).
4. You can assume that the original string does not contain the padding chars
5. see the definitions for Corner and EncryptKey in mock1common.py

'''

from mock1common import EncryptKey, Corner

def decrypt(encrypted_text, key):
    if (not isinstance(encrypted_text, str)) or (not isinstance(key, EncryptKey)):
        raise TypeError
    if (key[0] * key[1] != len(encrypted_text)) or (key[0] * key[1] <= 0):
        raise ValueError
    strarr = [i for i in range(key[0] * key[1])]
    encrypted_text = iter(encrypted_text)
    s_row = 0
    s_col = 0
    e_row = key[0] - 1
    e_col = key[1] - 1
    start = 0
    while (e_row >= s_row and e_col >= s_col):
        if (start == 0 and key[2] == Corner.TOP_LEFT) or start:
            start = 1
            for i in range(s_col, e_col + 1):
                strarr[(s_row * key[1]) + i] = encrypted_text.__next__()
            s_row += 1
        if (start == 0 and key[2] == Corner.TOP_RIGHT) or start:
            start = 1
            for i in range(s_row, e_row + 1):
                strarr[(i * key[1]) + e_col] = encrypted_text.__next__()
            e_col -= 1
        if (start == 0 and key[2] == Corner.BOTTOM_RIGHT) or start:
            start = 1
            for i in range(e_col, s_col - 1, -1):
                strarr[(e_row * key[1]) + i] = encrypted_text.__next__()
            e_row -= 1
        if (start == 0 and key[2] == Corner.BOTTOM_LEFT) or start:
            start = 1
            for i in range(e_row, s_row - 1, -1):
                strarr[(i * key[1]) + s_col] = encrypted_text.__next__()
            s_col += 1
    strarr = "".join(strarr).replace("*","")
    return strarr

# a basic test is given, write your own tests based on constraints.
def test_decrypt():
    assert "how are you?" == decrypt("ao***?urhow y e", EncryptKey(3, 5, Corner.TOP_RIGHT))