income=float(input("Enter your monthly income: "))
expensse=float(input("Enter your total monthly expenses: "))
saving=income-expensse
saving_year=saving*12+(saving*12*0.05)
print(f"Your monthly savings are : {saving}")
print(f"Projected savings after one year, with interest, is: {saving_year}")
