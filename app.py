from PIL import Image
import os

# Pasta contendo as imagens
pasta_imagens = "./raw_files"

# Pasta de saída para os PDFs
pasta_saida = "./pdf_folder"

# Lista de todas as imagens na pasta
imagens = [f for f in os.listdir(pasta_imagens) if f.endswith('png')]

# Garante que a pasta de saída exista, se não, a cria
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# Loop através de cada imagem
for imagem_nome in imagens:
    # Caminho completo para a imagem de entrada
    caminho_entrada = os.path.join(pasta_imagens, imagem_nome)

    # Nome do arquivo sem a extensão para usar na imagem de saída
    nome_sem_extensao = os.path.splitext(imagem_nome)[0]

    # Caminho completo para o PDF de saída
    caminho_saida = os.path.join(pasta_saida, nome_sem_extensao + ".pdf")

    # Abre a imagem usando o Pillow
    imagem = Image.open(caminho_entrada)

    # Redimensiona a imagem (substitua 800 e 600 pelos tamanhos desejados)
    nova_dimensao = (900, 800)
    imagem_redimensionada = imagem.resize(nova_dimensao)

    # Salva a imagem redimensionada como PDF
    imagem_redimensionada.save(caminho_saida, "PDF", resolution=100.0)

print('Conversão para PDF com redimensionamento concluída!')
