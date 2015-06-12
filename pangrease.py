# General Annotations
	# The "print" command displays a variable or content to the screen
	# The "input" command allows the user to input data and the program stores it as a variable - "int" means an integer input and "str" means a string input
	# Float is similar to int in that the input is a number, but a float can be any number not just an integer
	# The continue command is used to make the program go back to the beginning of the loop after a set of instructions
	# IF/ELSE statements give instructions to follow depending on whether specific requirements are TRUE or FALSE

	# Sets the variable "loop" as 1 and declares the start of an instruction set while "loop" is 1
loop = 1
while loop == 1:

	print ("Welcome to Pan Grease.")

	recipe_name = input(str("What is the name of the recipe? "))

	print (" ")
	print ("1.")
	print ("2.")
	print ("3.")
	print ("4.")
	print ("5.")
	print ("6.")
	print (" ")

	ingredient_number = int(input("How many ingredients are there? "))

	if ingredient_number == 1:
		ingredient_1 = str(input("What is the first ingredient? "))
		ingredient_number1 = float(input("How much of the ingredient is there? "))
		units1 = str(input("What are the units for the ingredient? "))

		ingredient1people = int(input("How many people does it serve? "))
		ingredient1final = int(input("How many people should it serve? "))

		if ingredient1final == 1:
			ingredient1end = ingredient_number1 / ingredient1people
			print(" ")
			print("--------------------------------------------------")
			print ("Recipe Name:", recipe_name)
			print ("Ingredient Name:", ingredient_1)
			print ("Amount Of Ingredient:", ingredient1end, units1)
			print ("Serves:", ingredient1final, "people")
			print("--------------------------------------------------")
			print (" ")
			continue

		else:

			if ingredient1final > ingredient1people:
				ingredient1end1 = ingredient1final * ingredient_number1
				ingredient1end = ingredient1end1 / ingredient1people
				print(" ")
				print("--------------------------------------------------")
				print ("Recipe Name:", recipe_name)
				print ("Ingredient Name:", ingredient_1)
				print ("Amount Of Ingredient:", ingredient1end, units1)
				print ("Serves:", ingredient1final, "people")
				print("--------------------------------------------------")
				print (" ")

			if ingredient1final < ingredient1people:
				ingredient1end = ingredient_number1 / ingredient1final
				print(" ")
				print("--------------------------------------------------")
				print ("Recipe Name:", recipe_name)
				print ("Ingredient Name:", ingredient_1)
				print ("Amount Of Ingredient:", ingredient1end, units1)
				print ("Serves:", ingredient1final, "people")
				print("--------------------------------------------------")
				print (" ")

	if ingredient_number == 2:
		ingredient_1 = str(input("What is the first ingredient? "))
		ingredient_number1 = float(input("How much of the ingredient is there? "))
		units1 = str(input("What are the units for the ingredient? "))

		ingredient1people = int(input("How many people does it serve? "))
		ingredient1final = int(input("How many people should it serve? "))

		ingredient_2 = str(input("What is the second ingredient? "))
		ingredient_number2 = float(input("How much of the ingredient is there? "))
		units2 = str(input("What are the units for the ingredient? "))

		if ingredient1final > ingredient1people:
			ingredient1end1 = ingredient1final * ingredient_number1
			ingredient1end = ingredient1end1 / ingredient1people
			ingredient2end2 = ingredient1final * ingredient_number2
			ingredient2end = ingredient2end2 / ingredient1people

		if ingredient1final < ingredient1people:
			ingredient1end = ingredient_number1 / ingredient1final
			ingredient2end = ingredient_number2 / ingredient1final

		if ingredient1final == 1:
			ingredient1end = ingredient_number1 / ingredient1people
			ingredient2end = ingredient_number2 / ingredient1people

		print(" ")
		print("--------------------------------------------------")
		print ("Recipe Name:", recipe_name)
		print ("Ingredient(s) Name:", ingredient_1,",",ingredient_2)
		print ("Amount Of Ingredient(s):", ingredient1end,units1,",",ingredient2end,units2)
		print ("Serves:", ingredient1final, "people")
		print("--------------------------------------------------")
		print (" ")

	if ingredient_number == 3:
		ingredient_1 = str(input("What is the first ingredient? "))
		ingredient_number1 = float(input("How much of the ingredient is there? "))
		units1 = str(input("What are the units for the ingredient? "))

		ingredient1people = int(input("How many people does it serve? "))
		ingredient1final = int(input("How many people should it serve? "))

		ingredient_2 = str(input("What is the second ingredient? "))
		ingredient_number2 = float(input("How much of the ingredient is there? "))
		units2 = str(input("What are the units for the ingredient? "))

		ingredient_3 = str(input("What is the third ingredient? "))
		ingredient_number3 = float(input("How much of the ingredient is there? "))
		units3 = str(input("What are the units for the ingredient? "))

		if ingredient1final > ingredient1people:
			ingredient1end1 = ingredient1final * ingredient_number1
			ingredient1end = ingredient1end1 / ingredient1people
			ingredient2end2 = ingredient1final * ingredient_number2
			ingredient2end = ingredient2end2 / ingredient1people
			ingredient3end3 = ingredient1final * ingredient_number3
			ingredient3end = ingredient3end3 / ingredient1people

		if ingredient1final < ingredient1people:
			ingredient1end = ingredient_number1 / ingredient1final
			ingredient2end = ingredient_number2 / ingredient1final
			ingredient3end = ingredient_number3 / ingredient1final

		if ingredient1final == 1:
			ingredient1end = ingredient_number1 / ingredient1people
			ingredient2end = ingredient_number2 / ingredient1people
			ingredient3end = ingredient_number3 / ingredient1people

		print(" ")
		print("--------------------------------------------------")
		print ("Recipe Name:", recipe_name)
		print ("Ingredient(s) Name:", ingredient_1,",",ingredient_2,",",ingredient_3)
		print ("Amount Of Ingredient(s):", ingredient1end,units1,",",ingredient2end,units2,",",ingredient3end,units3)
		print ("Serves:", ingredient1final, "people")
		print("--------------------------------------------------")
		print (" ")

	if ingredient_number == 4:
		ingredient_1 = str(input("What is the first ingredient? "))
		ingredient_number1 = float(input("How much of the ingredient is there? "))
		units1 = str(input("What are the units for the ingredient? "))

		ingredient1people = int(input("How many people does it serve? "))
		ingredient1final = int(input("How many people should it serve? "))

		ingredient_2 = str(input("What is the second ingredient? "))
		ingredient_number2 = float(input("How much of the ingredient is there? "))
		units2 = str(input("What are the units for the ingredient? "))

		ingredient_3 = str(input("What is the third ingredient? "))
		ingredient_number3 = float(input("How much of the ingredient is there? "))
		units3 = str(input("What are the units for the ingredient? "))

		ingredient_4 = str(input("What is the fourth ingredient? "))
		ingredient_number4 = float(input("How much of the ingredient is there? "))
		units4 = str(input("What are the units for the ingredient? "))

		if ingredient1final > ingredient1people:
			ingredient1end1 = ingredient1final * ingredient_number1
			ingredient1end = ingredient1end1 / ingredient1people
			ingredient2end2 = ingredient1final * ingredient_number2
			ingredient2end = ingredient2end2 / ingredient1people
			ingredient3end3 = ingredient1final * ingredient_number3
			ingredient3end = ingredient3end3 / ingredient1people
			ingredient4end4 = ingredient1final * ingredient_number4
			ingredient4end = ingredient4end4 / ingredient1people

		if ingredient1final < ingredient1people:
			ingredient1end = ingredient_number1 / ingredient1final
			ingredient2end = ingredient_number2 / ingredient1final
			ingredient3end = ingredient_number3 / ingredient1final
			ingredient4end = ingredient_number4 / ingredient1final

		if ingredient1final == 1:
			ingredient1end = ingredient_number1 / ingredient1people
			ingredient2end = ingredient_number2 / ingredient1people
			ingredient3end = ingredient_number3 / ingredient1people
			ingredient4end = ingredient_number4 / ingredient1people

		print(" ")
		print ("--------------------------------------------------")
		print ("Recipe Name:", recipe_name)
		print ("Ingredient(s) Name:", ingredient_1,",",ingredient_2,",",ingredient_3,",",ingredient_4)
		print ("Amount Of Ingredient(s):", ingredient1end,units1,",",ingredient2end,units2,",",ingredient3end,units3,",",ingredient4end,units4)
		print ("Serves:", ingredient1final, "people")
		print ("--------------------------------------------------")
		print(" ")

	if ingredient_number == 5:
		ingredient_1 = str(input("What is the first ingredient? "))
		ingredient_number1 = float(input("How much of the ingredient is there? "))
		units1 = str(input("What are the units for the ingredient? "))

		ingredient1people = int(input("How many people does it serve? "))
		ingredient1final = int(input("How many people should it serve? "))

		ingredient_2 = str(input("What is the second ingredient? "))
		ingredient_number2 = float(input("How much of the ingredient is there? "))
		units2 = str(input("What are the units for the ingredient? "))

		ingredient_3 = str(input("What is the third ingredient? "))
		ingredient_number3 = float(input("How much of the ingredient is there? "))
		units3 = str(input("What are the units for the ingredient? "))

		ingredient_4 = str(input("What is the fourth ingredient? "))
		ingredient_number4 = float(input("How much of the ingredient is there? "))
		units4 = str(input("What are the units for the ingredient? "))

		ingredient_5 = str(input("What is the fifth ingredient? "))
		ingredient_number5 = float(input("How much of the ingredient is there? "))
		units5 = str(input("What are the units for the ingredient? "))

		if ingredient1final > ingredient1people:
			ingredient1end1 = ingredient1final * ingredient_number1
			ingredient1end = ingredient1end1 / ingredient1people
			ingredient2end2 = ingredient1final * ingredient_number2
			ingredient2end = ingredient2end2 / ingredient1people
			ingredient3end3 = ingredient1final * ingredient_number3
			ingredient3end = ingredient3end3 / ingredient1people
			ingredient4end4 = ingredient1final * ingredient_number4
			ingredient4end = ingredient4end4 / ingredient1people
			ingredient5end5 = ingredient1final * ingredient_number5
			ingredient5end = ingredient5end5 / ingredient1people

		if ingredient1final < ingredient1people:
			ingredient1end = ingredient_number1 / ingredient1final
			ingredient2end = ingredient_number2 / ingredient1final
			ingredient3end = ingredient_number3 / ingredient1final
			ingredient4end = ingredient_number4 / ingredient1final
			ingredient5end = ingredient_number5 / ingredient1final

		if ingredient1final == 1:
			ingredient1end = ingredient_number1 / ingredient1people
			ingredient2end = ingredient_number2 / ingredient1people
			ingredient3end = ingredient_number3 / ingredient1people
			ingredient4end = ingredient_number4 / ingredient1people
			ingredient5end = ingredient_number5 / ingredient1people

		print(" ")
		print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
		print ("Recipe Name:", recipe_name)
		print ("Ingredient(s) Name:", ingredient_1,",",ingredient_2,",",ingredient_3,",",ingredient_4,",",ingredient_5)
		print ("Amount Of Ingredient(s):", ingredient1end,units1,",",ingredient2end,units2,",",ingredient3end,units3,",",ingredient4end,units4,",",ingredient5end,units5)
		print ("Serves:", ingredient1final, "people")
		print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
		print (" ")

	if ingredient_number == 6:
		ingredient_1 = str(input("What is the first ingredient? "))
		ingredient_number1 = float(input("How much of the ingredient is there? "))
		units1 = str(input("What are the units for the ingredient? "))

		ingredient1people = int(input("How many people does it serve? "))
		ingredient1final = int(input("How many people should it serve? "))

		ingredient_2 = str(input("What is the second ingredient? "))
		ingredient_number2 = float(input("How much of the ingredient is there? "))
		units2 = str(input("What are the units for the ingredient? "))

		ingredient_3 = str(input("What is the third ingredient? "))
		ingredient_number3 = float(input("How much of the ingredient is there? "))
		units3 = str(input("What are the units for the ingredient? "))

		ingredient_4 = str(input("What is the fourth ingredient? "))
		ingredient_number4 = float(input("How much of the ingredient is there? "))
		units4 = str(input("What are the units for the ingredient? "))

		ingredient_5 = str(input("What is the fifth ingredient? "))
		ingredient_number5 = float(input("How much of the ingredient is there? "))
		units5 = str(input("What are the units for the ingredient? "))

		ingredient_6 = str(input("What is the sixth ingredient? "))
		ingredient_number6 = float(input("How much of the ingredient is there? "))
		units6 = str(input("What are the units for the ingredient? "))

		if ingredient1final > ingredient1people:
			ingredient1end1 = ingredient1final * ingredient_number1
			ingredient1end = ingredient1end1 / ingredient1people
			ingredient2end2 = ingredient1final * ingredient_number2
			ingredient2end = ingredient2end2 / ingredient1people
			ingredient3end3 = ingredient1final * ingredient_number3
			ingredient3end = ingredient3end3 / ingredient1people
			ingredient4end4 = ingredient1final * ingredient_number4
			ingredient4end = ingredient4end4 / ingredient1people
			ingredient5end5 = ingredient1final * ingredient_number5
			ingredient5end = ingredient5end5 / ingredient1people
			ingredient6end6 = ingredient1final * ingredient_number6
			ingredient6end = ingredient6end6 / ingredient1people

		if ingredient1final < ingredient1people:
			ingredient1end = ingredient_number1 / ingredient1final
			ingredient2end = ingredient_number2 / ingredient1final
			ingredient3end = ingredient_number3 / ingredient1final
			ingredient4end = ingredient_number4 / ingredient1final
			ingredient5end = ingredient_number5 / ingredient1final
			ingredient6end = ingredient_number6 / ingredient1final

		if ingredient1final == 1:
			ingredient1end = ingredient_number1 / ingredient1people
			ingredient2end = ingredient_number2 / ingredient1people
			ingredient3end = ingredient_number3 / ingredient1people
			ingredient4end = ingredient_number4 / ingredient1people
			ingredient5end = ingredient_number5 / ingredient1people
			ingredient6end = ingredient_number6 / ingredient1people


		print(" ")
		print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
		print ("Recipe Name:", recipe_name)
		print ("Ingredient(s) Name:", ingredient_1,",",ingredient_2,",",ingredient_3,",",ingredient_4,",",ingredient_5,",",ingredient_6)
		print ("Amount Of Ingredient(s):", ingredient1end,units1,",",ingredient2end,units2,",",ingredient3end,units3,",",ingredient4end,units4,",",ingredient5end,units5,",",ingredient6end,units6)
		print ("Serves:", ingredient1final, "people")
		print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
		print (" ")





		
