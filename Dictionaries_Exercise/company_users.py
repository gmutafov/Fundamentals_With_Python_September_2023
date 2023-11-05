company_info = {}
while True:
    data = input().split(" -> ")

    if data[0] == 'End':
        break

    company = data[0]
    employee_id = data[1]
    if company not in company_info:
        company_info[company] = [employee_id]
    else:
        if employee_id in company_info[company]:
            pass
        else:
            company_info[company].append(employee_id)


for company, employee_id in company_info.items():
    print(company)
    for employee in employee_id:
        print(f"-- {employee}")