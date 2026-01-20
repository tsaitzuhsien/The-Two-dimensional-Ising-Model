import matplotlib.pyplot as plt
import numpy as np

Ts = [2.22, 2.225, 2.23, 2.235, 2.24, 2.245, 2.25, 2.255, 2.26, 2.265, 2.27, 2.275, 2.28, 2.285, 2.29, 2.295, 2.30, 2.305, 2.31, 2.315, 2.32, 2.325, 2.33, 2.335, 2.34, 2.345]
Ls = [16, 32, 64, 128, 256]

def read_file(file_path: str):
	mags = []
	with open(file_path, "r") as fp:
		line = fp.readline()
		while line:
			mags.append(int(line))
			line = fp.readline()
	return mags

def bin_data(data, bin_size: int):
	bin_results = []
	bin_n = (len(data) + bin_size - 1) // bin_size

	for i in range(bin_n):
		head = i * bin_size
		tail = min((i + 1) * bin_size, len(data))
		bin_results.append(np.mean(data[head:tail]))
	
	return np.array(bin_results)

def binder_jackknife(mags: list, bin_n: int):
	bin_size = len(mags) // bin_n
	temp_bin = []
	mag_bin = []
	mag_sq_bin = []
	mag_quad_bin = []
	for i in range(len(mags)):
		temp_bin.append(mags[i])
		if (i + 1) % bin_size == 0:
			mag_bin.append(np.mean(temp_bin))
			mag_sq_bin.append(np.mean(np.array(temp_bin) ** 2))
			mag_quad_bin.append(np.mean(np.array(temp_bin) ** 4))
			temp_bin.clear()
	
	mag_jk = []
	mag_sq_jk = []
	mag_quad_jk = []
	for discard_bin in range(bin_n):
		avg = []
		sq = []
		quad = []
		for i in range(bin_n):
			if i != discard_bin:
				avg.append(mag_bin[i])
				sq.append(mag_sq_bin[i])
				quad.append(mag_quad_bin[i])
		mag_jk.append(np.mean(avg))
		mag_sq_jk.append(np.mean(sq))
		mag_quad_jk.append(np.mean(quad))
	
	binder_jk = [1 - mag_quad_jk[i] / (3 * (mag_sq_jk[i] ** 2)) for i in range(len(mag_jk))]

	return np.mean(binder_jk)

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

def binder_cumulant(bin_size: int):
	for L in Ls:
		binder = []
		for T in Ts:
			file_path = f"./result/{L}/{int(T * 1000)}"
			mags = np.array(read_file(file_path))
			binder_c = binder_jackknife(mags, 10)
			binder.append(binder_c)
		plt.plot(Ts, binder, label = f"L = {L}")
	plt.legend()
	plt.xlabel("$T/J$")
	plt.ylabel("Binder cumulant")
	plt.savefig("binder.png")
	plt.clf()

if __name__ == "__main__":
	bin_size = 5
	magnetic_susceptibility()
#	binder_cumulant(bin_size)
