import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    """
    Calcula o número de iterações para um ponto c escapar.

    Args:
        c (complex): O número complexo a ser testado.
        max_iter (int): O número máximo de iterações.

    Returns:
        int: O número de iterações até a fuga. Retorna 0 se o ponto
             pertence ao conjunto (não escapou).
    """
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    
    # Se o loop terminou por atingir max_iter, o ponto está no conjunto
    if n == max_iter:
        return 0
        
    return n

def generate_fractal(width, height, x_min, x_max, y_min, y_max, max_iter):
    """
    Gera a matriz de iterações para a imagem do fractal.

    Args:
        width (int): Largura da imagem em pixels.
        height (int): Altura da imagem em pixels.
        x_min, x_max (float): Limites do eixo real no plano complexo.
        y_min, y_max (float): Limites do eixo imaginário no plano complexo.
        max_iter (int): Número máximo de iterações.

    Returns:
        numpy.ndarray: Uma matriz 2D com os valores de iteração para cada pixel.
    """
    # Cria arrays para os eixos real (r) e imaginário (i)
    r = np.linspace(x_min, x_max, width)
    i = np.linspace(y_min, y_max, height)
    
    # Inicializa a imagem como uma matriz de zeros
    image = np.zeros((height, width))

    # Itera sobre cada pixel
    for x in range(width):
        for y in range(height):
            if x % 10 == 0:
                print(f"Processando coluna {x}/{width}...")

            # Converte as coordenadas do pixel (x, y) para um número complexo c
            c = complex(r[x], i[y])
            
            # Calcula o número de iterações e armazena na matriz da imagem
            image[y, x] = mandelbrot(c, max_iter)
            
    return image

if __name__ == '__main__':
    # --- PARÂMETROS DE CONFIGURAÇÃO ---
    # ALTERAR GRADUALMENTE
    IMG_WIDTH = 300 
    IMG_HEIGHT = 300

    
    # Limites do plano complexo (experimente mudar para dar "zoom")
    X_MIN, X_MAX = -2.0, 1.0
    Y_MIN, Y_MAX = -1.5, 1.5

    # Qualidade do fractal (valores mais altos geram mais detalhes, mas são mais lentos)
    # ALTERAR GRADUALMENTE
    MAX_ITERATIONS = 50
    
    print("Gerando o fractal de Mandelbrot... Isso pode levar alguns momentos.")
    
    # Gera a matriz de dados do fractal
    fractal_image = generate_fractal(IMG_WIDTH, IMG_HEIGHT, X_MIN, X_MAX, Y_MIN, Y_MAX, MAX_ITERATIONS)

    print("Geração concluída. Exibindo a imagem.")

    # --- VISUALIZAÇÃO ---
    plt.figure(figsize=(10, 10))
    # 'imshow' exibe dados de uma matriz como uma imagem.
    # O parâmetro 'cmap' define o mapa de cores a ser usado. 'hot', 'viridis', 'plasma' são boas opções.
    plt.imshow(fractal_image.T, cmap='hot', extent=[X_MIN, X_MAX, Y_MIN, Y_MAX])
    plt.colorbar(label='Iterações para escapar')
    plt.title('Conjunto de Mandelbrot')
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginária')
    
    # Salva a imagem em um arquivo
    plt.savefig('mandelbrot_fractal.png', dpi=300)
    
    plt.show()