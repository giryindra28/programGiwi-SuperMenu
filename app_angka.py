
class angka():
    def __init__ (self,value_1):
        self.value_1 = value_1
    
    def persegi(self):
        for i in range(1,self.value_1+1):
            for j in range(self.value_1):
                print(i,end=" ")
            print()

    def persegi_deret(self):
        k = 1
        for i in range(self.value_1):
            for j in range(self.value_1):
                print(k, end=" ")
                k+=1
            print()
    
    def segitiga_angka(self):
        for i in range(1,self.value_1+1):
            for j in range(1,i+1):
                print(j, end=" ")
            print()
    
    def segitiga_deret(self):
        k=1
        for i in range(1,self.value_1+1):
            for j in range(1,i+1):
                print(k,end=" ")
                k+=1
            print()

    def segitiga_terbalik(self):
        for i in range(1,self.value_1+1):
            for j in range(self.value_1-i+1):
                print(i,end=" ")
            print()
    
    def deret_A(self):
        for i in range(1,self.value_1+1):
            i*=3
            print(i,end=" ")
        print()
    
    def deret_B(self):
        for i in range(1,self.value_1+1):
            print(i**2,end=" ")
        print()
    
    def faktorial(self):
        k = 1
        print(f"{self.value_1}! = ",end="")
        for i in range(1,self.value_1+1):
            k*=i
            print(f"{i} * ", end="")
        print(f" = {k}",end="")
    
    def deret_genap(self):
        for i in range(1,self.value_1+1):
            print(i*2, end=" ")
        print()

    def deret_ganjil(self):
        for i in range(1,self.value_1+1):
            print(i*2-1, end=" ")
        print()

class deret_angka(angka):
    def __init__ (self,value_1,value_2):
        angka.__init__(self,value_1)
        self.value_2 = value_2
    
    def deret_genap_withRange(self):
        for i in range(self.value_1, self.value_2+1):
            if i%2==0:
                print(i,end=" ")
        print()

    def deret_ganjil_withRange(self):
        for i in range(self.value_1,self.value_2+1):
            if i%2!=0:
                print(i,end=" ")
        print()

    

    