# Automação de Cadastro de Produtos com Python

Projeto desenvolvido para praticar automação web utilizando Python.

A aplicação lê uma planilha Excel com dados de produtos e realiza o cadastro automático em uma aplicação web local utilizando Playwright.

O projeto também possui validação de dados, tratamento de erros, geração de logs, screenshots em caso de falha e relatório final da execução.

## Objetivo

O objetivo deste projeto é automatizar uma tarefa repetitiva de cadastro de produtos.

Os dados são obtidos de uma planilha Excel e processados pelo Python. Em seguida, o Playwright acessa uma aplicação web e realiza o preenchimento automático dos campos.

Ao final da execução, é gerado um relatório com o resultado de cada produto processado.

## Tecnologias utilizadas

- Python
- Playwright
- Pandas
- OpenPyXL
- Flask
- HTML
- Logging

## Funcionamento

O fluxo da automação é:

```text
produtos.xlsx
      ↓
Pandas
      ↓
Validação dos dados
      ↓
Playwright
      ↓
Aplicação Web
      ↓
Cadastro dos produtos
      ↓
Logs / Screenshots
      ↓
resultado.xlsx
```

## Funcionalidades

- Leitura de produtos através de arquivo Excel
- Validação de preço e quantidade
- Automação do navegador com Playwright
- Cadastro automático de produtos
- Tratamento de exceções
- Registro de logs
- Captura de screenshot em caso de erro
- Geração de relatório Excel com o resultado da execução
- Separação das responsabilidades em diferentes módulos

## Estrutura do projeto

```text
automacao-produtos/
│
├── automacao/
│   ├── main.py
│   ├── leitor_excel.py
│   ├── validacao.py
│   ├── automacao_web.py
│   └── relatorio.py
│
├── dados/
│   └── produtos.xlsx
│
├── logs/
│
├── resultados/
│
├── screenshots/
│
├── sistema/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Arquivo de entrada

Os produtos são informados através do arquivo:

```text
dados/produtos.xlsx
```

Exemplo:

| codigo | nome | preco | quantidade |
| --- | --- | ---: | ---: |
| 101 | Caneta Azul | 2.50 | 100 |
| 102 | Caderno Universitário | 19.90 | 50 |
| 103 | Mouse USB | 89.90 | 20 |
| 104 | Teclado | 120.00 | 15 |

## Validações

Antes de realizar o cadastro, alguns dados são validados.

Por exemplo:

- O preço deve ser maior que zero.
- A quantidade não pode ser negativa.

Caso algum produto não passe pela validação, ele não será enviado para o cadastro e será registrado no relatório final.

## Tratamento de erros

A automação utiliza `try/except` para evitar que uma falha interrompa todo o processamento.

Quando ocorre uma exceção durante o cadastro:

- O erro é registrado.
- É gerado um screenshot da tela somente quando ocorre uma exceção do Playwright ou do Python.
- O produto recebe status de erro no relatório.
- A automação continua processando os próximos produtos.

## Logs

Os logs são gerados no arquivo:

```text
logs/automacao.log
```

Exemplo:

```text
2026-10-06 10:30:10 - INFO - Caneta Azul: cadastrado com sucesso.
2026-10-06 10:30:11 - WARNING - Mouse USB: preço inválido.
2026-10-06 10:30:12 - ERROR - Erro ao cadastrar Teclado.
```

## Relatório

Ao final da execução é gerado:

```text
resultados/resultado.xlsx
```

Exemplo:

| codigo | nome | status | mensagem |
| --- | --- | --- | --- |
| 101 | Caneta Azul | Sucesso | Produto cadastrado |
| 102 | Caderno Universitário | Sucesso | Produto cadastrado |
| 103 | Mouse USB | Erro | Preço inválido |

## Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd automacao-produtos
```

### 2. Crie o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Instale o Chromium utilizado pelo Playwright

```bash
playwright install chromium
```

### 6. Inicie a aplicação web

```bash
python sistema/app.py
```

A aplicação estará disponível em:

```text
http://localhost:5000
```

### 7. Execute a automação

Abra outro terminal e execute:

```bash
python automacao/main.py
```

O navegador será aberto automaticamente e os produtos existentes no arquivo Excel serão cadastrados.

## Dependências

O arquivo `requirements.txt` possui as principais bibliotecas utilizadas:

```text
flask
playwright
pandas
openpyxl
```

## Conceitos praticados

Durante o desenvolvimento deste projeto foram utilizados conceitos como:

- Variáveis
- Funções
- Estruturas condicionais
- Estruturas de repetição
- Listas
- Dicionários
- Manipulação de arquivos Excel
- Tratamento de exceções
- Modularização
- Logs
- Automação Web
- Seletores CSS
- Interação com elementos HTML

## Aprendizado

Este projeto foi desenvolvido como parte dos meus estudos em Python e automação.

O principal objetivo foi criar uma automação completa, passando pela leitura e validação dos dados, interação com uma aplicação web, tratamento de falhas e geração de um relatório final.

Também busquei aplicar boas práticas de organização, separando responsabilidades em diferentes módulos para facilitar a leitura e manutenção do código.

## Próximas melhorias

Como evolução do projeto, poderão ser adicionados:

- Testes automatizados
- Novas regras de validação
- Configurações externas
- Melhorias na interface da aplicação
- Novos tipos de relatórios
- Execução do navegador em modo headless
- Melhorias no tratamento de erros

## Autor

Kennedy Martins

Desenvolvedor Full Stack em aprendizado contínuo de Python e automação.