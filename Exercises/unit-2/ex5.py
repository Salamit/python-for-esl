# # # P = principal amount(Initial investment)
# r = annual nominal interest rate (as a decimal)
# n = number of times the interest is compunded per year
# t = number of years. 
#name = input("Please enter your name: ")
### Write a program that replaces these letters with something a bit more 
# human-readable, and calculate tehh interest for some 
# varying amounts of money at realistic interest rates
# such as 1% and -0.05%. 
# When you have that working, ask the user for teh value of some
# of these variabbles and do the calculation
# ##
# ###
### A = P(1 + r/n)nt

initialInvestment = 100
nominalRate = 0.01
numberOfTimesInterestCompounded = 12
numberOfYears = 1


finalAmount = initialInvestment * (1 + nominalRate/numberOfTimesInterestCompounded) ** (numberOfTimesInterestCompounded * numberOfYears)
print(finalAmount)

nominalRate = -0.05
finalAmount = initialInvestment * (1 + nominalRate/numberOfTimesInterestCompounded) ** (numberOfTimesInterestCompounded * numberOfYears)
print(finalAmount)