# 📊 Pesquisa de Satisfação - Tudo Web

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![Marketing](https://img.shields.io/badge/Empresa-Tudo_Web-0284c7?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?style=for-the-badge&logo=github&logoColor=white)

---

## 📌 Sobre o Projeto
O **Pesquisa de Satisfação** é um sistema interativo desenvolvido em Python para a agência de marketing digital e soluções web **Tudo Web**. O programa automatiza a coleta de opiniões dos clientes, garantindo a validação de dados demográficos e avaliações de atendimento para gerar um relatório estatístico consolidado ao final.

---

## 🎯 Objetivos
* Controlar o fluxo de entrevistas com um número pré-definido de participantes.
* Coletar e validar dados de identificação e idade dos entrevistados em tempo de execução.
* Oferecer um menu interativo com opções de avaliação de atendimento claras e intuitivas.
* Processar e exibir um relatório final consolidado com a contagem exata de votos por categoria.

---

## 🛠️ Linguagem e Recursos Utilizados
* **Python 3** — Linguagem principal de desenvolvimento.
* **Laços de Repetição (`while`)** — Controle do fluxo de repetição por entrevistado e validação de entradas inválidas.
* **Validação de Dados** — Uso do método `.isdigit()` para garantir que apenas números inteiros sejam aceitos no campo de idade.
* **Formatadores ANSI** — Aplicação de estilos em negrito, centralização e formatação visual elegante no terminal.

---

## 🧮 Opções de Avaliação e Regras

| Opção | Categoria | Ação no Sistema / Contabilização |
| :--- | :--- | :--- |
| **[1]** | **Excelente** | Incrementa o contador de avaliações de nível máximo de satisfação. |
| **[2]** | **Bom** | Incrementa o contador de avaliações positivas intermediárias. |
| **[3]** | **Ruim** | Incrementa o contador de avaliações que necessitam de melhoria no atendimento. |

---

## 🚀 Como Executar o Programa

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Clone este repositório ou baixe o arquivo de código-fonte (`pesquisa_satisfacao.py`).
3. Abra o terminal na pasta onde o script está salvo.
4. Execute o programa digitando o comando:

```bash
python pesquisa_satisfacao.py