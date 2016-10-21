word=input('Word: ')
s=0;w=0
while w<len(word):
    print(word[0:len(word)+s])
    s=s-1
    w+=1
    
