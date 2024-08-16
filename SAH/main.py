import FEnotation #Ugotovi kera figura je kje na podlagi prejsnjega FEN-a in ali so polja prazna, imajo črne ali bele figure
import coords #Ti mu das polje, on ti da koordinate kamor mora robot
import stockfish_wrapper #Z njim lahko uporabljamo stockfish - da nam poteze (zahvale zhelyabuzhsky-ju)
import CheckCoords #Pove nam če je polje praznio, kako visoka je figura na njem ali pa spremeni FEN na podlagi poteze
import socket #Za socket komunikacijo
import time #Za funkcije čakanja
import pogled #S kamero pogleda ploščo in nam pove ali so polja prazna, oz. katere barve je figura na njih
import Graphics #GUI za pokazat FEN 

#! podajas se na nevarno potovanje v notranjost neraziskane kode. Srečno vojak 🫡s

HOST = "192.168.125.123" #IP od računalnika za namene socket komunikacije
PORT = 65432 #Št. porta za namene socket komunikacije 

prev = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR" #FEN začetne pozicije 

def send_coords(c_socket:socket, coords:list) -> None: #Roki pošlje koordinate po socketu (sprejme socket ki ga želi na clientu in pa seznam koordinat)
    for i in range(6):
        c_socket.sendall(str(coords[i]).encode()) #Pošlje prvo koordinato
        time.sleep(0.1) #Delay da ni prehitro
    

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

server_socket.listen(5)
print(f'Server listening on {HOST}:{PORT}')

GotMove = False #Bool če ima potezo
coordinates = []
konec=["E", "0", "0", "0", "0", "0"] #Te koordinate pošljemo če se igra konča, da roka ne vrže error ampak naredi nekaj predvidjivega

while True:
    client_socket, addr = server_socket.accept() #Odpre socket in čaka na povezavo clienta (roke)
    while True: # ko se ta povezava zgodi delamo še en while loop
        # dobimo podatke od roke
        data = client_socket.recv(1024).decode('utf-8') # 1MB max
        if not data:
            break
        if data == "move": # Če po socketu prejmemo move, pomeni da je roka pripravljena na potezo in roki vrnemo potezo
            seznam_koordinat = [] #Sprazne seznam koordinat
            BnW = pogled.get_fen_from_pic() #iz slike vidi ali so polja prazna, ali imajo črne ali bele igure    
            prev = FEnotation.get_fen(prev, BnW) #Na podlagi tega ali so polja prazna in barv figur na njih nam pove katera figura je kje

            Graphics.see_board(prev) #Poaže igro z GUI
            # poteza za stockfish   vvvvvvvvvvvvvvv
            stock = stockfish_wrapper.get_move(prev + " b") 
            move, temp = stock[0], stock[1]

            if CheckCoords.check_square(prev, move[2:])!=True: #Če na cilju še ni figure oz. če roka ne rabi "jesti"
                seznam_koordinat.append(coords.get_coords(move[:2]))
                seznam_koordinat[0].append(CheckCoords.Piece_height(prev, move[:2]))
                seznam_koordinat.append(coords.get_coords(move[2:]))
                seznam_koordinat[1].append(CheckCoords.Piece_height(prev, move[2:]))
            else:
                seznam_koordinat.append(coords.get_coords(move[2:]))                     # dobimo prve koordinate (ta kmet bo pojeden)    [(x, y, 0)]
                seznam_koordinat[0].append(CheckCoords.Piece_height(prev, move[2:]))     # dobimo višino za prejšnjo potezo [(x, y, Z)]
                seznam_koordinat.append((0, 650, 0))                                     # nesemo kmeta na (0, 650, 0)
                
                seznam_koordinat.append(coords.get_coords(move[:2]))                     # dobimo koordinate kje je kmet, ki je pojedel
                seznam_koordinat[2].append(CheckCoords.Piece_height(prev, move[:2]))     # dobimo višino za prejšnjo potezo
                seznam_koordinat.append(coords.get_coords(move[2:]))                     # dobimo kam rabi ta kmet it
                seznam_koordinat[3].append(CheckCoords.Piece_height(prev, move[2:]))     # in kako visoko ga odpozimo  
            #! sez.clear()          # napaka hall of fame
            prev = temp
            Graphics.see_board(prev)
            GotMove = True
            coordinates.clear()
            time.sleep(0.3)
            for i in range (2): #Na coords da 1. del poteze
                for j in range(3):
                    coordinates.append(str(seznam_koordinat[0][i]))
                seznam_koordinat.pop(0)
        
        if data == "move2" and len(seznam_koordinat)!=0: #Move2 -> roka pričakuje 2. del poteze, če seznam koordinat ni prazen ga dodamo na cords
            coordinates.clear()
            for i in range (2):
                for j in range(3):
                    coordinates.append(str(seznam_koordinat[0][i]))
                seznam_koordinat.pop(0)

        elif data == "move2" and len(seznam_koordinat) == 0: #Če je seznam koordinat prazen pomeni da roka ne bo jedla in mu damo koordinate ki nakazujejo konec poteze
            coordinates.clear()
            for i in konec:
                coordinates.append(i)   

        send_coords(client_socket, coordinates)