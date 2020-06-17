# -*- coding: utf-8 -*-
# 関数
def say_hi(name,age = 20):  # age=20は初期値
  print("hi {0} ({1})".format(name,age))

say_hi("tom",23)
say_hi("bob",21)
say_hi("steve")

def say_hello():
  # 関数の中身がない場合、もしくは後で書くので何か書いておきたい場合はpassとかく
  # Noneが返る
  pass
  # return "hello"

msg = say_hello()
print(msg)