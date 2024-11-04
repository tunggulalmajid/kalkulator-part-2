import os 
import termcolor

def clear ():
    os.system("cls")

def garis ():
    print ("="*50)

def garis2 ():
    print ("-"*50)

def cover (a):
    garis()
    print ("KALKULATOR".center(50))
    garis2()
    print (a.center(50))
    garis()

def enter ():
    enter =  input ("Tekan Enter untuk melanjutkan >> ")

def main ():
    clear()
    cover ("HALAMAN UTAMA")
    print ("""
    Menu :
            1. Kalkulator Pertambahan
            2. Kalkulator Pengurangan
            3. Kalkulator Perkalian
            4. Kalkulator Pembagian
            5. Bilangan Faktorial 
""")
    garis()
    while True :
        try :
            pilih = int (input("Pilih Opsi >> "))
            if pilih == 1 :
                enter()
                pertambahan()
                break
            elif pilih == 2 :
                enter()
                pengurangan()
                break
            elif pilih == 3 :
                enter()
                perkalian()
                break
            elif pilih == 4 :
                enter()
                pembagian ()
                break
            elif pilih == 5 :
                enter()
                faktorial()
            else :
                raise ValueError ("Opsi yang anda pilih tidak tersedia...")
        except ValueError as error :
            termcolor.cprint (error, "red")

def pertambahan ():
    clear ()
    cover ("PERTAMBAHAN")    
    tampungan = []
    a = 0
    while True :
        while True :
            try:
                num = int (input ("masukkan angka >>"))
                break
            except ValueError :
                print ("hanya angka yang di masukkan ")
                continue

        a += num
        tampungan.append(num)
        while True:
            try :
                tambah = input ("ingin menambahkan angka lagi ? [y]/[n] >>")
                if tambah.lower() != "y" and tambah.lower() != "n":
                    raise ValueError ("inputan tidak valid")
                else :
                    break
            except ValueError as error :
                print (error)
                continue    
        if tambah == "y":
            continue
        elif tambah == "n":
            break
      

    print ("\nHASIL DARI :")
    for i in range  (len(tampungan)):
        if i < (len(tampungan)-1):
            print (tampungan[i],end=" + ", )
        elif i == (len(tampungan)-1):
            print (tampungan[i]," = ", a, end ="")
    print (" ")
    enter()
    main()

def pengurangan ():
    clear ()
    cover ("PENGURANGAN")    
    tampungan = []
    a = int (input ("masukkan angka pertama >>"))
    tampungan.append(a)
    while True :
        while True :
            try:
                num = int (input ("masukkan angka sebagai pengurang >>"))
                break
            except ValueError :
                print ("hanya angka yang di masukkan ")
                continue

        a -= num
        tampungan.append(num)
        while True:
            try :
                tambah = input ("ingin menambahkan angka lagi ? [y]/[n] >>")
                if tambah.lower() != "y" and tambah.lower() != "n":
                    raise ValueError ("inputan tidak valid")
                else :
                    break
            except ValueError as error :
                print (error)
                continue    
        if tambah == "y":
            continue
        elif tambah == "n":
            break
      

    print ("\nHASIL DARI :")
    for i in range  (len(tampungan)):
        if i < (len(tampungan)-1):
            print (tampungan[i],end=" - ", )
        elif i == (len(tampungan)-1):
            print (tampungan[i]," = ", a, end ="")
    print (" ")
    enter()
    main()

def perkalian ():
    clear ()
    cover ("PERKALIAN")    
    tampungan = []
    a = int (input ("masukkan angka pertama >>"))
    tampungan.append(a)
    while True :
        while True :
            try:
                num = int (input ("masukkan angka sebagai pengali >>"))
                break
            except ValueError :
                print ("hanya angka yang di masukkan ")
                continue

        a *= num
        tampungan.append(num)
        while True:
            try :
                tambah = input ("ingin menambahkan angka lagi ? [y]/[n] >>")
                if tambah.lower() != "y" and tambah.lower() != "n":
                    raise ValueError ("inputan tidak valid")
                else :
                    break
            except ValueError as error :
                print (error)
                continue    
        if tambah == "y":
            continue
        elif tambah == "n":
            break
      

    print ("\nHASIL DARI :")
    for i in range  (len(tampungan)):
        if i < (len(tampungan)-1):
            print (tampungan[i],end=" * ", )
        elif i == (len(tampungan)-1):
            print (tampungan[i]," = ", a, end ="")
    print (" ")
    enter()
    main()
def pembagian ():
    clear ()
    cover ("PEMBAGIAN")    
    tampungan = []
    a = int (input ("masukkan angka pertama >>"))
    a = f"{a:.2f}"
    tampungan.append(a)
    while True :
        while True :
            try:
                num = int (input ("masukkan angka sebagai pembagi >>"))
                break
            except ValueError :
                print ("hanya angka yang di masukkan ")
                continue

        a /= num
        tampungan.append(num)
        while True:
            try :
                tambah = input ("ingin menambahkan angka lagi ? [y]/[n] >>")
                if tambah.lower() != "y" and tambah.lower() != "n":
                    raise ValueError ("inputan tidak valid")
                else :
                    break
            except ValueError as error :
                print (error)
                continue    
        if tambah == "y":
            continue
        elif tambah == "n":
            break
      

    print ("\nHASIL DARI :")
    for i in range  (len(tampungan)):
        if i < (len(tampungan)-1):
            print (tampungan[i],end=" / ", )
        elif i == (len(tampungan)-1):
            print (tampungan[i]," = ", a, end ="")
def faktorial ():
    clear()
    cover("FAKTORIAL")
    fakto = int (input ("masukkan angka yang  ingin di hitung faktorialnya >>"))
    hasil = fakto
    for i in range (1, fakto):
        hasil *= i
    print (f"HASIL DARI {fakto}! = {hasil}")
    pilih = (input ("apakah ingin kembali ke menu ? [y]/[n]"))
    if pilih.lower() == "y":
        enter()
        main ()
    elif pilih.lower() == "n":
        enter()
        faktorial()

if __name__ == "__main__":
    main()