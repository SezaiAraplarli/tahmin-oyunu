import random
import time
kurallar = (input("Sayı tahmin oyununa hoşgeldin,istiyorsan sana kuralları özetliyeyim.İstiyorsan 'olur' istemiyorsan 'let the game begin' de!"))
while True :
    hak=30
    puan=0
    if kurallar=="olur":
        print("Kurallar şöyle:")
        time.sleep(1)
        print("1)420 puana ulaşırsan kazanırsın.")
        time.sleep(1.35)
        print("2)Toplam 30 hakkın var . Dikkatli kullan!")
        time.sleep(2)
        print("3)Sayılar 1 ile 20 arasında tutulacaktır.")
        time.sleep(1.20)
        print("4)Bu aralıktan büyük veya küçük bir sayı girersen olan senin haklarına olacak.")
        time.sleep(3)
        print("5)Her tahmininde 70 puan alacaksın.")
        time.sleep(2)
        print("6)Her bilemediğinde hakkın 1 azalacak.")
        time.sleep(2)
        print("Kurallar bu kadar , İyi eğlenceler !")
        time.sleep(2)
        while True:
            print("Sayı tutuluyor...")
            print("-__-__-__-__-__-__-")
            time.sleep(1)
            tutulan_sayi=random.randint(1,20)
            girilen_sayi=int(input("Ee hangi sayıyı tuttum?"))
            if girilen_sayi==tutulan_sayi:
                puan=puan+70
                print("hll bildin")
                print("Puanın =",(puan))
                print("Kalan hakkın =", (hak))
            elif girilen_sayi!=tutulan_sayi:
                hak=hak-1
                print("dostum ... üzdün , tuttuğum sayı",tutulan_sayi,"idi")
                print("Puanın =",(puan))
                print("Kalan hakkın =",(hak))
            elif hak==0:
                print("such a looser")
                break
            elif puan==420:
                print("Tebrikler oyunu kazandın!")
                break
    elif kurallar=="let the game begin":
        while True:
            print("Sayı tutuluyor...")
            print("-__-__-__-__-__-__-")
            time.sleep(1)
            tutulan_sayi=random.randint(1,20)
            girilen_sayi=int(input("Ee hangi sayıyı tuttum?"))
            if girilen_sayi==tutulan_sayi:
                puan=puan+70
                print("hll bildin")
                print("Puanın =",(puan))
                print("Kalan hakkın =", (hak))
            elif girilen_sayi!=tutulan_sayi:
                hak=hak-1
                print("dostum ... üzdün , tuttuğum sayı",tutulan_sayi,"idi")
                print("Puanın =",(puan))
                print("Kalan hakkın =",(hak))
            elif hak==0:
                print("such a looser")
                break
            elif puan==420:
                print("Tebrikler oyunu kazandın!")
                break
    else:
        print("Ne Dediğini anlayamadım")
        break
