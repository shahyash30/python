str = input("enteer the message: ")
coding = input("1 for encryption and 2 for decryption : ")
words = str.split(" ")
if(coding =="1"):
    coding = True 
else:
    coding = False

if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            rand1 = "yash"
            rand2 = "yash"
            strnew = rand1 + word[:-1] + word[0] + rand2
            nwords.append(strnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            strnew = word[3:-3]
            strnew = strnew[-1] + strnew[:-1]
            nwords.append(strnew)
        else:
            nwords.append(words[::-1])
    print(" ".join(nwords))


