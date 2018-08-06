__author__ = 'Kalyan'

max_marks = 30

problem_notes = '''                                                                    
This problem deals with a custom encryption/decryption scheme that works as follows.  

Given a string like "how are you?" and m * n grid. The characters of the string are fi
into the grid row wise top to bottom. So for 3 * 5 you get                            

h o w _ a                                                                             
r e _ y o                                                                             
u ? * * *                                                                             

In the above example _ is shown visually where there is a space character. Unfilled ce

The encrypted string is found by starting at a specified corner and going clockwise in
a decreasing spiral till all the cells are covered. So if corner is top right you get 


Notes:                                                                                
1. raise TypeError if text is not a str or key is not EncryptKey                      
2. raise ValueError if the grid cannot accomodate the text  or if rows/cols are <= 0  
3. returns the encrypted string as specified above.                                   
4. see the definitions for Corner and EncryptKey in mock1common.py                    
'''

from mock1common import EncryptKey, Corner

def encrypt(text, key):
    if (not isinstance(text, str)) or (not isinstance(key, EncryptKey)):
        raise TypeError
    if (key[0] * key[1] < len(text)) or (key[0] * key[1] <= 0):
        raise ValueError
    if len(text) < key[0] * key[1]:
        text = text + "*" * ((key[0] * key[1]) - len(text))
    arr = [list(text[i*key[1] : i*key[1]+key[1]]) for i in range(key[0])]
    s = ""
    s_length = 0
    text_length = len(text)
    start = 0
    s_row = 0
    s_col = 0
    e_row = key[0] - 1
    e_col = key[1] - 1
    while (e_row >= s_row and e_col >= s_col):
        if(start and s_length < text_length) or (start == 0 and key[2] == Corner.TOP_LEFT):
            start = 1
            for i in range(s_col, e_col + 1):
                s = s + arr[s_row][i]
                s_length += 1
            s_row += 1
        if(start and s_length < text_length) or (start == 0 and key[2] == Corner.TOP_RIGHT):
            start = 1
            for i in range(s_row, e_row + 1):
                s = s + arr[i][e_col]
                s_length += 1
            e_col -= 1
        if (start and s_length < text_length) or (start == 0 and key[2] == Corner.BOTTOM_RIGHT):
            start = 1
            for i in range(e_col, s_col - 1, -1):
                s = s + arr[e_row][i]
                s_length += 1
            e_row -= 1
        if (start and s_length < text_length) or (start == 0 and key[2] == Corner.BOTTOM_LEFT):
            start = 1
            for i in range(e_row, s_row - 1, -1):
                s = s + arr[i][s_col]
                s_length += 1
            s_col += 1
    return s

def test_encrypt():
    assert "ao***?urhow y e" == encrypt("how are you?", EncryptKey(3, 5, Corner.TOP_RIGHT))
