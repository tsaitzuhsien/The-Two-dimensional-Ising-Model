#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

#include <stack>
#include <string>

using namespace std;

int step_r[4] = {0, -1, 0, 1};
int step_c[4] = {1, 0, -1, 0};

void flip(short int *spin, int pos, bool *in_cluster, double T, int L, stack<int> &candidates) {	

	for (int neighbor_id = 0; neighbor_id < 4; neighbor_id++) {
		int neighbor_pos = pos + step_r[neighbor_id] * L + step_c[neighbor_id];

		if (neighbor_pos >= L * L || neighbor_pos < 0)
			continue;
		if (step_c[neighbor_id] != 0 && (neighbor_pos / L) != (pos / L))
			continue;
		if (in_cluster[neighbor_pos])
			continue;
		if (spin[neighbor_pos] != spin[pos])
			continue;

		double flip_prob = 1 - exp(-2 / T);
		if (((double) rand() / RAND_MAX) <= flip_prob) {
			candidates.push(neighbor_pos);
			in_cluster[neighbor_pos] = true;
		}
	}

	return;
}

void wolff(short int *spin, double T, int L, int iterations, int burnout, FILE *fp) {
	bool *in_cluster = (bool *)malloc(L * L * sizeof(bool));

	for (int i = 0; i < burnout; i++) {
		memset(in_cluster, 0, L * L * sizeof(bool));

		int start_pos = rand() % (L * L);
		stack<int> candidates;
		candidates.push(start_pos);
		in_cluster[start_pos] = true;
		
		while (candidates.empty() == false) {
			int current_pos = candidates.top();
			candidates.pop();
			flip(spin, current_pos, in_cluster, T, L, candidates);
		}

		for (int i = 0; i < L * L; i++) {
			if (in_cluster[i]){
				spin[i] *= -1;
//				printf("(%d, %d)\n", i / L, i % L);
			}
		}
	}

	for (int i = 0; i < iterations; i++) {
		memset(in_cluster, 0, L * L * sizeof(bool));

		int start_pos = rand() % (L * L);
		stack<int> candidates;
		candidates.push(start_pos);
		in_cluster[start_pos] = true;
		
		while (candidates.empty() == false) {
			int current_pos = candidates.top();
			candidates.pop();
			flip(spin, current_pos, in_cluster, T, L, candidates);
		}

		int mag = 0;
		for (int i = 0; i < L * L; i++) {
			if (in_cluster[i]){
				spin[i] *= -1;
			}
			mag += spin[i];
		}
		fprintf(fp, "%d\n", mag);
	}

	free(in_cluster);

	return;
}

int main(int argc, char *argv[]) {
	double T = atof(argv[1]);
	int L = atoi(argv[2]);
	int iterations = atoi(argv[3]);
	int burnout = atoi(argv[4]);
	
	short int *spin = (short int *)malloc(L * L * sizeof(short int));

	for (int i = 0; i < L * L; i++) {
		if (rand() % 2 == 1)
			spin[i] = 1;
		else
			spin[i] = -1;
	}

	char file_path[50];
	sprintf(file_path, "./result/%s/%d", argv[2], (int)(T * 1000));
	FILE *output_file = fopen(file_path, "w");
	wolff(spin, T, L, iterations, burnout, output_file);
	fclose(output_file);

	return 0;
}
