import threading

class Cube:
    def vol(self,a):
        print("Cube volume is: ")
        print(a*a*a)

    def side_length(self,a):
        print('\n')
        print("Cube sides length is: ")
        print(12*a)


c1 = Cube()
c2 = Cube()

if __name__ == "__main__": 
    
    t1 = threading.Thread(target=c1.side_length, args=(1,))
    t2 = threading.Thread(target=c1.vol, args=(1,))

    t3 = threading.Thread(target=c2.side_length, args=(2,))
    t4 = threading.Thread(target=c2.vol, args=(2,))

    t1.start()
    t1.join()
    t2.start()
    t2.join()

    t3.start()
    t3.join()
    t4.start()
    t4.join()

    
   
    


    
