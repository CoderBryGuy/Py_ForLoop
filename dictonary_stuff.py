employee = {}
print(employee)

employee = {"Mary" : 24, "Frank": 28, "Gru": 40}
print(employee)

employee["pigggy"] = 23

print(employee)

employee["Gru"] = 41

print(employee)

del employee["Frank"]

print(employee)

print(employee.keys())

a = list(employee.keys())
print(a)

print(a[0])

print(employee.values())

b = list(employee.values())
print(b[0])

print(employee.items())

