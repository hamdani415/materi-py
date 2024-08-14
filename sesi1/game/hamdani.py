import random
import main

def mulai() :
    while True :
        marmut_posisi = random.randint(1,4)
        marmut = ["|🐹| |_| |_| |_|", "|_| |🐹| |_| |_|" , "|_| |_| |🐹| |_|" ,"|_| |_| |_| |🐹|"]

        jawaban = marmut[marmut_posisi - 1]

        

        print (f'\ncoba perhatikan goa di bawah ini\n\n|_| |_| |_| |_|\n ')
        pilihan= int(input ("menurut kamu dimana marmut berada 1/2/3/4 ? :"))

        if marmut_posisi == pilihan : 
            
            print(f"\n{jawaban}\n\nselamat  kamu menang posisi marmut ada di posisi {marmut_posisi} dan pilihan kamu adalah {pilihan}")
        else :
            
            print (f'\n{jawaban}\n\njawaban kamu salah posisi marmut ada di {marmut_posisi} sedangkan pilihan kamu adalah {pilihan}')
            
        lanjut = input ("apakah kamu mau bermain lagi? [y/n]:")
        if lanjut == "n" :
           main.menu()


if __name__ == "__main__" :
    mulai()
    