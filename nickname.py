import random
def main():
    data_list = []  # Boş bir liste

    while True:
        item = input("Bir öğe girin (Karışıma hazır hissettiğinizde L basın): ").upper()
        
        if item == 'L':
            break  # Döngü Sonlandırıcı

        data_list.append(item)  # Kullanıcıdan Alınan Veri

    print("Girilen Nick Name'ler:")
    for item in data_list:
        print(item)

    soru = input("Hazır mısınız? (Karışım için E basın): ").upper()

    if soru == "Q":
        breakpoint
    
    if soru == "E" or soru == "EVET":
        karisim = random.choice(data_list)
        print("\n Hayırlı olsun işte nickiniz ->: "+karisim)
    
       

if __name__ == "__main__":
    main()
