# 📂 Organizador de Arquivos em Python

Projeto simples para organizar automaticamente arquivos da pasta Downloads por tipo.

---

## 📌 Objetivo

Projeto criado para praticar Python e automação de tarefas do dia a dia.

---

## 🚀 Funcionalidades

* Separa arquivos por tipo (Imagens, Vídeos, Documentos)
* Cria pastas automaticamente
* Evita sobrescrever arquivos duplicados
* Mostra relatório final no terminal

---

## 🧠 Tecnologias

* Python
* Biblioteca `os`
* Biblioteca `shutil`

---

## ▶️ Como usar

1. Ajuste o caminho da pasta no código:

```python
pasta = r"C:\Users\SeuUsuario\Downloads"
```

2. Execute no terminal:

```bash
python organizador.py
```

---

## 📊 Exemplo de saída

```bash
Movendo: foto.jpg → Imagens
Movendo: arquivo.pdf → Documentos

===== RELATÓRIO =====
Arquivos movidos: 5
Arquivos ignorados: 2
```

---

## 📁 Estrutura do projeto

```
organizador-arquivos-python/
│
├── organizador.py
└── README.md
```

---

## 💡 Melhorias futuras

* Adicionar suporte para mais tipos de arquivos
* Criar interface simples
* Permitir escolher a pasta via input

---

