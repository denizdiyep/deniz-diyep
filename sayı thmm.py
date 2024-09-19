import random

def sayi_tahmin_oyunu():
    print("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin?")
    rastgele_sayi = random.randint(1, 100)
    tahmin_sayisi = 0

    while True:
        tahmin = input("Tahmininizi girin: ")
        
        # Tahminin sayı olup olmadığını kontrol ediyoruz
        if not tahmin.isdigit():
            print("Lütfen bir sayı girin!")
            continue
        
        tahmin = int(tahmin)
        tahmin_sayisi += 1
        
        if tahmin < rastgele_sayi:
            print("Daha büyük bir sayı söyleyin.")
        elif tahmin > rastgele_sayi:
            print("Daha küçük bir sayı söyleyin.")
        else:
            print(f"Tebrikler! {tahmin_sayisi} denemede doğru tahmini yaptınız.")
            break

sayi_tahmin_oyunu()
