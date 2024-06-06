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
cir.R   (1,3,cir.gnd , 1@u_Ohm)
cir.R   (2,1,cir.gnd , 2@u_Ohm)
cir.R   (3, 2, 3     , 2@u_Ohm)
cir.R   (4, 3, 1     , 3@u_Ohm)

cir.I   (1,cir.gnd,2 , 10@u_A)
cir.I   (2, 1, 3     , 5@u_A)

cir.V   (1, 2, 3     , 10@u_V)

cir.CCVS(1, cir.gnd, 2, 3, 1,       2)
cir.VCCS(1, cir.gnd, 1, 3, cir.gnd, 2)
# End Netlist

sim      = cir.simulator(temperature=25,nominal_temperature=25)
analysis = sim.operating_point()

print("\nNode Voltages   : ")
for node in analysis.nodes.values(): 
    print('Node {}: {:5.2f} V'.format(str(node), float(node[0])))

print("\nBranch Currents : ")
for node in analysis.branches.values(): 
    print('Node {}: {:5.2f} A'.format(str(node), float(node[0])))
