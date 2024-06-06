import numpy as np
import matplotlib.pyplot as plt

import PySpice
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
import PySpice.Logging.Logging as Logging
################################################
logger=Logging.setup_logging()

cir = Circuit("3rd_Question")

# Netlist
r = 5
a = 1
b = cir.gnd
c = 4
d = 3 

cir.V   (1, a, 2     , 15@u_V)
cir.V   (2, c, d     , 12@u_V)
cir.V   ('test', d, 6,  0@u_V)
cir.I   (1,cir.gnd,2 , 75@u_A)
cir.I   (2,d, cir.gnd,  6@u_A)
cir.I   (3,cir.gnd,c , 10@u_A)

cir.CCVS(1, 2, 6,       'Vtest', r)
cir.CCVS(2, 2, cir.gnd, 'Vtest', 6)
cir.VCCS(1, 1, cir.gnd, c, d, 9)
# End Netlist

sim      = cir.simulator(temperature=25,nominal_temperature=25)
analysis = sim.operating_point()

print("\nNode Voltages   : ")
for node in analysis.nodes.values(): 
    print('Node {}: {:5.2f} V'.format(str(node), float(node[0])))

print("\nBranch Currents : ")
for node in analysis.branches.values(): 
    print('Node {}: {:5.2f} A'.format(str(node), float(node[0])))
