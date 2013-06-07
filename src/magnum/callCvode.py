#!/usr/bin/python
from magnum import *
from math import pi, cos, sin
import magnum.magneto as m
from llgDiffEq import *
import gc

world = World(RectangularMesh((8, 8, 1), (  5e-9,    5e-9, 3.0e-9)), Body("all", Material.Py(alpha=0.02)))

def state0(field, pos): 
    u = abs(pi*(pos[0]/field.mesh.size[0]-0.5)) / 2.0
    return 8e5 * cos(u), 8e5 * sin(u), 0

# Relax to get initial state for SP4
solver = create_solver(world, [StrayField, ExchangeField], log=True, do_precess=False, evolver="cvode", eps_abs=1e-4, eps_rel=1e-2, step_size=1e-11)
solver.state.M = state0
solver.state.alpha = 0.5
solver.relax(1.0)
#solver.solve(condition.Time(1.0e-9))

#llg = LlgDiffEq(solver.state)
#c = m.Cvode(llg)
#writeOMF("test1.omf",solver.state.M)
#i = c.evolve()
#print("fertig")
#print(i)
#writeOMF("test2.omf",solver.state.M)