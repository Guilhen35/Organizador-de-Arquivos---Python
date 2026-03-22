import os
import shutil

# OBSERVACAO:
# O programa detecta automaticamente o usuario do computador e usa a pasta Desktop como padrao.
# Se quiser mudar a pasta padrao, altere a palavra "Desktop" na linha abaixo para outra pasta,
# como por exemplo "Downloads" ou "Documentos".
pasta_padrao = os.path.join(os.path.expanduser("~"), "Desktop")

pasta = input(
    f"Digite o caminho da pasta que deseja organizar [{pasta_padrao}]: "
).strip()

if not pasta:
    pasta = pasta_padrao

if not os.path.exists(pasta):
    print("Caminho invalido!")
    exit()

# Tipos de arquivos
tipos = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Musicas": [".mp3", ".wav", ".flac", ".aac"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executaveis": [".exe", ".msi"],
}

# Pasta para arquivos nao identificados
outros = "Outros"

movidos = 0
ignorados = 0

# Criar pastas de destino
for pasta_nome in list(tipos.keys()) + [outros]:
    caminho = os.path.join(pasta, pasta_nome)
    if not os.path.exists(caminho):
        os.makedirs(caminho)

# Organizar arquivos
for arquivo in os.listdir(pasta):
    caminho_arquivo = os.path.join(pasta, arquivo)

    # Ignora pastas
    if not os.path.isfile(caminho_arquivo):
        continue

    movido = False

    for pasta_nome, extensoes in tipos.items():
        if any(arquivo.lower().endswith(ext) for ext in extensoes):
            destino = os.path.join(pasta, pasta_nome, arquivo)

            if not os.path.exists(destino):
                shutil.move(caminho_arquivo, destino)
                print(f"Movendo: {arquivo} -> {pasta_nome}")
                movidos += 1
            else:
                print(f"Ja existe: {arquivo} em {pasta_nome}")
                ignorados += 1

            movido = True
            break

    # Se nao encontrou tipo, vai para Outros
    if not movido:
        destino = os.path.join(pasta, outros, arquivo)

        if not os.path.exists(destino):
            shutil.move(caminho_arquivo, destino)
            print(f"Movendo: {arquivo} -> {outros}")
            movidos += 1
        else:
            print(f"Ja existe: {arquivo} em {outros}")
            ignorados += 1

# Relatorio final
print("\n===== RELATORIO =====")
print(f"Arquivos movidos: {movidos}")
print(f"Arquivos ignorados: {ignorados}")
