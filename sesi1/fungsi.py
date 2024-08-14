import socket
from time import sleep
pc_name = socket.gethostname()
def judul() :
    
    yolo = "*" * (len(pc_name)+6)
    print(yolo)
    print(f'** {pc_name} **')
    print(yolo)

def exit_program():
    print ("program akan di hentikan")
    sleep(1)
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    print("program di hentikan")
    exit()
    
     
if __name__ == "__main__" :
    judul()
    exit_program()
    