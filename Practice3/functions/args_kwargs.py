def my_function(*args):
  print("Type:", type(args))#tuple
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

#**kwards
def f(student_id, **details):
  print("id:", student_id)
  print("Additional details:")
  for key, value in details.items():
    print(key + ":", value)
f("25B032201", age=18, city="Aksay",name="Raymbek")