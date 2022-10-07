import hmac


student = {"arslan":23, "adnan":21, "hamza":20, "armaghan":19}
print(student)
print(len(student))
del student["armaghan"]
print(student)
student["armaghan"] = 22
print(student)
student["hamza"] = 32
print(student)