    #opening the template
with open("./Input/Names/invited_names.txt", mode="r") as names:
    list_of_names = names.readlines()
    #creating the letter
with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
        letter_list = letter.read()
        for name in list_of_names:
            new_name = name.rstrip()
            new_letter = letter_list.replace("[name]", new_name)
            # saving the leter with individual name
            with open(f"./Output/ReadyToSend/letter_to_{new_name}.txt", mode="w") as complete_letter: 
                complete_letter.write(new_letter)
