import matplotlib.pyplot as plt
import numpy as np

from arch.bootstrap import IIDBootstrap, MovingBlockBootstrap
from utils import read_file, jackknife

Ts = [2.22, 2.225, 2.23, 2.235, 2.24, 2.245, 2.25, 2.255, 2.26, 2.265, 2.27, 2.275, 2.28, 2.285, 2.29, 2.295, 2.30, 2.305, 2.31, 2.315, 2.32, 2.325, 2.33, 2.335, 2.34, 2.345]
Ls = [16, 32, 64, 128, 256]

def magnetic_susceptibility():
	for L in Ls:
		magsus = []
		for T in Ts:
			file_path = f"./result/{L}/{int(T * 1000)}"
			mags = np.array(read_file(file_path))
			mags = np.abs(mags)
			m = np.mean(mags)
			m2 = np.mean(mags ** 2)

			magsus.append((m2 - m ** 2) / (T * (L ** 2)))
		plt.plot(Ts, magsus, label = f"L = {L}")
	plt.legend()
	plt.xlabel("$T/J$")
	plt.ylabel("Magnetic susceptibility")
	plt.savefig("magsus.png")
	plt.clf()

def binder_cumulant():
	for L in Ls:
		binder = []
		for T in Ts:
			file_path = f"./result/{L}/{int(T * 1000)}"
			mags = np.array(read_file(file_path))
			binder_c = jackknife(mags, 10)
			binder.append(binder_c)
		plt.plot(Ts, binder, label = f"L = {L}")
	plt.legend()
	plt.xlabel("$T/J$")
	plt.ylabel("Binder cumulant")
	plt.savefig("binder.png")
	plt.clf()

if __name__ == "__main__":
	magnetic_susceptibility()
	binder_cumulant()
