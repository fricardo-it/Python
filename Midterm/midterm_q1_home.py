## Q1

hourly_wage = 0

while hourly_wage == 0:
    hourly_wage = float(input("Enter the hourly wage: "))
    hours_week = float(input("Enter the hours per week: "))
    qty_weeks = 52
    annual_amount = qty_weeks * hours_week * hourly_wage

    taxable_income = annual_amount
    tax = 0

    if taxable_income <= 30000:
        tax += taxable_income * .1
        taxable_income -= 30000
    elif taxable_income <= 60000: 
        tax += (30000 * .1) + (taxable_income-30000) * .15
        taxable_income -= 60000
    elif taxable_income <= 100000:
        tax += (30000 * .1) + (30000 * 0.15) + (taxable_income-60000) * 0.2
        taxable_income -= 40000  
    else:
        tax += (30000 * .1) + (30000 * 0.15) + (40000 * 0.2) + (taxable_income-100000) * 0.25

    print("Annual Salary: ",annual_amount)
    print("Tax Income: ",tax)
