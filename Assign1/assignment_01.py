## Question 1 - Change the values of variables ##
print("Question 1 - Change the values of variables")
var_1 = float(input("Type the 1st value: "))
var_2 = float(input("Type the 2nd value: "))
print("Var1: {user_var_1}, Var2: {user_var_2}".format(user_var_1=var_2,user_var_2=var_1))

## Question 2 - calculate the Amount ##
print("\n\nQuestion 2 - calculate the Amount")
principal_amount = float(input("Type your Principal Amount($ 0.00): $ "))
annual_rate = float(input("Type the annual rate (0.00): "))
time_in_years = float(input("Type the time (in years): "))
mount = 1
amount = principal_amount*((1+(annual_rate/mount))**(mount*time_in_years))
print("Using the formula: A = P(1+r/m)^mt, your amount (A) is: $ {A:.2f}".format(A=amount))
