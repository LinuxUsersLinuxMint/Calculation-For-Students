#!/usr/bin/python3
"Copyright© 2023 LinuxUsersLinuxMint"
"Python Calculation For Students Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır."
"Python Calculation For Students All Rights Reserved under the GPL(General Public License)."
"Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"
"A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"

okulturu=str(input('Okul Türünüzü Giriniz (Ortaokul/Lise): '))
islem=str(input('Yapmak İstediğiniz İşlemi Seçiniz: '))

if islem=="yazılıort":
    yz1=float(input('1.Yazılı Notunuzu Giriniz: '))
    yz2=float(input('2.Yazılı Notunuzu Giriniz: '))
    ortsonuc=yz1+yz2/2
    print("Yazılı Ortalamanız: {0}". format(ortsonuc))
elif islem=="ortsnf":
    yzort=float(input('Yazılı Ortalamanızı Giriniz: '))
    if yzort >= 50:
        print("Yazılı Ortalamanız 50'den Yüksek Sınıfı Geçtiniz")
    else:
        print("Üzgünüm Yazılı Ortalamanız 50'den Düşük Sınıfı Geçemediniz...")
        print("Ancak Üzülmeyin Her Zaman Daha iyisini Yapabilirsiniz.\n")
elif islem=="about":
    print("Calculation For Students v1.0 (Son Güncellemne tarihi 9 , Eylül , 2023 , 17:33)")
else:
    print("Geçersiz İşlem veya işlem girilmedi...")