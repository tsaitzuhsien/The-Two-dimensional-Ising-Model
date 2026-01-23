import matplotlib.pyplot as plt
import numpy as np

def read_file(file_path: str):
	mags = []
	with open(file_path, "r") as fp:
		line = fp.readline()
		while line:
			mags.append(int(line))
			line = fp.readline()
	return mags

def jackknife(mags: list, bin_n: int):
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
