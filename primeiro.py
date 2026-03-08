password_correct = "python"
password_entered = input("Digite a senha: ")
counter = 0

while password_correct != password_entered:
    print("senha incorreta")
    password_entered = input("Digite a senha novamente: ")
    counter += 1

print(f"senha correta")
print(f"tentativas: {counter} erradas")