# Constante que define a quantidade de entrevistados
# Inicialmente foram feitos testes com 5 entrevistados, mas o programa foi ajustado para coletar dados de 50 pessoas
total_entrevistados = 50

# Inicialização dos acumuladores de notas
qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0

# Exibição do cabeçalho formatado do programa (Utilizando formatação ANSI)
print(f"\33[1m{' Programa Pesquisa de Satisfação ': ^75}\33[0m")
print()
print(f"\33[1m{' Tudo Web ':=^75}\33[0m")
print()
print(
    "Olá! Somos a Tudo Web, empresa de agência de marketing digital e soluções"
    " web e gostaríamos de saber a\nsua opinião sobre os nossos serviços. Por"
    " favor, responda as perguntas abaixo."
)
print("\n" * 2)

# Laço principal 'for': itera exatamente 50 vezes (de 1 até total_entrevistados)
for cont in range(1, total_entrevistados + 1):
    # Exibe o número do entrevistado atual no ciclo
    print(f"--- Entrevistado {cont} de {total_entrevistados} ---")

    # Coleta do nome do entrevistado
    nome = input("Digite o seu nome: ")

    # Validação da idade utilizando o método .isdigit()
    idade = input("Digite a sua idade: ")
    while not idade.isdigit():
        print(
            "[Aviso] Idade inválida! Por favor digite apenas números para a idade."
        )
        idade = input("Digite a sua idade: ")

    # Como o isdigit aceita apenas strings numéricas, aqui se faz necessário convertemos para um número inteiro
    idade = int(idade)

    print()
    print("Avalie o nosso atendimento:")
    print()
    print("""
          [1] Excelente
          [2] Bom
          [3] Ruim          
          """)

    # Coleta e validação da opção para evitar crash se o usuário digitar texto
    opiniao_str = input("Digite o número que representa a sua opinião: ")
    
    # Garante que seja numérico e esteja no intervalo de 1 a 3
    while not opiniao_str.isdigit() or int(opiniao_str) < 1 or int(opiniao_str) > 3:
        print("[Aviso] Opção inválida! Digite um número entre 1 e 3.")
        opiniao_str = input("Digite o número que representa a sua opinião: ")

    opiniao = int(opiniao_str)

    # Estruturas de decisão (if/elif) para contabilizar os votos
    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 2:
        qtd_bom += 1
    elif opiniao == 3:
        qtd_ruim += 1

    print()

# Exibição do bloco final com os resultados consolidados da pesquisa
print("\n" * 2)
print(f"\33[1m{' Resultado da Pesquisa ':=^75}\33[0m")
print()
print(f"--- Total de entrevistados: {total_entrevistados} ---")
print(f"--- Total de pessoas que responderam Excelente: {qtd_excelente} ---")
print(f"--- Total de pessoas que responderam Bom: {qtd_bom} ---")
print(f"--- Total de pessoas que responderam Ruim: {qtd_ruim} ---")

print("\n" * 3)

# Mensagem de encerramento do programa
print(f"\33[1m{'Obrigado por responder a nossa pesquisa, a sua opinião é muito importante para nós!':^75}\33[0m")