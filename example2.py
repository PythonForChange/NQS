from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram,display
from user.index import Index
try:
	Index["maicra"]("Vegetta","vaca")
except:
	print("Error: maicra is not defined or is inaccessible")
