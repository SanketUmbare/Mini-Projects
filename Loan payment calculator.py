# collect the necessary input: principal, interest, years
# calculate monthly payments
# show to user

def main():
    print("This is a Monthly payment loan calculator ")
    print("")


    principal=float(input("Input the loan amount: "))
    apr= float(input("Input the annual interest rate: "))
    years=float(input("Input amount of years: "))

    monthly_interest_rate= apr/ 1200
    months=years*12
    monthly_payment=principal*monthly_interest_rate/(1- (1+monthly_interest_rate) **(-months))


    print("The monthly payment for this loan is: %.2f" % monthly_payment)
    print("")
    print("")


while True:
    main()
