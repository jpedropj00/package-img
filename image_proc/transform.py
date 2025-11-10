def redimensionar(imagem, largura: int, altura: int):
    """Redimensiona a imagem para as dimensões dadas."""
    return imagem.resize((largura, altura))

def rotacionar(imagem, angulo: float):
    """Rotaciona a imagem no sentido horário pelo ângulo especificado."""
    return imagem.rotate(-angulo)
