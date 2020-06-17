# 関数
def say_hi(name,age = 20):  # age=20は初期値
  print("hi {0} ({1})".format(name,age))

say_hi("tom",23)
say_hi("bob",21)
say_hi("steve")