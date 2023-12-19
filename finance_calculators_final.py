import math

'''user chooses which calculator they want to use: bond or investment
if user chooses bond ask a set of questions: "present value of the house",
"the interest rate" , "the number of months they plan to take to repay the bond"
then calculate from their answers what their monthly repayment will be
if user chooses investment ask a set of questions "the amount of money they will deposit",
"the interest rate", "how many years they will invest", 
"whether they want simple or compound interest"
then calculate from their answers depending on simple or compound 
interest how much they will get back after the given period'''

   
#add variables for lines to use in the code
line_1 = "~" * 100 
line_2 = "=" * 100
line_3 = "*" * 100

#create a menu so the user knows where to start
print(f"{line_2}\nInvestment - to calculate the amount of interest \
you'll earn on your investment\n\n\
Bond - to calculate the amount you'll have to pay on a home loan\n{line_2}\n")

#get the user to input 'bond' or 'investment' to define which calculator they will be using
while True:
    user_calculator_choice = str(input("\nEnter either 'investment' or 'bond' from the menu\
 above to proceed: "))
    
    #convert user input to lower case
    user_choice = user_calculator_choice.lower()
    
    #create defensive program incase user enters anything other than 
    # investment or bond. 
    try:
        if user_choice not in ["investment", "bond"]:
            raise ValueError("Invalid choice. Please enter either 'investment' or 'bond'.")
        break
    except ValueError as raised_error:
        print(f"\n{line_3}\nError: {raised_error}\n{line_3}\n")
    continue

#if user chooses bond, ask for further inputs that can be used in the bond calculation
if user_choice == "bond":
        
        #create while loop to check for errors using try and except
        while True:
            try:
                
                    # add inputs asking for house value (intager), interest rate (float) 
                    # and monthly payments (intager). convert to integers
                    bond_property_value = int(input(f"{line_1}\nWhat is the present \
value of your house? "))

                    #put bond interest rate as a float so i can either input an interest 
                    #example of 1.5 or a whole number
                    bond_interest_rate = float(input("What is the interest rate? "))
                    bond_monthly_payments = int(input("How many monthly payments do \
you plan to take to repay the bond? "))
                    break
            except ValueError:
                    print(f"\n{line_3}\nError: Please enter valid input\n{line_3}")
                    continue

        #use stored values in the monthly repayment calculation and format
        i = (bond_interest_rate/100)/12
        p = bond_property_value
        n = bond_monthly_payments
        monthly_repayment = float(i * p)/(1 - (1 + i )**(-n))

        #round answer to 2 decimal places
        round_monthly_repayment = float(math.ceil(monthly_repayment*100)/100)

        #let the user know how much they will have to pay
        print(f"{line_1}\n{line_2}\nYou will have to pay £{round_monthly_repayment} \
each month\n{line_2}\n")

#if user chooses investment, ask for further inputs that can be used in the 
#investment calculation
elif user_choice == "investment":
            
            #create while loop to check for errors using try and except
            while True:
                try:
                    #if the user chooses the investment calculator, add inputs 
                    #asking how much they want to deposit, what the interest rate is,
                    #how many years to invest and if they want simple or compound interest. 
                    #convert to intagers.
                    investment_deposit = int(input(f"{line_1}\nWhat is the amount of \
money that you are depositing? "))

                    #put investment interest as a float so i can either input an 
                    #interest example of 1.5 or a whole number             
                    investment_interest = float(input("What is the interest rate? "))
                    investment_years = int(input("How many years do you plan on investing? "))
                    break
                except ValueError:
                            print(f"\n{line_3}\nError: Please enter valid input\n{line_3}")
                            continue
            
            #ask user if they want simple or compound interest
            #create while loop to check for errors using try and except
            #to check if user chooses anything other than simple or compound
            while True:
                interest = str(input(f"{line_1}\nPlease type whether you would like 'simple'\
 or 'compound' interest: "))
                user_interest_choice = interest.lower()                         
                   
                try:
                    if user_interest_choice not in ["simple", "compound"]:
                        raise ValueError ("Invalid choice. Please enter either 'simple' or \
'compound'.")
                    break
                    
                except ValueError as raised_error:
                        print(f"\n{line_3}\nError: {raised_error}\n{line_3}\n")
                        continue
                    

            #if user chooses simple then calculate the simple interest using previously 
            #stored values
            if user_interest_choice == "simple":
                            t = investment_years
                            r = investment_interest/100
                            p = investment_deposit
                            simple = float(p *(1 + r * t))

                            #round answer to 2 decimal places
                            round_simple = float(math.ceil(simple*100)/100)

                            #take away deposit from total interest icluding deposit
                            simple_interest = int(simple - p)
                            round_simple_interest = (math.ceil(simple_interest*100)/100)

                            #let the user know how much they have made in interest and the 
                            #total including interest and deposit
                            #create if statement if the user only picks 1 year of investment
                            if t == int(1):
                                print(f"{line_2}\nThe Simple interest you will receive over \
{t} year is: £{round_simple_interest} \nGiving you a total including your deposit and interest:\
 £{round_simple}\n{line_2}\n")
                            else:
                                print(f"{line_2}\nThe Simple interest you will receive over {t} \
years is: £{round_simple_interest} \nGiving you a total including your deposit and interest: \
£{round_simple}\n{line_2}\n")

            #if user chooses compound create elif statement to work out compound interest 
            #calculation
            elif user_interest_choice == "compound":
                                p = investment_deposit
                                r = investment_interest/100
                                t = investment_years
                                compound = float(p * math.pow((1+r),t))

                                #round answer to 2 decimal places
                                round_compound = float(math.ceil(compound*100)/100)

                                #take away deposit from total interest icluding deposit
                                compound_interest = float(compound - p)
                                round_compound_interest = float(math.ceil(compound_interest*100)/100)

                                #let the user know how much they have made in interest and the total 
                                #including interest and deposit
                                #create if statement if the user only picks 1 year of investment
                                if t == int(1):
                                    print(f"{line_2}\nThe Compound interest you will receive over {t} \
year is: £{round_compound_interest} \nGiving you a total including your deposit and interest: \
£{round_compound}\n{line_2}\n")
                                else:
                                    print(f"{line_2}\nThe Compound interest you will receive over {t} \
years is: £{round_compound_interest} \nGiving you a total including your deposit and interest: \
£{round_compound}\n{line_2}\n")