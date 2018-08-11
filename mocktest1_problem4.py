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
    if (key.rows * key.cols != len(encrypted_text)) or (key.rows * key.cols <= 0) or (not isinstance(key.corner, Corner)):
        raise ValueError
    strarr = [i for i in range(key.rows * key.cols)]
    text_len = len(encrypted_text)
    start = 0
    cur_ind = 0
    s_row = 0
    s_col = 0
    e_row = key.rows - 1
    e_col = key.cols - 1
    while (e_row >= s_row and e_col >= s_col):
        if(start and cur_ind < text_len) or (start == 0 and key.corner == Corner.TOP_LEFT):
            start = 1
            for i in range(s_col, e_col + 1):
                strarr[(s_row * key.cols) + i] = encrypted_text[cur_ind]
                cur_ind += 1
            s_row += 1
        if(start and cur_ind < text_len) or (start == 0 and key.corner == Corner.TOP_RIGHT):
            start = 1
            for i in range(s_row, e_row + 1):
                strarr[(i * key.cols) + e_col] = encrypted_text[cur_ind]
                cur_ind += 1
            e_col -= 1
        if(start and cur_ind < text_len) or (start == 0 and key.corner == Corner.BOTTOM_RIGHT):
            start = 1
            for i in range(e_col, s_col - 1, -1):
                strarr[(e_row * key.cols) + i] = encrypted_text[cur_ind]
                cur_ind += 1
            e_row -= 1
        if(start and cur_ind < text_len) or (start == 0 and key.corner == Corner.BOTTOM_LEFT):
            start = 1
            for i in range(e_row, s_row - 1, -1):
                strarr[(i * key.cols) + s_col] = encrypted_text[cur_ind]
                cur_ind += 1
            s_col += 1
    strarr = "".join(strarr).replace("*","")
    return strarr

# a basic test is given, write your own tests based on constraints.
def test_decrypt():
    assert "how are you?" == decrypt("ao***?urhow y e", EncryptKey(3, 5, Corner.TOP_RIGHT))
