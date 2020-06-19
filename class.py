class User:
  # コンストラクタ
  def __init__(self,name):
    # インスタンス変数
    self.name = name

# tom = User()
# tom.name = "tom"
# tom.score = 20

# bob = User()
# bob.name = "bob"
# bob.level = 5

# print(tom.name)
# print(bob.level)
tom = User("tom")
bob = User("bob")

print(tom.name)
print(bob.name)
