from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
import numpy as np

qc = QuantumCircuit(2)

qc.h(0)

qc.cx(0,1)

qc.measure_all()

qc.draw()

#U = Operator(qc)

# Show the results
#U.data
