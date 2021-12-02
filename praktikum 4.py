a = 0
Nama = []
NIM = []
Tugas = []
UTS = []
UAS = []
NilaiAkhir = []

while True :
    Nama1=input("Nama   : ")
    Nama.append(Nama1)
    NIM1=input("NIM     : ")
    NIM.append(NIM1)
    Tugas1=input("Nilai Tugas  : ")
    Tugas.append(Tugas1)
    UTS1=input("Nilai UTS   : ")
    UTS.append(UTS1)
    UAS1=input("Nilai UAS   : ")

    NilaiAkhir1=(int(Tugas1)*0.30)+(int(UTS1)*0.35)+(int(UAS1)*0.35)
    NilaiAkhir.append(NilaiAkhir1)

    more=""
    while more!="y" and more!="t" :
        more=input("Tambah Data(y/t) ?")
    a+=1
    if more=="t" :
        break

print(".__________________________________________________________________________.")
print("|                          Daftar Mahasiswa                                          |")
print("|__________________________________________________________________________|")
print("|  No. |    Nama  |   NIM   |   Tugas  |   UTS  |   UAS   |  Tugas Akhir   |")
print("|--------------------------------------------------------------------------|")
for n in range(a) :
     print ("| ",n+1,"  | ",Nama[n],"  | ",NIM[n]," | ",Tugas[n],"  |  ",UTS[n],"  | ",UAS[n]," |  ",NilaiAkhir[n]," |")