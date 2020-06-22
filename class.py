# -*- coding: utf-8 -*-

class User:
  # クラス変数
  count = 0
  # コンストラクタ
  def __init__(self,name):
    User.count += 1
    # インスタンス変数
    self.name = name

  def say_hi(self):
    print("hi {0}".format(self.name))

# tom = User()
# tom.name = "tom"
# tom.score = 20

# bob = User()
# bob.name = "bob"
# bob.level = 5

# print(tom.name)
# print(bob.level)
print(User.count)
tom = User("tom")
bob = User("bob")
print(User.count)

print(tom.name)
print(tom.count)
print(bob.name)
print(bob.count)
