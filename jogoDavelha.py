tabuleiro = [       #cria uma array com valores vazios para formar o jogo da velha
    [" "," "," "],
    [" "," "," "],
    [" "," "," "],
]
jogador = "X" 
def exibeTabuleiro(): #função para a estrura do jogo da velha
    for linha in tabuleiro:
        print(f"|".join(linha)) # forma resumida desse código --> {linha[0]}|{linha[1]}|{linha[2]}
        print("-" * 5) # repete a string 5 vezes

def jogada(linha, coluna):
    if (not 0 <= linha <=2 or   # linha for menor que 0 ou maior que 2, jogada invalida
        not 0 <= coluna <= 2 or  # coluna for menor que 0 ou maior que 2, jogada invalida
        tabuleiro[linha][coluna] != " " # jogar em posiçoes que ja foram marcadas ,jogada invalida
    ): 
        print("Jogada invalida")
        return jogador
    tabuleiro[linha][coluna] = jogador
    return "O" if jogador == "X" else "X" # lógica inversa para alternar as vezes dos jogadores

def temGanhador():
    #verifica as linhas
    for linha in range(3):
        if (
            tabuleiro[linha][0] != " " and
            tabuleiro[linha][0] == tabuleiro[linha][1] and
            tabuleiro[linha][0] ==  tabuleiro[linha][2]
        ):
            print(f"{tabuleiro[linha][0]} ganhou")
            return True
    #verifica as colunas
    for coluna in range(3):
        if (
            tabuleiro[0][coluna] != " " and
            tabuleiro[0][coluna] == tabuleiro[1][coluna] and
            tabuleiro[0][coluna] ==  tabuleiro[2][coluna]
        ):
            print(f"{tabuleiro[coluna][0]} ganhou")
            return True
    #verifica as diagonais
    if (
        tabuleiro[1][1] != " " and(
        (
            tabuleiro[0][0] == tabuleiro[1][1] and
            tabuleiro[0][0] == tabuleiro[2][2]
        )
        or
        ( 
            tabuleiro[0][2] == tabuleiro[1][1] and
            tabuleiro[1][1] == tabuleiro[2][0]
        )
        )
    ):
        print(f"{tabuleiro[1][1]} ganhou")
        return True
    #se nao teve ganhador de nenhuma forma
    return False

def  temEmpate():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == " ":
                return False
    print("Acabou empatado!")
    return True

while True:
    print(f"Jogador da vez : {jogador}")
    try:
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        jogador = jogada(linha, coluna)
    except (ValueError, IndexError): # tratar os erros mais comuns do código
        print("Digite valores numéricos entre 0 e 2")
    exibeTabuleiro()
    if temGanhador() or temEmpate():
        break
    
    