import csv
from datetime import datetime

def calculate_salary(employee):
    base_salary = 3000  
    hourly_rate = 20  
    overtime_rate = 30  
    working_hours = 8
    max_productivity_score = 100

 
    arrival = datetime.strptime(employee['ArrivalTime'], '%H:%M')
    leave = datetime.strptime(employee['LeaveTime'], '%H:%M')
    total_hours_worked = (leave - arrival).seconds / 3600
    overtime = max(0, total_hours_worked - working_hours)

   
    total_vacation = int(employee['TotalVacationDays'])
    max_vacation = int(employee['MaxAllowedVacation'])
    vacation_penalty = max(0, total_vacation - max_vacation) * 50  

 
    alerts = int(employee['Alerts'])
    alert_penalty = alerts * 100  

 
    productivity = int(employee['ProductivityScore'])
    productivity_factor = productivity / max_productivity_score
    raise_amount = 200 if productivity > 90 else 0  

   
    normal_hours_salary = min(working_hours, total_hours_worked) * hourly_rate
    overtime_salary = overtime * overtime_rate
    total_salary = (base_salary + normal_hours_salary + overtime_salary + raise_amount) \
                   - vacation_penalty - alert_penalty

    return total_salary



def read_employee_data(file_name):
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        employees = [row for row in csv_reader]
    return employees


def write_salary_report(employees, file_name):
    with open(file_name, mode='w', newline='') as file:
        fieldnames = ['EmployeeID', 'Name', 'Salary']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for employee in employees:
            salary = calculate_salary(employee)
            writer.writerow({'EmployeeID': employee['EmployeeID'], 'Name': employee['Name'], 'Salary': salary})



def main():
    input_file = '/Users/Hamada/Desktop/code-work/code-working/employees.csv'
    output_file = 'salary_report.csv'

    employees = read_employee_data(input_file)
    write_salary_report(employees, output_file)
    print(f"Salary report generated: {output_file}")


if __name__ == "__main__":
    main()
