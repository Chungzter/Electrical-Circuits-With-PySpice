import numpy as np
import matplotlib.pyplot as plt

import PySpice
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
import PySpice.Logging.Logging as Logging

logger=Logging.setup_logging()

cir=Circuit(" ")

cir.V(1,1,2,5@u_V)
cir.R(1,1,3,4@u_Ohm)
cir.R1.plus.add_current_probe(cir)
cir.R(2,3,cir.gnd,5@u_Ohm)
cir.R2.plus.add_current_probe(cir)
cir.R(8,2,cir.gnd,6@u_F)
cir.R8.plus.add_current_probe(cir)
cir.R(4,3,4,8@u_Ohm)
cir.R4.plus.add_current_probe(cir)
cir.R(5,cir.gnd,5,15@u_Ohm)
cir.R5.plus.add_current_probe(cir)
cir.I(1,4,5,5@u_A)


sim=cir.simulator(temperature=25,nominal_temperature=25)
#analysis=sim.operating_point()
analysis=sim.transient(step_time=0.001@u_ns,end_time=1000@u_ns)

#current=np.array(analysis.branches.values())
#volt=np.array(analysis.nodes.values())

#plt.grid()
#plt.plot(analysis.time*1e3,analysis["2"])
