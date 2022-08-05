def calculomapa():
    XminSRU = 0
    YminSRU = 0
    XminSRD = 0
    YminSRD = 0
    XmaxSRU = int(input("Digite o valor maximo de Altura no Universo (em CM):"))
    YmaxSRU = int(input("Digite o valor maximo de Largura no Universo (em CM):"))
    XmaxSRD = int(input("Digite o valor maximo de Altura no Dispositivo (em Pixels):"))
    YmaxSRD = int(input("Digite o valor maximo de Largura no Dispositivo (em Pixels):"))
    Xu = int(input("Digite o valor Altura que você gostaria de mapear no Dispositivo (em Pixels):"))
    Yu = int(input("Digite o valor Largura que você gostaria de mapear no Dispositivo (em Pixels):"))

    print("O valor Altura mapeado no dispositivo é igual á:", XminSRD+(Xu-XminSRU)*((XmaxSRD-XminSRD)/(XmaxSRU-XminSRU)))
    print("O valor Largura mapeado no dispositivo é igual á:", YminSRD+(Yu-YminSRU)*((YmaxSRD-YminSRD)/(YmaxSRU-YminSRU)))
    laco()

def laco():
    repete = int(input("Digite 1 para fazer um novo calculo ou 2 para encerrar o programa:"))

    if repete == 1:
        calculomapa()
    elif repete == 2:
        print(""" 
        
                                Muito Obrigado por utilizar este programa!
         
         Att.
         Pedro Henrique Sassi""")
        exit(0)
    else:
        print("Caractere invalido!")
        laco()

def bemvindo():
    print(""" 
    
        Seja Bem Vindo a este programa:
        
          Trata-se de um programa em Python que, dado um ponto no sistema de origem, calcula o respectivo ponto no sistema destino (SRD)
          Ele foi desenvolvido por Pedro Henrique Gomes Sassi aluno do Curso de Ciencia da Computação no IFFAr-FW
          para cumprimento de demanda da matéria de Computação Grafica ministrada pelo professor Dr. Ygor Yepes. 
                            
                            
                            Vamos Começar:
                            
                            """)

bemvindo()
calculomapa()
