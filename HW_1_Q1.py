import numpy as np
import matplotlib.pyplot as plt

import PySpice
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
import PySpice.Logging.Logging as Logging
################################################
logger=Logging.setup_logging()

cir = Circuit("1st_Question")

# Netlist
cir.R   (1,1,2       , 5@u_Ohm)
cir.R   (2,3,4       , 7@u_Ohm)
cir.R   (3,5,cir.gnd , 20@u_Ohm)
cir.R   (4,4,cir.gnd , 9@u_Ohm)

cir.I   (1,cir.gnd,1 , 5@u_A)
cir.I   (2,cir.gnd,3 , 13@u_A)

cir.V   (1,2,cir.gnd , 20@u_V)
cir.V   (2,2,3       , 5@u_V)

cir.VCVS(1, cir.gnd, 5, 3, cir.gnd, 8)
# End Netlist

sim      = cir.simulator(temperature=25,nominal_temperature=25)
analysis = sim.operating_point()

print("\nNode Voltages   : ")
for node in analysis.nodes.values(): 
    print('Node {}: {:5.2f} V'.format(str(node), float(node[0])))

print("\nBranch Currents : ")
for node in analysis.branches.values(): 
    print('Node {}: {:5.2f} A'.format(str(node), float(node[0])))