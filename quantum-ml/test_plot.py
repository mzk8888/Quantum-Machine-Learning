import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

losses = [0.9, 0.8, 0.7, 0.6]

save_path = r"C:\Users\81806\quantum-ml\test_curve.png"

plt.plot(losses, marker="o")
plt.title("Test Save Plot")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)

plt.savefig(save_path, dpi=300, bbox_inches="tight")
plt.close()

print(f"✅ テスト保存: {save_path}")
