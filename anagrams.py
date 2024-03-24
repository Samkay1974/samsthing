def is_anagram(x,y):
    x =x.upper().replace(" ","").replace(',','')
    y = y.upper().replace(" ","").replace(',','')
    if len(x)!= len(y):
        print("Words must have the same length")
    
    sorted_x = sorted(x)
    sorted_y = sorted(y)
    if sorted_x == sorted_y:
        print("They are anagrams")
    else:
        print("Fuck off, they ain't anagrams")
is_anagram("L I S T,E,N","silent")