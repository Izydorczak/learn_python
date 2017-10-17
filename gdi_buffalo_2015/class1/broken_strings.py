

#Fix this paragraph so that the line print(paragraph) at the end will print the paragraph
#with all the groots capitalized and the first letter of each sentence capitalized. 

# print(paragraph) should give us the original paragraph, with all the groots capitalized
paragraph = "i am groot. yeah we know who you are. i am groot. yeah, you just said that.I wasn't retrieving the orb for Ronan. I was betraying him. i am groot. well that's just as fascinating as the first 89 times you said that."

print("What follows is the paragraph with all the groots capitalized:\n ",paragraph.replace('groot', 'Groot'))

print ("\n\nWhat follows should still be the paragraph with all the groots capitalized:\n ", paragraph)

# split the paragraph into a list of sentences

par_list = paragraph.split('.')
print("\n\nThis is the paragraph split into a list:\n",par_list)

#The empty sentence at the end causes a key error. You will need to remove it.

# This loop will capitalize each sentence

for sentence of par_list:
  sentence = sentence.lstrip()  #remove space before sentence
  sentence_list = list(sentence  #turn sentence into a list to make it mutable 
  sentence_list[0]= sentence_list[0].upper  #capitalize the first letter
  sentence = "".join(sentence_list)   #rejoin sentence
  par_list_new.append(sentence)


print("\n\nHere is the fixed paragraph:\n",paragraph)
