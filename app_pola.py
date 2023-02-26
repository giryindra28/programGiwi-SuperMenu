
class pola_bintang:
    def __init__ (self,value_1):
        self.value_1 = value_1
    
    def persegi_bintang(self):
        for i in range(self.value_1):
            for j in range(self.value_1):
                print("*",end=" ")
            print()

    def segitiga_bintang(self):
        for i in range(1,self.value_1 + 1):
            for j in range(i):
                print("*", end=" ")
            print()

    def segitiga_tebalik(self):
        for i in range(self.value_1 ):
            for j in range(1,self.value_1-i+1):
                print("*", end=" ")
            print()    

    def piramida(self):
        for i in range(1,self.value_1+1):
            for j in range(self.value_1-i):
                print(" ",end="")
            for k in range(i):
                print(" *",end="")
            print()

    def piramida_tebalik(self):
        for i in range(self.value_1):
            for j in range(i):
                print(" ",end="")
            for k in range(self.value_1-i):
                print(" *",end="")
            print()
    
    def belah_ketupat(self):
        for i in range(self.value_1):
            for j in range(self.value_1-i):
                print(" ",end="")
            for k in range(i):
                print(" *",end="")
            print()
        
        for i in range(self.value_1):
            for j in range(i):
                print(" ",end="")
            for k in range(self.value_1-i):
                print(" *",end="")
            print()

class sub_bintang(pola_bintang):
    def __init__ (self,value_1,value_2):
        pola_bintang.__init__(self,value_1)
        self.value_2 = value_2
    
    def persegi_panjang(self):
        for i in range(self.value_1):
            for j in range(self.value_2):
                print("*",end=" ")
            print()

