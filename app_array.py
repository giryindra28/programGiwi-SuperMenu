
class arrayy():
    def __init__ (self,value_1):
        self.value_1 = value_1
       

    def find_max(self):
        print("")
        list_1 = []
        print(f"Input {self.value_1} angka (dipisah dengan enter): ")
        for i in range(1,self.value_1+1):
            print(f"Angka ke-{i}: ",end=" ")
            list_1.append(int(input()))
        result = max(list_1)
        print("")
        print("Angka terbesar adalah: ",result)
    
    def find_min(self):
        print("")
        list_1 = []
        print(f"Input {self.value_1} angka (dipisah dengan enter): ")
        for i in range(1,self.value_1+1):
            print(f"Angka ke-{i}: ",end=" ")
            list_1.append(int(input()))
        result = min(list_1)
        print("")
        print("Angka terkecil adalah: ",result)
    
    def find_sum(self):
        print("")
        list_1 = []
        print(f"Input {self.value_1} angka (dipisah dengan enter): ")
        for i in range(1,self.value_1+1):
            print(f"Angka ke-{i}: ",end=" ")
            list_1.append(int(input()))
        result = sum(list_1)
        print("")
        print(f"total penjumlahan dari {self.value_1} angka tersebut adalah: ",result)
    
    def find_avg(self):
        print("")
        list_1 = []
        print(f"Input {self.value_1} angka (dipisah dengan enter): ")
        for i in range(1,self.value_1+1):
            print(f"Angka ke-{i}: ",end=" ")
            list_1.append(int(input()))
        result = sum(list_1) / len(list_1)
        print("")
        print(f"total rata-rata dari {self.value_1} angka tersebut adalah: " ,round(result,2))
    


    def find_array(self):
        print("")
        list_1 = []
        print(f"Input {self.value_1} angka (dipisah dengan enter): ")
        for i in range(1,self.value_1+1):
            print(f"Angka ke-{i}: ",end=" ")
            list_1.append(int(input()))
        print("")
        num_2 = int(input("Input angka yang ingin dicari: "))
        for i in range(self.value_1+1):
           if list_1[i] == num_2:
            print("Angka ditemukan pada urutan ke ", i+1)
            break
        if(i+1 == self.value_1):
            print('Angka tidak ditemukan')

     

