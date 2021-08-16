
employee_file = open("26 Employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
