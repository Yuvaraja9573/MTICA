#reverse of a dictionary words
string='''
practice problems for list com pre hension in python.
'''
wordslst=string.split(' ')
#print(wordslst)
wordslst=[i.strip("\n")for i in wordslst]
#print(wordslst)
ans={i:i[::-1]for i in wordslst}
print(ans)
