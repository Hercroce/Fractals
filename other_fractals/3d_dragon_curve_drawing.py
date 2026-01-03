from dragon_curve import DragonCurve3D
import matplotlib.pyplot as plt

def xyz(path):
    return tuple(zip(*path))

# Inícios dos 3 dragões
pairs = [
    ((0.0, 0.0, 0.0), (0.0, 0.0, 1.0)),
    ((1.0, 0.0, 0.0), (1.0, 0.0, 1.0)),
    ((2.0, 0.0, 0.0), (2.0, 0.0, 1.0)),
]

up0 = (0.0, -1.0, 0.0)  # -Y
rules = [["right", "left"], ["left", "right"], ["up", "down"], ["down", "up"]]

dragons = []
for A, B in pairs:
    d = DragonCurve3D(A, B, up0, step=1.0, rules=rules)
    d.curve_drawing_3d(iterations=2, initial_command=["right", "up"])
    dragons.append(d)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plota cada dragão sem marcadores (só a linha)
for d in dragons:
    xs, ys, zs = xyz(d.path)
    ax.plot(xs, ys, zs)  # <- sem marker

ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.set_title('Três dragões 3D')

# aspecto ~igual considerando todos
all_x = [p[0] for d in dragons for p in d.path]
all_y = [p[1] for d in dragons for p in d.path]
all_z = [p[2] for d in dragons for p in d.path]
xspan = (max(all_x) - min(all_x)) or 1
yspan = (max(all_y) - min(all_y)) or 1
zspan = (max(all_z) - min(all_z)) or 1
ax.set_box_aspect((xspan, yspan, zspan))

plt.show()
