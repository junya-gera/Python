# coding: utf-8
# Python2ではソースコードに日本語が含まれていた場合、↑の記述が必要

msg = "Hello World"
# Python2では()は必要ないが3では必ず必要
print(msg)

# 大文字で表した変数は定数とみなす。再代入はできてしまう
ADMIN_EMAIL = "aaa@gmail.com"

# 論理値は大文字で始まるTrue False
flag = True

x = 10
print(x // 3) # 切り捨て割り算

print(True and False) # False
print(True or False) # True
print(not True) # False