import os
import shutil

# Caminho da pasta Downloads
pasta = r"C:\Users\Ph\Downloads"

# Tipos de arquivos
tipos = {
    'Imagens': ['.png', '.jpg', '.jpeg'],
    'Videos': ['.mp4', '.mkv'],
    'Documentos': ['.pdf', '.doc', '.docx', '.txt']
}

movidos = 0
ignorados = 0

# Criar pastas se não existirem
for pasta_nome in tipos:
    caminho = os.path.join(pasta, pasta_nome)
    if not os.path.exists(caminho):
        os.makedirs(caminho)

# Organizar arquivos
for arquivo in os.listdir(pasta):
    caminho_arquivo = os.path.join(pasta, arquivo)

    if os.path.isfile(caminho_arquivo):
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

        if not movido:
            ignorados += 1

print("\n===== RELATÓRIO =====")
print(f"Arquivos movidos: {movidos}")
print(f"Arquivos ignorados: {ignorados}")