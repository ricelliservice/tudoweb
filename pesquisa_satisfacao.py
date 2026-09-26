# Constante que define a quantidade de entrevistados
# (Define a quantidade de pessoas que participarão da pesquisa)
total_entrevistados = 3

# Inicialização das variáveis de controle e acumuladores de notas
cont = 1
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
    " favor, responda as perguntas abaixo.")
print("\n" * 2)

# Laço principal 'while': controla a repetição para coletar dados de cada entrevistado
while cont <= total_entrevistados:
  # Exibe o número do entrevistado atual no ciclo
  print(f"--- Entrevistado {cont} de {total_entrevistados} ---")

  # Coleta do nome do entrevistado
  nome = input("Digite o seu nome: ")

  # Validação da idade utilizando o método .isdigit()
  # Garante que o programa não quebre caso o usuário digite texto ou deixe vazio quando solicitado a idade
  idade = input("Digite a sua idade: ")
  while not idade.isdigit():
    print(
        "[Aviso] Idade inválida! Digite apenas números inteiros para a idade."
    )
    idade = input("Digite a sua idade: ")

  # Conversão segura da idade para inteiro após a validação bem-sucedida
  idade = int(idade)

  print()
  print("Avalie o nosso atendimento:")
  print()
  print("""
          [1] Excelente
          [2] Bom
          [3] Ruim          
          """)

  # Coleta da opção que classifica a pesquisa
  opiniao = int(input("Digite o número que respresenta a sua opinião: "))

  # Laço 'while' secundário: garante que não haja uma entrada de dados inválida
  while opiniao < 1 or opiniao > 3:
    print("[Aviso] Opção inválida! Digite um número entre 1 e 3.")
    opiniao = int(input("Digite o número que respresenta a sua opinião: "))

  # Estruturas de decisão (if/elif) para contabilizar os votos de acordo com a escolha
  if opiniao == 1:
    qtd_excelente += 1
  elif opiniao == 2:
    qtd_bom += 1
  elif opiniao == 3:
    qtd_ruim += 1

  # Incrementa o contador para avançar para o próximo entrevistado (evita loop infinito)
  cont += 1
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

#Mensagem de encerramento do programa

print(f"\33[1m{'Obrigado por responder a nossa pesquisa, a sua opnião é muito importante para nós!':^75}\33[0m") 