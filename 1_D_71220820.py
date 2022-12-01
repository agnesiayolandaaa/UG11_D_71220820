def bioskop ():
    print ("Halo selamat datang di bioskop!")
    print ("Dimanakah kamu ingin menonton?")
    print ("1) XXI Empire")
    print ("2) XXI Amplaz")
    print ("3) XXI JCM")

    bioskop= int(input("Masukkan pilihanmu"))
    if (bioskop>3):
        print ("Pilihan tak tersedia")
        exit ()

    print ("Mau nonton film apa nih? Ada film")
    print ("1. Frozen ")
    print ("2. Keramat")
    print ("3. KKN di Desa Penari")
    namafilm= int(input("Pilih no film"))
    if (namafilm>3):
        print ("Pilihan tidak tersedia")
        exit()

    print ("Mau nonton layar bioskop apa")
    print ("1. Reguler ")
    print ("2. Dolby Almos")
    print ("3. Premiere")
    tipelayar= int(input("Pilihan nomor tipe layar"))
    if (tipelayar>3):
        print ("Pilihan tidak tersedia")
        exit()

    banyaktiket= int(input("Berapa banyak tiket"))

    print ("Mau nonton layar bioskop apa")
    pilihan1= ("12.35")
    pilihan2= ("14.45")
    pilihan3= ("16.55")
    pilihan4= ("19.05")

    print ("1. " , pilihan1 )
    print ("2. " , pilihan2 )
    print ("3. " , pilihan3 )
    print ("4. " , pilihan4 )

    pilihan= int(input("Masukkan angka pilihan anda"))
    if (pilihan==1) :
        print("Oke berhasil!, Silahkan dinikmati di jam", pilihan1)
    elif (pilihan==2) :
        print("Oke berhasil!, Silahkan dinikmati di jam", pilihan2)
    elif (pilihan==3) :
        print("Oke berhasil!, Silahkan dinikmati di jam", pilihan3)
    elif (pilihan==4) :
        print("Oke berhasil!, Silahkan dinikmati di jam", pilihan4)
    else:
        print ("Pilihan tidak ada")

bioskop()