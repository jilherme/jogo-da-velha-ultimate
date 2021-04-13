#! /usr/bin/python
# encoding=utf-8
import sys
import socket

PORT = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = ("", int(PORT))
s.bind(dest)
s.listen(1)
c, ipcliente = s.accept()
qt_jogada = 0
jogada = 0
bowie = 0
venceu = str
perdeu = str

#server velha
#=======================================================================

msg = c.recv(1000).decode()
print(msg)

msg = "Hello world pra voce tambem!".encode()
c.send(msg)

# hello word pra testar comunicação
#=======================================================================
# início do código

velha = [[1,2,3],[4,5,6],[7,8,9]] # Declarou o formato do tabuleiro

def printarm(velha):
    for i in range(3):
        if i == 1 or i == 2:
            print("-"*10)
            print(velha[i])
        else:
            print(velha[i])

printarm(velha) # Executa a função de exibir o estado atual da matriz

"""def encode(velha):
    if isinstance(velha, list):
        return [encode(x) for x in velha]
    else:
        return velha.encode('utf-8')"""

enviavelha = velha.encode() # Codifica a matriz para enviar ao client
c.send(enviavelha) # Envia a matriz codificada
    
def posicao(bowie): # alocar jogada do server na matrix
    bowie = int(input("Digite onde que jogar: "))
    while bowie < 0 and bowie > 9:
        bowie = int(input("Digite um valor disponível: "))
    if jogada > 0 and jogada < 10:
        if jogada == 1:
            velha[0][0] = "x"
        elif jogada == 2:
            velha[0][1] = "x"
        elif jogada == 3:
            velha[0][2] = "x"
        elif jogada == 4:
            velha[1][0] = "x"
        elif jogada == 5:
            velha[1][1] = "x"
        elif jogada == 6:
            velha[1][2] = "x"
        elif jogada == 7:
            velha[2][0] = "x"
        elif jogada == 8:
            velha[2][1] = "x"
        elif jogada == 9:
            velha[2][2] = "x"
    enviavelha = velha.encode() # Codifica a matriz para enviar ao client
    c.send(enviavelha) # Envia a matriz codificada
    printarm(velha)
    

def posicaoc(jogada): # função a cada vez que o client jogar
    jogada = c.recv(1000).decode
    if jogada > 0 and jogada < 10:
        if jogada == 1:
            velha[0][0] = "o"
        elif jogada == 2:
            velha[0][1] = "o"
        elif jogada == 3:
            velha[0][2] = "o"
        elif jogada == 4:
            velha[1][0] = "o"
        elif jogada == 5:
            velha[1][1] = "o"
        elif jogada == 6:
            velha[1][2] = "o"
        elif jogada == 7:
            velha[2][0] = "o"
        elif jogada == 8:
            velha[2][1] = "o"
        elif jogada == 9:
            velha[2][2] = "o"

    printarm(velha)

def conidc(): # Determinara quem ganhou
    venceu = ("Parabéns, você venceu").encode()
    perdeu = ("Infelizmente você perdeu :(").encode()
if velha[0][0] and velha[0][1] and velha[0][1] == "x":
    print(venceu)
    c.send(perdeu)
    socket.close()
elif velha[1][0] and velha[1][1] and velha[1][1] == "x":
    print(venceu)
    c.send(perdeu)
    socket.close()
elif velha[2][0] and velha[2][1] and velha[2][1] == "x":
    print(venceu)
    c.send(perdeu)
    socket.close()
elif velha[0][1] and velha[1][1] and velha[2][2] == "x":
    print(venceu)
    c.send(perdeu)
    socket.close()
elif velha[0][2] and velha[1][1] and velha[2][0] == "x":
    print(venceu)
    c.send(perdeu)
    socket.close()
elif velha[0][0] and velha[1][0] and velha[2][0] == "x":
    print(venceu)
    c.send(perdeu)
    socket.close()
elif velha[0][1] and velha[1][1] and velha[2][1] == "x":
    print(venceu)
    c.send(perdeu)
    socket.close()
elif velha[0][2] and velha[1][2] and velha[2][2] == "x":
    print(venceu)
    c.send(perdeu)
    socket.close()
else:
    if qt_jogada < 9:
        empate = 9 - qt_jogada
        print("faltam", empate, "jogadas para dar velha!")
    elif qt_jogada == 9:
        print("Deu velha!")

if velha[0][0] and velha[0][1] and velha[0][1] == "o":
    print(perdeu)
    c.send(venceu)
    socket.close()
elif velha[1][0] and velha[1][1] and velha[1][1] == "o":
    print(perdeu)
    c.send(venceu)
    socket.close()
elif velha[2][0] and velha[2][1] and velha[2][1] == "o":
    print(perdeu)
    c.send(venceu)
    socket.close()
elif velha[0][1] and velha[1][1] and velha[2][2] == "o":
    print(perdeu)
    c.send(venceu)
    socket.close()
elif velha[0][2] and velha[1][1] and velha[2][0] == "o":
    print(perdeu)
    c.send(venceu)
    socket.close()
elif velha[0][0] and velha[1][0] and velha[2][0] == "o":
    print(perdeu)
    c.send(venceu)
    socket.close()
elif velha[0][1] and velha[1][1] and velha[2][1] == "o":
    print(perdeu)
    c.send(venceu)
    socket.close()
elif velha[0][2] and velha[1][2] and velha[2][2] == "o":
    print(perdeu)
    c.send(venceu)
    socket.close()
else:
    empate = (9 - qt_jogada).encode()
    c.send(empate)

posicao(bowie)
qt_jogada += 1
conidc()
posicaoc(jogada) # Executa a função da jogada do client
qt_jogada += 1
conidc()
posicao(bowie)
qt_jogada += 1
conidc()
posicaoc(jogada)
qt_jogada += 1
conidc()
posicaoc(bowie)
qt_jogada += 1
conidc()
posicaoc(jogada)
qt_jogada += 1
conidc()
posicao(bowie)
qt_jogada += 1
conidc()
posicaoc(jogada)
qt_jogada += 1
conidc()
posicao(bowie)
qt_jogada += 1
conidc()
#
print("matriz após a jogada do client: ", velha)

printarm(velha) # Executa a função de exibir o estado atual da matriz

"""
posicao(bowie): # alocar jogada do server na matrix
posicao(jogada): # função a cada vez que o client jogar
printarm(velha): # Executa a função de exibir o estado atual da matriz
condic(): #
"""