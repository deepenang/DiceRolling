
#OUTPUT JIKA MAHU BERMAIN DADU

def Dadu(baling):
   
    while baling == "y" or baling == "Y":

            print("\n\t\t******************************")
            print("\n\t\t......Dadu sedang diputarkan......")

            time.sleep(2.5)
            #Paparkan Nilai Dadu Pertama secara rawak

            print("\n\t\tNilai Dadu Pertama :",random.randint(nilai_min, nilai_max))

            #Paparkan Nilai Dadu Kedua secara rawak

            print("\n\t\tNilai Dadu Kedua :",random.randint(nilai_min, nilai_max))

            print("\n\t\t******************************")

            #Pengguna memilih nak teruskan balingan dadu atau tidak
    
            baling = input("\n\t\tAdakah anda ingin membaling Dadu lagi (Y / N)? ")


#Declare pembolehubah/variable
import time
import random

nilai_min = 1
nilai_max = 6
baling = None

# Tajuk PERMAINAN
print("\n\t*****SELAMAT DATANG KE PERMAINAN DADU******")

#INPUT
baling = input("\n\t\tAdakah anda ingin membaling Dadu? ")


#CALL Function Dadu dan hantar argument baling samada Yes atau No
Dadu(baling)
print("\n\t\t......Terima Kasih kerana Bemain Dadu.....\n\t\t\t......Sampai Jumpa Lagi......")
