import numpy as np
from PIL import Image
from matplotlib.pyplot import get_cmap

# função fc
def fc(z, c):
    return z ** 2 + c

# Função de teste mandelbot
def is_Mandelbrot(c, N):
    M = 2  # valor máximo de convergencia das orbitas
    z = 0  # valor inicial da orbita
    n = 0  # valor de inicio da iteração
    while n < N:
        z = fc(z, c)
        modulo = abs(z)
        if modulo > M:
            break
        else:
            n += 1

    if n == N:
        return True, 0
    else:
        return False, N - n

# Vetorizando o is_mandelbrot
v_is_Mandelbrot = np.vectorize(is_Mandelbrot)

# Definido as partes real e imaginária de um pixel e testando Mandelbrot
def pix_to_z(lp, cp):
    a = -2 + (cp * 3) / 900  # parte real, cp é a coluna do pixel
    b = -2 + (lp * 4) / (1200)  # parte imaginária, lp é a linha do pixel
    c = a + b * 1j  # complexo

    Tipo, conv = v_is_Mandelbrot(c, 100)  # Testa se é Mandelbrot e já dá o numero de iterações

    return conv

# gerando a matriz base da imagem e a normalizando
matriz_base = np.fromfunction(pix_to_z, (1200, 900))
matriz_normalizada = matriz_base / 100
seca = (matriz_normalizada * 255).astype(np.uint8)  # sem degradê em RGB aqui o degradê está em tons de cinza

# Mapeando as cores e gerando o degradê
mapa = get_cmap('turbo')  # Pega um color map em RGB

figura_Mapeada = mapa(matriz_normalizada) # Aplica as cores do mapa nos elementos da matriz normalizada (cada número da matriz se associa a uma cor ou tom dessa cor)

imagem_degrade = (figura_Mapeada * 255).astype(np.uint8) # Figura final com degradê

# Visualizando
imagem_final = Image.fromarray(seca)  # pra ver a com degradê troca seca pela imagem_degrade

imagem_final.show()

