def Outer():
    X=10
    def Inner():
        nonlocal X
        X +=5
        print("Inner X",X)
        
    Inner()
    print("Outer X",X)
    
Outer()