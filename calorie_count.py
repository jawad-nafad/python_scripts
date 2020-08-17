input_date=input("Today's date? \n")
breakfast_calorie=int(input("Breakfast Calories? \n"))
lunch_calorie=int(input("Lunch Calories? \n"))
dinner_calorie=int(input("Dinner Calories? \n"))
snack_calorie=int(input("Snack Calories? \n"))
total_calorie=breakfast_calorie + lunch_calorie + dinner_calorie + snack_calorie
print("Calorie content for " + input_date +": "+ str(total_calorie))