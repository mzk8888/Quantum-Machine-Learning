from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

service = QiskitRuntimeService(channel="ibm_quantum_platform")
backend = service.backend("ibm_brisbane")

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

print("Quantum Circuit:")
print(qc.draw())

qc_transpiled = transpile(qc, backend)

sampler = Sampler(backend)
job = sampler.run([qc_transpiled])
result = job.result()

# 結果を取り出して辞書形式に変換
counts = result[0].data.c.get_counts()

print("✅ 実行結果 (counts):")
print(counts)

# ヒストグラムで可視化
plot_histogram(counts)
plt.savefig("bell_result.png", dpi=300)
plt.show()




