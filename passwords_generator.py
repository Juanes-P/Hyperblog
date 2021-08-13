import random


def generar_contrasena():

    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"', "'", "«", "»"]

    caracteres = MAYUS + MINUS + NUMS + CHARS

    password = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)
        
    password = "".join(password)
    return password


def run():
    pasword = generar_contrasena()
    print(f"Your new password is: ----->  {pasword}  <----- ")



if __name__ == "__main__":
    run()