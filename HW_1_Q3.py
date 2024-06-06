import numpy as np
import matplotlib.pyplot as plt

import PySpice
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
import PySpice.Logging.Logging as Logging
################################################
logger=Logging.setup_logging()

cir = Circuit("2nd_Question")
