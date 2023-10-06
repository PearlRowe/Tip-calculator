#ROWE PEARL ROWENA
#SCT211-0678/2021
bill =float(input("enter amount"))
Percentage_tip=int(input(" tip is 10%,12% or 15%"))
Number_of_people=int(input("Number of people splitting bill is"))
Tip=bill*(Percentage_tip/100)
Amount_to_be_paid=bill+Tip
Amount_per_person=Amount_to_be_paid/Number_of_people
K=round(Amount_per_person, 2)
print("Each person pays:" , K)
