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

name = "sinomiya"
# ()の中は入力時のメッセージ
score = int(input("score?"))
# if score > 80:
#   print("Great!")
# elif score > 60:
#   print("Good!")
# else:
#   print("so so...")
print("Great!" if score > 80 else "so so...")

# 文字列の中で変数を使う。文字列→%s,小数→%f,整数→%d。最後に%()の中に順番に変数を入れる
print("name: %s, score: %f" %(name,score))
# この書き方もできる
print("name: {0}, score: {1}".format(name,score))

i = 0
while i < 10:
  if i == 5:
    break
  print(i)
  i += 1
else:
  print("end")