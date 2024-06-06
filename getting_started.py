'''
installation on cmd or an ubuntu terminal using pip:
1)pip install PySpice
2)pyspice-post-installation --install-ngspice-dll
'''
import numpy as np
import matplotlib.pyplot as plt

import PySpice
from   PySpice.Spice.Netlist import Circuit
from   PySpice.Unit import *
import PySpice.Logging.Logging as Logging

logger=Logging.setup_logging()

#init circuit
cir=Circuit("test")

#creating the circuit
cir.R   (1,1,2      , 1@u_Ohm)
cir.R   (2,2,cir.gnd, 1@u_Ohm)
cir.R   (3,2,3      , 1@u_Ohm)
cir.R   (4,3,cir.gnd, 1@u_Ohm)
cir.I   (1,2,3      , 2@u_A)
cir.V   (1,1,cir.gnd, 20@u_V)

cir.VCCS(1,cir.gnd,3,2,cir.gnd,3)

sim      = cir.simulator(temperature=25,nominal_temperature=25)
analysis = sim.operating_point()

print("\nNode Voltages   : ")
for node in analysis.nodes.values(): 
    print('Node {}: {:5.2f} V'.format(str(node), float(node[0])))

print("\nBranch Currents : ")
for node in analysis.branches.values(): 
    print('Node {}: {:5.2f} A'.format(str(node), float(node[0])))
