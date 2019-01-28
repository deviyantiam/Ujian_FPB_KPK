angka1=int(input('Ketik angka pertama     : '))
angka2=int(input('Ketik angka kedua       : '))
def fpb(bil1,bil2):
    if angka1 > angka2:
        kecil = angka2
    else:
        kecil = angka1
    for i in range(1, kecil+1): #dibagi dimulai dari 1 sampai variabel 'kecil'
        if((angka1 % i == 0) and (angka2 % i == 0)):
            fpb_ = i  #akan berubah menjadi bilangan yang paling besar yang merupakan dari faktor keduanya 
    return fpb_
print('FPB dari',angka1,'dan',angka2,'adalah =',fpb(angka1,angka2))
def kpk(bil1,bil2):
    pengali1=1
    pengali2=1
    kel1=bil1*pengali1 #kelipatan bil1
    kel2=bil2*pengali2 #kelipatan bil2
    while kel1!=kel2:
        while kel1>kel2:
            pengali2+=1
            kel2=bil2*pengali2
        while kel1<kel2:
            pengali1+=1
            kel1=bil1*pengali1
    if kel1==kel2:
        print('KPK dari',bil1,'dan',bil2,'adalah =',kel1)
kpk(angka1,angka2)



