# 📂 Organizador de Arquivos em Python

Projeto simples para organizar automaticamente arquivos de uma pasta por tipo.

## 📌 Objetivo

Projeto criado para praticar Python e automacao de tarefas do dia a dia.

## 🚀 Funcionalidades

- Separar arquivos por tipo, como Imagens, Videos, Musicas, Documentos, Compactados e Executaveis
- Criar pastas automaticamente
- Evitar sobrescrever arquivos duplicados
- Permitir que o usuario escolha outra pasta
- Mostrar relatorio final no terminal

## 🧠 Tecnologias

- Python
- Biblioteca `os`
- Biblioteca `shutil`

## ▶️ Como usar

O programa detecta automaticamente o usuario do computador e usa o `Desktop` como pasta padrao.

No codigo, a linha principal e esta:

```python
pasta_padrao = os.path.join(os.path.expanduser("~"), "Desktop")
Se quiser mudar a pasta padrao, troque "Desktop" por outra pasta, como por exemplo:

pasta_padrao = os.path.join(os.path.expanduser("~"), "Downloads")
Depois, execute no terminal:

python organizador.py
Quando o programa iniciar, ele vai mostrar algo assim:

Digite o caminho da pasta que deseja organizar [C:\Users\SeuUsuario\Desktop]:
Se quiser usar a pasta padrao, basta apertar Enter
Se quiser outra pasta, digite o caminho manualmente e pressione Enter
Exemplo:

C:\Users\SeuUsuario\Downloads
📊 Exemplo de saida
Movendo: foto.jpg -> Imagens
Movendo: arquivo.pdf -> Documentos

===== RELATORIO =====
Arquivos movidos: 5
Arquivos ignorados: 2
📁 Estrutura do projeto
organizador-arquivos-python/
|
├── organizador.py
└── README.md

💡 Melhorias futuras
Adicionar suporte para mais tipos de arquivos
Criar interface grafica simples
Permitir escolher multiplas pastas
Exibir mais detalhes no relatorio final
