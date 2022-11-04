x=input()
if len(x)%2==1:
    x=x
else:
    if "." in x:
        x=x.replace(".","")
    else:
        x=x+"."    
word=x 
k=len(word)
l=int(k/2)
print(word[l-1:l+2])
