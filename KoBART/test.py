
def asfd(q, w, abc=0):
    print(q, w, abc)
    abc += 1
    return abc
    

ab=0

for i in range(50):
    abc = asfd('q','w', abc=ab)