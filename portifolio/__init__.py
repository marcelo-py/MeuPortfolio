"""import os

caminho_imagens = r".\templates\static\imagens\projetos"
imagens_projetos = []
for raiz, diretorio, arquivos in os.walk(caminho_imagens):
    imagens_projetos.clear()
    for arq in arquivos:
        imagens_projetos.append(os.path.join(raiz[11:], arq))

print(imagens_projetos)"""