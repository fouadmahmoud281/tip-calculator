print("welcom to tip calcultor app""welcom to tip calcultor app")
print("(an app to save you if you are bad in math)")
total_bill = input("enter the total bill? ")
precentage = input("enter the precentage tip you want to give 10,12 or 15? ")
people = input("how many people you want to split the tip on them? ")

tip = float(total_bill) * float(precentage) /100
totl= round((float(total_bill) + tip) / int(people),1)
print(f"every one should pay: {totl} egyptian pound")
