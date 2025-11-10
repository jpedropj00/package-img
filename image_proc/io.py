from PIL import Image

def carregar_imagem(caminho: str):
    """Carrega uma imagem de um arquivo."""
    try:
        return Image.open(caminho)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

def salvar_imagem(imagem, caminho: str):
    """Salva uma imagem em disco."""
    imagem.save(caminho)
