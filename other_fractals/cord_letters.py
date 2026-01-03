import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

class CordLetters():
    """
    Uma classe onde cada propriedade retorna as coordenadas de uma letra do alfabeto
    como um array NumPy no formato (2, N).
    """
    @property
    def a(self): return np.array([[0,0.5,1,1.5,0.5,1.5,2],[0,1,2,1,1,1,0]])
    @property
    def b(self): return np.array([[0,0,1,1.5,1,0,1,1.5,1,0],[0,2,2,1.5,1,1,1,0.5,0,0]])
    @property
    def c(self): return np.array([[2,1,0,0,1,2],[1.8,2,1.5,0.5,0,0.2]])
    @property
    def d(self): return np.array([[0,0,1.5,2,2,1.5,0],[0,2,2,1.5,0.5,0,0]])
    @property
    def e(self): return np.array([[2,0,0,1.5,0,2],[2,2,1,1,0,0]])
    @property
    def f(self): return np.array([[2, 0, 0, 1.5, 0, 0], [2, 2, 1, 1, 1, 0]]) # Simplificado para evitar erro de shape
    @property
    def g(self): return np.array([[2,1,0,0,1,2,2,1],[1.8,2,1.5,0.5,0,0.2,1,1]])
    @property
    def h(self): return np.array([[0,0,0,2,2,2],[0,2,1,1,2,0]])
    @property
    def i(self): return np.array([[1,1],[0,2]])
    @property
    def j(self): return np.array([[2,2,1,0,0],[2,0.5,0,0.5,1]])
    @property
    def k(self): return np.array([[0,0,2,0.5,2],[0,2,2,1,0]])
    @property
    def l(self): return np.array([[0,0,2],[2,0,0]])
    @property
    def m(self): return np.array([[0,0,1,2,2],[0,2,1,2,0]])
    @property
    def n(self): return np.array([[0,0,2,2],[0,2,0,2]])
    @property
    def o(self): return np.array([[0,2,2,0,0],[0,0,2,2,0]])
    @property
    def p(self): return np.array([[0,0,2,2,0],[0,2,2,1,1]])
    @property
    def q(self): return np.array([[0,2,2,0,0,1.5,2.5],[0,0,2,2,0,0.5,-0.5]])
    @property
    def r(self): return np.array([[0,0,2,2,0,2],[0,2,2,1,1,0]])
    @property
    def s(self): return np.array([[2,0,0,2,2,0],[2,2,1,1,0,0]])
    @property
    def t(self): return np.array([[0,2,1,1],[2,2,2,0]])
    @property
    def u(self): return np.array([[0,0,1,2,2],[2,0.5,0,0.5,2]])
    @property
    def v(self): return np.array([[0,1,2],[2,0,2]])
    @property
    def w(self): return np.array([[0,0.5,1,1.5,2],[2,0,1,0,2]])
    @property
    def x(self): return np.array([[0,2,1,1,0,2],[2,0,1,1,0,2]])
    @property
    def y(self): return np.array([[0,1,2,1,1],[2,1,2,1,0]])
    @property
    def z(self): return np.array([[0,2,0,2],[2,2,0,0]])



def plot_letras_alinhadas(
    gerador_letras: CordLetters,
    letras_a_plotar: list[str],
    ax: plt.Axes,
    colorido: bool = True,
    mostrar_legenda: bool = True
):
    """
    Plota uma sequência de letras lado a lado em um eixo Matplotlib. (Versão Final)
    """
    cores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    borda_direita_anterior = 0.0

    for i, nome_letra in enumerate(letras_a_plotar):
        try:
            coords_originais = getattr(gerador_letras, nome_letra.lower())
        except AttributeError:
            print(f"Aviso: A letra '{nome_letra}' não foi encontrada. Pulando.")
            continue

        borda_esquerda_atual = coords_originais[0].min()
        deslocamento_x = borda_direita_anterior - borda_esquerda_atual

        coords_deslocadas = coords_originais.copy()
        coords_deslocadas[0] = coords_deslocadas[0] + deslocamento_x

        cor_atual = cores[i % len(cores)] if colorido else 'C0'

        ax.plot(
            coords_deslocadas[0],
            coords_deslocadas[1],
            marker='o',
            linestyle='-',
            label=f'Letra {nome_letra.upper()}',
            color=cor_atual
        )

        borda_direita_anterior = coords_deslocadas[0].max() + 0.5 # Adiciona um pequeno espaço

    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_aspect('equal', adjustable='box')
    
    if mostrar_legenda:
        ax.legend()


# Criar a instância da classe com o alfabeto completo
gerador_alfabeto = CordLetters()

# Criar a lista de todas as letras
letras_do_alfabeto = list("abcdefghijklmnopqrstuvwxyz")

# Configurar a figura - precisa ser bem larga para caber tudo!
fig, ax = plt.subplots(figsize=(28, 3))
ax.set_title('Alfabeto Completo Alinhado', fontsize=18)

# Chamar a função para plotar o alfabeto inteiro
# Usaremos colorido=True para distinguir as letras e mostrar_legenda=False para não poluir
plot_letras_alinhadas(
    gerador_letras=gerador_alfabeto,
    letras_a_plotar=letras_do_alfabeto,
    ax=ax,
    colorido=True,
    mostrar_legenda=False # Desativar a legenda
)

plt.tight_layout()
plt.show()











# # --- Como Usar e as Vantagens na Prática ---

# # 1. Instancie a classe
# letras_np = CordLetters()

# # 2. Acesse uma letra. O objeto retornado é um array NumPy.
# coords_h = letras_np.h
# print("--- Coordenadas da Letra H (como array NumPy) ---")
# print(coords_h)
# print(f"Tipo do objeto: {type(coords_h)}")
# print(f"Shape (formato) do array: {coords_h.shape}")


# # 3. Realize operações matemáticas de forma simples e eficiente

# # Exemplo 1: Deixar a letra 'H' duas vezes maior (escala)
# h_maior = coords_h * 2
# print("\n--- Letra H com o dobro do tamanho ---")
# print(h_maior)

# # Exemplo 2: Mover (transladar) a letra 'H' 5 unidades para a direita (eixo X) e 3 para cima (eixo Y)
# # Criamos um vetor de translação e o somamos diretamente ao array de coordenadas.
# vetor_movimento = np.array([[5],  # Adiciona 5 a todas as coordenadas X
#                             [3]]) # Adiciona 3 a todas as coordenadas Y

# h_movida = coords_h + vetor_movimento
# print("\n--- Letra H movida para a direita e para cima ---")
# print(h_movida)