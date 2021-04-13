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
venceu = ("Parabéns, você venceu").encode()
perdeu = ("Infelizmente você perdeu :(").encode()
bowie = 0

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

"""enviav = [x.encode('UTF8') for x in velha]# Codifica a matriz para enviar ao client
c.send(enviav) # Envia a matriz codificada"""
    
def posicao(jogada): # alocar jogada do server na matrix
    jogada = int(input("Digite onde que jogar: "))
    while jogada < 0 and jogada > 9:
        jogada = int(input("Digite um valor disponível: "))
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
    printarm(velha)
    matrizstring()


def matrizstring():
    s = ""
    for i in range(3):
        if i == 1 or i == 2:
            s+=str(velha[i])+"\n"
            print("-"*10)
        else:
            s+=str(velha[i])+"\n"
    return(s)
    msg = printarm(velha)
    print(msg)
    codmsg = msg.encode()
    enviam = c.send(codmsg)

def posicaoc(jogada): # função a cada vez que o client jogar
    matrizstring()
    jogada = int(c.recv(1000).decode())
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
    if velha[0][0] and velha[0][1] and velha[0][2] == "x":
        print(venceu)
        c.send(perdeu)
    elif velha[1][0] and velha[1][1] and velha[1][2] == "x":
        print(venceu)
        c.send(perdeu)
    elif velha[2][0] and velha[2][1] and velha[2][1] == "x":
        print(venceu)
        c.send(perdeu)
    elif velha[0][1] and velha[1][1] and velha[2][1] == "x":
        print(venceu)
        c.send(perdeu)
    elif velha[0][2] and velha[1][1] and velha[2][0] == "x":
        print(venceu)
        c.send(perdeu)
    elif velha[0][0] and velha[1][1] and velha[2][2] == "x":
        print(venceu)
        c.send(perdeu)
    elif velha[0][0] and velha[1][0] and velha[2][0] == "x":
        print(venceu)
        c.send(perdeu)
    elif velha[0][1] and velha[1][1] and velha[2][1] == "x":
        print(venceu)
        c.send(perdeu)
    elif velha[0][2] and velha[1][2] and velha[2][2] == "x":
        print(venceu)
        c.send(perdeu)
    else:
        empate = 9 - qt_jogada
        print("faltam", empate, "jogadas para dar velha!")

    if velha[0][0] and velha[0][1] and velha[0][1] == "o":
        print(perdeu)
        c.send(venceu)
    elif velha[1][0] and velha[1][1] and velha[1][1] == "o":
        print(perdeu)
        c.send(venceu)
    elif velha[2][0] and velha[2][1] and velha[2][1] == "o":
        print(perdeu)
        c.send(venceu)
    elif velha[0][1] and velha[1][1] and velha[2][2] == "o":
        print(perdeu)
        c.send(venceu)
    elif velha[0][2] and velha[1][1] and velha[2][0] == "o":
        print(perdeu)
        c.send(venceu)
    elif velha[0][0] and velha[1][0] and velha[2][0] == "o":
        print(perdeu)
        c.send(venceu)
    elif velha[0][1] and velha[1][1] and velha[2][1] == "o":
        print(perdeu)
        c.send(venceu)
    elif velha[0][2] and velha[1][2] and velha[2][2] == "o":
        print(perdeu)
        c.send(venceu)
    else:
        empate = (9 - qt_jogada)
        print(empate)


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

#print("matriz após a jogada do client: ", velha)

printarm(velha) # Executa a função de exibir o estado atual da matriz

"""
posicao(bowie): # alocar jogada do server na matrix
posicao(jogada): # função a cada vez que o client jogar
printarm(velha): # Executa a função de exibir o estado atual da matriz
condic(): #
"""
