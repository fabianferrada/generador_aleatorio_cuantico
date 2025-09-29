from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

numOfRegisters = 32

def sort_result(e):
    return e[1]

qc = QuantumCircuit(numOfRegisters, numOfRegisters)

for index in range(numOfRegisters):
    qc.h(index)

qc.measure_all(add_bits=False)

backend = AerSimulator()

job = backend.run(qc)
job.wait_for_final_state()

result = list(job.result().get_counts().items())
result.sort(reverse=True, key=sort_result)
print(int(result[0][0], 2))
