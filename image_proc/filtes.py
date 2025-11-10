from PIL import ImageFilter

def aplicar_filtro_borrado(imagem, raio: float = 2.0):
    """Aplica um desfoque gaussiano."""
    return imagem.filter(ImageFilter.GaussianBlur(raio))

def aplicar_filtro_bordas(imagem):
    """Realça as bordas da imagem."""
    return imagem.filter(ImageFilter.FIND_EDGES)
