def fibonaci(n):
    a = 0
    b = 1
    c = 0
    print "start"
    for i in range(n):
        c = a + b
        a = b
        b = c
        
        print "Fibonaci"
        print 'i-->',i,'c===>',c
        print "end"
        print "test"
        

if __name__ == '__main__':
    fibonaci(10)
    
        

