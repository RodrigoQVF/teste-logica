def inverteString(string):
    i = 0
    tamMax = len(string)
    novaString = []
    j = tamMax - 1
    for i in range (tamMax):
        novaString.append(string[j])
        j-= 1
    print(novaString)
    


inverteString("palavra")
