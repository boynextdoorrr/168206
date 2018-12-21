for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if((not a)+(d)+(b)+(not d)==1 and a+b+c+d==1):
                    if a==1:
                        print ("小偷是A")
                        if b==1:
                            print ("小偷是B")
                            if c==1:
                                print ("小偷是C")
                                if d==1:
                                    print ("小偷是D")
