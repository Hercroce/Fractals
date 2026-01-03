import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
from typing import Tuple, Optional, List, Literal
import math

import os

Point3 = Tuple[float, float, float]
Vec3   = Tuple[float, float, float]

class DragonCurve:
    def __init__(self, rules=(["right", "left"],["left","right"])):
        self.rules = rules
        pass

    def first_equation(self, z):
        result = ((1 + 1j) * z) /2
        return result
    
    def second_equation(self, z):
        result = 1 - ((1 - 1j) * z) /2
        return result

    def _right_left_invertion(self, way):
        if way == "right":
            return "left"
        
        elif way == "left":
            return "right"
        
    def command_transformation(self, command):
        for first,second in self.rules:
            if first == command:
                return second
            else:
                pass


    def _chain_invertion(self, chain):
        inverted_chain = [self.command_transformation(way) for way in chain]
        inverted_chain.reverse()
        return inverted_chain


    def logic_sequence (self, iterations, initial_command="right"):


        chain_of_command = [initial_command]

        for iteration in range(iterations):
            inverted_chain_of_command = self._chain_invertion(chain_of_command)
            chain_of_command.append(initial_command)
            chain_of_command = chain_of_command+inverted_chain_of_command

        return chain_of_command


    def add_turned_point(self,coords, command="right"):
        if len(coords) < 2:
            raise ValueError("Need at least two coordinates to determine direction")

        # RIGHT turn = -90°, LEFT turn = +90°
        if command == 'right':
            degrees = -90
        else:
            degrees = 90

        x_prev, y_prev = coords[-2]
        x_curr, y_curr = coords[-1]

        dx = x_curr - x_prev
        dy = y_curr - y_prev
        angle = math.atan2(dy, dx)

        # Rotate
        angle += math.radians(degrees)

        new_x = x_curr + math.cos(angle)
        new_y = y_curr + math.sin(angle)

        coords.append((round(new_x, 5), round(new_y, 5)))
        return coords


    def curve_drawing(self, iterations, initial_curve=[(0,0),(1,0)], initial_command="right"):
        chain_of_command = self.logic_sequence(iterations, initial_command=initial_command)
        curve = initial_curve

        for command in chain_of_command:
            curve = self.add_turned_point(curve, command)
        
        return curve
                    

    def _curve_coordinates(self, iterations, coordinates = [0 + 0j, 1 + 0j]):
        
        old_coordinates = []

        for interaction in range(0,iterations):
            new_coordinates = list(set(coordinates) - set(old_coordinates))
            old_coordinates = coordinates.copy()
            
            for coordinate in new_coordinates:
                first_coordinate = self.first_equation(coordinate)
                second_coordinate = self.second_equation(coordinate)

                self.insert_around_target(coordinates,coordinate,second_coordinate,first_coordinate)
        
        return coordinates


class DragonCurve3D(DragonCurve):
    def __init__(self, P_prev: Point3, P_curr: Point3, up: Vec3, rules: List, step: Optional[float] = None):
        super().__init__(rules)
        self.P_prev: Point3 = P_prev
        self.P_curr: Point3 = P_curr
        self.u: Vec3 = self._normalize(up)
        self.step: float = step if step is not None else self._module(self._vec(self.P_prev, self.P_curr))

        # histórico
        self.path: List[Point3] = [self.P_prev, self.P_curr]
        self.frames: List[Tuple[Vec3, Vec3]] = [(self._fwd(), self.u)]  # (forward, up) no ponto atual

        if self._module(self._cross(self._fwd(), self.u)) == 0:
            raise ValueError("up paralelo ao forward; escolha um up não colinear.")

    def advance(self, command, *, step: Optional[float] = None) -> Point3:
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
    

    def advance_many(self, commands: List, *, step: Optional[float] = None) -> List[Point3]:
        out: List[Point3] = []
        for cmd in commands:
            out.append(self.advance(cmd, step=step))
        return out
    
    def state(self) -> tuple[Point3, Point3, Vec3, Vec3]:
        return self.P_prev, self.P_curr, self._fwd(), self.u




    def logic_sequence_3d (self, iterations, initial_command=["up", "right"]):
        chain_of_command = initial_command
    
        for iteration in range(iterations):
            for command in initial_command:
                inverted_chain_of_command = self._chain_invertion(chain_of_command)
                chain_of_command.append(command)
                chain_of_command = chain_of_command+inverted_chain_of_command

        return chain_of_command


    def curve_drawing_3d(self
                         , iterations
                         , initial_command=["up", "right"]
                         , step=None):
        chain_of_command = self.logic_sequence_3d(iterations=iterations, initial_command=initial_command)

        out: List[Point3] = []
        for cmd in chain_of_command:
            out.append(self.advance(cmd, step=step))
            
        return out




    # ---- helpers vetoriais ----
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










