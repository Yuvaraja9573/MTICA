#use dictionary comprehension
#to count the length of each word in a sentence.

string='''
practice problems for list com pre hension in python.
'''
wordslst=string.split(' ')
print(wordslst)
wordslst=[i.strip("\n")for i in wordslst]
print(wordslst)
ans={i:len(i)for i in wordslst}
print(ans)



