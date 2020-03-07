# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""


import sys

a = 1
b = "some string"

def foo():
    print("This is the function 'foo'")

print("This is the top level")

##コードブロックは呼び出して使ったときのみ起動
##テスト時などに使用するとよい
if __name__ == '__main__':
    print("This is the code block")