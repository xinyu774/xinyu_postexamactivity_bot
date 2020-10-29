print("Title of program: Post Exam Activity bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("that that's nice")
      counter -= 1
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("find something meaningful to do")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("get some rest")
      counter += 1
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("cheer up as there would always be sunshine after the rain")
      counter += 1
    if each_word == "relaxed":
      feelings_list.append("relaxed")
      encouragement_list.append("to not let your guard down too easily")
      counter -= 1
    if each_word == "frustrated":
      feelings_list.append("frustrated")
      encouragement_list.append("cool down for a while and ask help if needed")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember to "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "" + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "" + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
