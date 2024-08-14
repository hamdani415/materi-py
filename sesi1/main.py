from game import hamdani
from fungsi import judul , exit_program
from tools import warung

def menu() :
    user_options = int(input ('menu program:\n1. hamdani game\n2. warung hamdani\n3. keluar\n\nsiahkan pilih :'))
    if user_options == 1 :
        hamdani.mulai()
    elif user_options == 2 :
        warung.mulai()
    elif user_options == 3 :
        exit_program()
        exit()
    else :
        print('hanya bisa pilih yang ada di dalam menu!!!\n')
        menu()

def game ():
    judul()
    menu()


if __name__ == "__main__" :
    game()