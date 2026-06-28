first_name = input("Enter your First name: ")
last_name = input("Enter your Last name: ")
full_name = first_name + ' ' + last_name
address = input("Enter your correct Address: ")
address += ', Apartment 4B'
employee_age = input("Enter you age: ")
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)
years_experience = 5
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department)
year_code = employee_code[4:8]
print(year_code)
initials = employee_code[9:11]
print(initials)
last_three  = employee_code[-3:]
print(last_three)