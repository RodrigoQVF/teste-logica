def fibonnaci(numero):
    fibo = [1]
    before = 1
    after = 1
    for i in range(10000):
        fibo.append(after)
        after, before = after + before, after
    if numero in fibo:
        print(f"O numero {numero} pertence fibonnaci")
    else:
        print(f"O numero {numero} nao pertence fibonacci")


fibonnaci(1367)
