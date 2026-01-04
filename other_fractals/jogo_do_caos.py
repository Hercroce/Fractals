import numpy as np
import matplotlib.pyplot as plt
import random

def chaos_game_sierpinski(num_points=50000):
    """
    Gera o Triângulo de Sierpinski usando o método do "Jogo do Caos".

    Args:
        num_points (int): O número de pontos a serem gerados para formar a imagem.

    Returns:
        numpy.ndarray: Um array com as coordenadas (x, y) dos pontos.
    """
    # 1. Definir os três vértices do triângulo principal
                #  FLAG
                #  FLAG
                #  FLAG
    vertices = np.array([
        [0, 0],      # Vértice A
        [1, 0],      # Vértice B
        [0.5, np.sqrt(3)/2] # Vértice C (para formar um triângulo equilátero)
    ])
                #  FLAG
                #  FLAG
                #  FLAG

    # Inicializa uma lista para armazenar os pontos gerados
    points = np.zeros((num_points, 2))
    
    # 2. Escolher um ponto de partida dentro do triângulo
    # (Uma forma simples é começar em um dos vértices)
    points[0] = vertices[0]

    # 3. Iterar para gerar os pontos restantes
    for i in range(1, num_points):
        # a. Escolher um vértice aleatoriamente
        random_vertex = vertices[random.randint(0, 2)]
        
        # b. Mover o ponto atual para a metade do caminho até o vértice escolhido
                #  FLAG
                #  FLAG
                #  FLAG

        points[i] = (points[i-1] + random_vertex) / 2.0
                #  FLAG
                #  FLAG
                #  FLAG
        
    return points

if __name__ == '__main__':
    print("Gerando pontos para o Triângulo de Sierpinski via Jogo do Caos...")
    
    # Gera as coordenadas dos pontos
    # Aumentar num_points para uma imagem mais densa e detalhada
                    #  FLAG
                    #  FLAG
                    #  FLAG
    num_points=50000
    sierpinski_points = chaos_game_sierpinski(num_points=num_points)
                    #  FLAG
                    #  FLAG
                    #  FLAG
                    #  FLAG

    print("Geração concluída. Exibindo a imagem.")

    # --- VISUALIZAÇÃO ---
    plt.figure(figsize=(10, 8))
    
    # Extrai as coordenadas x e y para o scatter plot
    x_coords = sierpinski_points[:, 0]
    y_coords = sierpinski_points[:, 1]
    
    # plt.scatter é ideal para plotar uma nuvem de pontos.
    # 's' é o tamanho do ponto, 'alpha' é a transparência.
    # Valores pequenos criam uma aparência de "poeira" que define bem o fractal.
    plt.scatter(x_coords, y_coords, s=0.1, color='blue')
    
    plt.title(f'Sierpinski Triangle (Chaos Game - {num_points} points)')
    plt.axis('equal') # Garante que as proporções x e y sejam as mesmas
    plt.axis('off')   # Remove os eixos para uma visualização limpa
    
    plt.savefig('sierpinski_chaos_game.png', dpi=300)
    plt.show()