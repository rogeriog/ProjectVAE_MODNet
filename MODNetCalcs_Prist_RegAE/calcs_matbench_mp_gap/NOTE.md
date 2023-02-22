This folder contains results from MODNet calculations on the matbench_mp_gap dataset using the best regular autoencoder, with different compression ratios. Specifically, the MODNet_mp_gap subfolders contain calculations performed with an autoencoder architecture N-2.2N-b  where N is the number of input features and b is the bottleneck, with compression ratios of 100, 40, 60, and 80, respectively. Additionally, a MODNet_mp_gap_filtered subfolder contains calculations performed on a filtered set of the dataset that matches the autoencoder features.


File	Final Score	Difference
MODNet_mp_gap_2.2f_100/log.txt	0.254	-0.7%
MODNet_mp_gap_2.2f_40/log.txt	0.328	20.6%
MODNet_mp_gap_2.2f_60/log.txt	0.337	24.9%
MODNet_mp_gap_2.2f_80/log.txt	0.281	3.7%
MODNet_mp_gap_filtered/log.txt	0.272	0.0%