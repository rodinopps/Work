temp = int(input("What is the current temperature? "))

if temp >= 80:
    outfit = "WE'RE BURNING WHAT DO YOU MEAN OUTFIT???"
elif 60 <= temp <= 79:
    outfit = "WE ARE BURNING GET SOME ICE CUBES!!!"
else:
    outfit = "wear whatever.."

advice = (f"Today wear {outfit}")
print(advice)
