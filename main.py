def main():
    print("Monthly loan payment calculator.")
    print("")

    principle = float(input("Input loan amount: ")) # No symbols are needed, just integers and decimals
    apr = float(input("Input the annual interest rate: ")) 
    years = int(input("Input the amount of years: "))

    monthly_interest_rate = apr / 1200 #This is to get the rate
    amount_of_months = years * 12
    monthly_payment = principle * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))

    print("The monthly payment for this loan is: $%.2f " % monthly_payment) #The %.2f is to cut off the decimal at the first two digits

main()
