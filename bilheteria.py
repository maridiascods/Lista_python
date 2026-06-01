#Aluno 1: padronizar o nome do filme--
def formatar (nome):
    return nome.upper()

#Aluno 2: Verificardor de idade--
def verificar_idade(idade): 
    if idade >= 18:
        return "Autorizado"
    else:
        return"Não Autorizado"
    
#bruno não é autorizado--
#não falamos do bruno--
#Aluno 3: Mensagem de retorno--
def gerar_mensagem(status):
    if status == "Autorizado":
        return "Tenha uma ótima Sessão!"
    else: 
        return"Sentimos,mas você não tem a idade minima"

    #Aluno 4: Execução de Algoritimo--
filme_entrada = input("Digite  o filme escolhido: ")
idade_entrada = int(input("Digite sua idade: "))
nome_final = formatar(filme_entrada) 
status_acesso = verificar_idade(idade_entrada)
mensagem = gerar_mensagem(status_acesso)
print(f"\nFilme:{nome_final}")
print(f"Status:{status_acesso}")
print(f"Mensagem:{mensagem}")

