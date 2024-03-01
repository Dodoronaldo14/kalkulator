def Penjumlahan (a,b):
    return a+b
def Pengurangan (a,b):
    return a-b
def Perkalian (a,b):
    return a*b
def Pembagian (a,b):
    if b ==0:
        return "error nilai pembagian dengan angka 0 tidak valid"
    return a/b

        
while True:
    print ("\n	===			SELAMAT DATANG 				===")
    print ("	===		  DI APLIKASI KALKULATOR RNLD			===")
    print ("")
    print ("")
    a = int(input("	masukan angka pertama:"))
    b = int(input("	masukan angka kedua:"))
    print ("	1. Penjumlahan")
    print ("	2. Pengurangan")
    print ("	3. Perkalian")
    print ("	4. Pembagian")
    print ("	5. Keluar")
    pilihan = input ("	PILIH OPSI YANG ANDA INGINKAN 1/2/3/4/5 :")


    if pilihan == ("1"):
        hasil = Penjumlahan (a,b)
        print ("	ANDA MEMILIH PENJUMLAHAN [+]")
        print ("	HASIL PENJUMLAHAN DARI",a,"+",b,"=",(hasil))
    elif pilihan == ("2"):
        hasil = Pengurangan (a,b)
        print ("	ANDA MEMILIH PENGURANGAN[-]")
        print ("	HASIL PENGURANGAN DARI",a,"-",b,"=",(hasil))
    elif pilihan == ("3"):
        hasil = Perkalian (a,b)
        print ("	===		ANDA MEMILIH PERKALIAN[*]")
        print ("	HASIL PERKALIAN DARI",a,"*",b,"=",(hasil))
    elif pilihan == ("4"):
        hasil = Pembagian (a,b)
        print ("	===		ANDA MEMILIH PEMBAGIAN[/]")
        print ("	HASIL PEMBAGIAN DARI",a,"/",b,"=",(hasil))
    elif pilihan == ("5"):
        print ("	===			ANDA TELAH KELUAR			===")
        print ("	===	TERIMAKASIH TELAH MENGGUNAKAN PROGRAM SAYA		===")
        break
else:
    print("input tidak aktif")
        

        