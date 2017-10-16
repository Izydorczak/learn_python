paragraph = "i am groot. yeah we know who you are. i am groot. yeah you just said that. i wasn't retrieving the orb for ronan, i was betraying him. i am groot. well that's just as fascinating as the first eighty-nine times you told me that." 

print(paragraph.replace('groot', 'Groot'))


print (paragraph)

paragraph = paragraph.replace('groot','Groot')



# let's try to captialize the sentences using the capitalize() function.
# In the end, print the original paragraph with proper capitalization.

par_list = paragraph.split('.')
print(par_list)

par_list_new=[]

#find the first letter of the sentence
for sentence in par_list:
  sentence = sentence.lstrip()
  sentence = sentence.capitalize()
  print(sentence)
  par_list_new.append(sentence)

print(par_list_new)
paragraph = (' ').join(par_list_new)
print(paragraph)
