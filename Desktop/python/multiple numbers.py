'''
print number from 1 to 100, if number is multiple of 3 then print "tecno"
and the number is multiple of 5 then print "soft" and if the number is
multiple of 3 and 5 then print "tecnosoft"

accept 5 numbers and find sum of five numbers and avg of five numbers

'''




for i in range(1,101):
    
    if i%3==0 and i%5==0:
        print(i,": tecnosoft")
    elif i%3==0:
        print(i,": tecno")
    elif i%5==0:
        print(i,": soft")
    else:
        print(i)
    
        
        
