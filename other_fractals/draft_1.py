from __future__ import annotations
from typing import Tuple, Optional, List, Literal
import math

Point3 = Tuple[float, float, float]
Vec3   = Tuple[float, float, float]

class SegmentWalker3D:
    # Alias de comando encapsulado na classe
    

    def __init__(
        self,
        P_prev: Point3,
        P_curr: Point3,
        up: Vec3,
        step: Optional[float] = None,
        commands: Optional[List[Command]] = None,
        autorun: bool = False,   # mantido para possível uso futuro; default = False
    ):
        self.P_prev: Point3 = P_prev
        self.P_curr: Point3 = P_curr
        self.u: Vec3 = self._normalize(up)
        self.step: float = step if step is not None else self._module(self._vec(self.P_prev, self.P_curr))

        # histórico
        self.path: List[Point3] = [self.P_prev, self.P_curr]
        self.frames: List[Tuple[Vec3, Vec3]] = [(self._fwd(), self.u)]  # (forward, up) no ponto atual

        # fila de comandos (não executa)
        self.commands: List[SegmentWalker3D.Command] = list(commands) if commands else []

        if self._module(self._cross(self._fwd(), self.u)) == 0:
            raise ValueError("up paralelo ao forward; escolha um up não colinear.")

        # opcional: não roda porque autorun=False por padrão
        if autorun and self.commands:
            self.advance_many(self.commands)  # executaria, mas só se autorun=True

    # ---------- API ----------
    def advance(self, command: Command, *, step: Optional[float] = None) -> Point3:
        f = self._fwd()
        u = self.u
        r = self._normalize(self._cross(f, u))

        cmd = command.lower()
        if cmd == "right":
            d = r;              f_next, u_next = r, u
        elif cmd == "left":
            d = (-r[0], -r[1], -r[2]);  f_next, u_next = d, u
        elif cmd == "down":
            d = (-u[0], -u[1], -u[2]);  f_next, u_next = d, f
        elif cmd == "up":
            d = u;              f_next, u_next = d, (-f[0], -f[1], -f[2])
        else:
            raise ValueError("Comando inválido. Use 'right', 'left', 'up' ou 'down'.")

        dist = step if step is not None else self.step
        P_next = self._p_plus_v(self.P_curr, self._scale(d, dist))

        # atualiza estado + histórico
        self.P_prev, self.P_curr = self.P_curr, P_next
        self.u = self._normalize(u_next)
        self.step = dist
        self.path.append(P_next)
        self.frames.append((self._fwd(), self.u))
        return P_next

    def advance_many(self, commands: List[Command], *, step: Optional[float] = None) -> List[Point3]:
        out: List[Point3] = []
        for cmd in commands:
            out.append(self.advance(cmd, step=step))
        return out

    def state(self) -> tuple[Point3, Point3, Vec3, Vec3]:
        return self.P_prev, self.P_curr, self._fwd(), self.u

    # ---------- Helpers ----------
    @staticmethod
    def _vec(A: Point3, B: Point3) -> Vec3:
        return (B[0]-A[0], B[1]-A[1], B[2]-A[2])

    @staticmethod
    def _p_plus_v(P: Point3, v: Vec3) -> Point3:
        return (P[0]+v[0], P[1]+v[1], P[2]+v[2])

    @staticmethod
    def _scale(a: Vec3, s: float) -> Vec3:
        return (a[0]*s, a[1]*s, a[2]*s)

    @staticmethod
    def _module(a: Vec3) -> float:
        return math.sqrt(a[0]**2 + a[1]**2 + a[2]**2)

    def _normalize(self, a: Vec3) -> Vec3:
        m = self._module(a)
        if m == 0:
            raise ValueError("Vetor de módulo zero.")
        return (a[0]/m, a[1]/m, a[2]/m)

    @staticmethod
    def _cross(a: Vec3, b: Vec3) -> Vec3:
        return (
            a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0],
        )

    def _fwd(self) -> Vec3:
        return self._normalize(self._vec(self.P_prev, self.P_curr))


if __name__ == "__main__":
    # estado inicial
    A: Point3 = (0.0, 0.0, 0.0)
    B: Point3 = (0.0, 0.0, 1.0)
    up0: Vec3 = (0.0, -1.0, 0.0)  # -Y

    walker = SegmentWalker3D(A, B, up0, step=1.0)

    # 6 comandos de exemplo
    commands: List[Command] = ["right", "down", "down", "left", "up", "right"]
    walker.advance_many(commands)

    # plot 3D
    xs, ys, zs = zip(*walker.path)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, marker='o')
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.set_title('Caminho 3D (6 comandos)')

    # aspecto ~igual entre eixos
    xspan = max(xs) - min(xs) or 1
    yspan = max(ys) - min(ys) or 1
    zspan = max(zs) - min(zs) or 1
    ax.set_box_aspect((xspan, yspan, zspan))

    plt.show()
