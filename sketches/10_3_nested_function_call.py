def A():
  print("A")


def B():
  print("B")
  A()


def C():
  print("C")
  A()
  B()


C()