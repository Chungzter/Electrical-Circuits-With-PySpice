import numpy as np
import matplotlib.pyplot as plt

import PySpice
import PySpice.Logging.Logging as Logging
from PySpice.Plot.BodeDiagram import bode_diagram
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
import math

pi=math.pi

logger=Logging.setup_logging()

cir=Circuit(" ")

cir.SinusoidalVoltageSource(1,1,cir.gnd,amplitude=5@u_V)

r=cir.R(1,1,2,5@u_kOhm)
c=cir.C(1,2,cir.gnd,3@u_uF)

br=1/(2*pi*float(r.resistance)*float(c.capacitance))

sim=cir.simulator(temperature=25,nominal_temperature=25)
analysis=sim.ac(start_frequency=1@u_Hz,
                stop_frequency=1@u_MHz,number_of_points=100,
                variation="dec")

f=np.array([float(i) for i in analysis.frequency])
g=np.array([20*np.log10(abs(float(analysis["2"][i]))) for i in range(len(analysis.frequency))])
phase=np.angle(analysis["2"],deg=True)


plt.semilogx(f,g)

plt.semilogx(f,phase)
