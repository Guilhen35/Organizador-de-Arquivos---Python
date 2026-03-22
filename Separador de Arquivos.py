import os
import shutil

# Usuário escolhe a pasta
pasta = input("Digite o caminho da pasta que deseja organizar: ")

if not os.path.exists(pasta):
    print("❌ Caminho inválido!")
    exit()

# Tipos de arquivos
tipos = {
    'Imagens': ['.png', '.jpg', '.jpeg'],
    'Videos': ['.mp4', '.mkv'],
    'Documentos': ['.pdf', '.doc', '.docx', '.txt']
}

# Pasta para arquivos não identificados
outros = "Outros"

movidos = 0
ignorados = 0

# Criar pastas
for pasta_nome in list(tipos.keys()) + [outros]:
    caminho = os.path.join(pasta, pasta_nome)
    if not os.path.exists(caminho):
        os.makedirs(caminho)

# Organizar arquivos
for arquivo in os.listdir(pasta):
    caminho_arquivo = os.path.join(pasta, arquivo)

    # Ignorar pastas
    if not os.path.isfile(caminho_arquivo):
        continue

    movido = False

    for pasta_nome, extensoes in tipos.items():
        for ext in extensoes:
            if arquivo.lower().endswith(ext):
                destino = os.path.join(pasta, pasta_nome, arquivo)

                if not os.path.exists(destino):
                    shutil.move(caminho_arquivo, destino)
                    print(f"Movendo: {arquivo} → {pasta_nome}")
                    movidos += 1
                else:
                    print(f"Já existe: {arquivo}")
                    ignorados += 1

                movido = True
                break

        if movido:
            break

    # Se não encontrou tipo
    if not movido:
        destino = os.path.join(pasta, outros, arquivo)

        if not os.path.exists(destino):
            shutil.move(caminho_arquivo, destino)
            print(f"Movendo: {arquivo} → Outros")
            movidos += 1
        else:
            ignorados += 1

# Relatório final
print("\n===== RELATÓRIO =====")
print(f"Arquivos movidos: {movidos}")
print(f"Arquivos ignorados: {ignorados}")




