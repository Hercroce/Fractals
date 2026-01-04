from dragon_curve import DragonCurve
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os

dragon = DragonCurve()



os.makedirs("src/frames", exist_ok=True)
filenames = []


# # 🔄 GIF Dragão Único
# # 🔄 GIF Dragão Único
# # 🔄 GIF Dragão Único

gif_name = "dragon_curve"

for n in range(1, 14):
    coords = dragon.curve_drawing(n, initial_curve=[(0,0),(1,0)])
    x, y = zip(*coords)

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, color="black")
    plt.title("Dragon Curve")        
    plt.axis('equal')
    plt.grid(True)
    plt.tick_params(labelbottom=False, labelleft=False)


    filename = f"src/frames/frame_{n:02d}.png"
    plt.savefig(filename)
    filenames.append(filename)
    plt.close()



# # 🔄 GIF Dragão De Cauda Gêmea
# # 🔄 GIF Dragão De Cauda Gêmea
# # 🔄 GIF Dragão De Cauda Gêmea

# gif_name = "dragon_curve_twin_tail"

# for n in range(1, 15):  # Gera passos de 1 a 19
#     coords_1 = dragon.curve_drawing(n,initial_curve=[(0,0),(1,0)])
#     coords_2 = dragon.curve_drawing(n,initial_curve=[(1,0),(0,0)])

#     x1, y1 = zip(*coords_1)
#     x2, y2 = zip(*coords_2)

#     plt.figure(figsize=(6, 6))

#     # Plot das duas curvas no mesmo gráfico
#     plt.plot(x1, y1, color='#7FDBFF', label=f'Passo {n}')       # Azul gelo
#     plt.plot(x2, y2, color='#C70039', label=f'Passo {n}')  # Vermelho cereja

#     # Título principal e legenda
#     plt.title("Curva Dragões de Cauda Gêmea", fontsize=14)
#     plt.suptitle(f"Passo {n}", fontsize=10)
#     plt.legend()

#     # Estética
#     plt.grid(True)
#     plt.axis('equal')

#     # Salvar frame
#     filename = f"frames/frame_{n:02d}.png"
#     plt.savefig(filename)
#     filenames.append(filename)
#     plt.close()


# # 🔄 GIF Dança dos Dois Dragões
# # 🔄 GIF Dança dos Dois Dragões
# # 🔄 GIF Dança dos Dois Dragões

# gif_name = "dragon_curve_two_dragon"

# for n in range(1, 15):  # Gera passos de 1 a 19
#     coords_1 = dragon.curve_drawing(n,initial_curve=[(0,0),(1,0)])
#     coords_2 = dragon.curve_drawing(n,initial_curve=[(1,0),(0,0)], initial_command="left")

#     x1, y1 = zip(*coords_1)
#     x2, y2 = zip(*coords_2)

#     plt.figure(figsize=(6, 6))

#     # Plot das duas curvas no mesmo gráfico
#     plt.plot(x1, y1, color='#7FDBFF', label=f'Passo {n}')       # Azul gelo
#     plt.plot(x2, y2, color='#C70039', label=f'Passo {n}')  # Vermelho cereja

#     # Título principal e legenda
#     plt.title("Curva Dança dos Dois Dragões", fontsize=14)
#     plt.suptitle(f"Passo {n}", fontsize=10)
#     plt.legend()

#     # Estética
#     plt.grid(True)
#     plt.axis('equal')

    # Salvar frame
    # filename = f"src/frames/frame_{n:02d}.png"
    # plt.savefig(filename)
    # filenames.append(filename)
    # plt.close()


# 🔄 GIF Dragões Gêmeos
# 🔄 GIF Dragões Gêmeos
# 🔄 GIF Dragões Gêmeos

# gif_name = "dragon_curve_elemental_dragons"

# for n in range(1, 13):  # Gera passos de 1 a x
#     coords_1 = dragon.curve_drawing(n,initial_curve=[(0,0),(1,0)])
#     coords_2 = dragon.curve_drawing(n,initial_curve=[(0,0),(0,1)])
#     coords_3 = dragon.curve_drawing(n,initial_curve=[(0,0),(-1,0)])
#     coords_4 = dragon.curve_drawing(n,initial_curve=[(0,0),(0,-1)])

#     x1, y1 = zip(*coords_1)
#     x2, y2 = zip(*coords_2)
#     x3, y3 = zip(*coords_3)
#     x4, y4 = zip(*coords_4)



#     plt.figure(figsize=(6, 6))

#     # Plot das duas curvas no mesmo gráfico
#     plt.plot(x1, y1, color='#E63946', label=f'Red Dragon')   
#     plt.plot(x2, y2, color='#7A4E1D', label=f'Brown Dragon') 
#     plt.plot(x3, y3, color='#0096C7', label=f'Blue Dragon')  
#     plt.plot(x4, y4, color='#FFF0A5', label=f'Yellow Dragon')

#     # Título principal e legenda
#     plt.title("Elemental Dragons Curve", fontsize=14)
#     plt.suptitle(f"Step {n}", fontsize=10)
#     plt.legend(fontsize=8)

#     # Estética
#     plt.grid(False)
#     plt.axis('equal')
#     # plt.gca().set_facecolor("#D8F3DC")
    

#     # Salvar frame
#     filename = f"src/frames/frame_{n:02d}.png"
#     plt.savefig(filename)
#     filenames.append(filename)
#     plt.close()

# Cria o GIF
with imageio.get_writer(f"src/images/{gif_name}.gif", mode='I', fps=1) as writer:  # 1 frame por segundo
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)


print(f"GIF salvo como {gif_name}.gif")