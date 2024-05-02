class exercicios:
    def __init__(self,nome,idade, sexo,status):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.status = status 

    def exercicios1(self):
        nome = "Maryana linda"
        idade = 17
        sexo = "feminino"
        status = True
        print("Meu nome é: ",nome, " tenho ", idade, "anos",sexo, "sexo", status, "status")

    def exercicios2 (self):  
        alunos = ["maryana", "maria", "carol", "bibi"]
        notas = [10, 1, 1, 0]
        print("Alunos:")
        for aluno in alunos:
            print(aluno)

        print("\nNotas:")
        for nota in notas:
            print(nota)



maryana = exercicios("maryana linda", 17, "F", True)
maryana.exercicios1()
maryana.exercicios2()

