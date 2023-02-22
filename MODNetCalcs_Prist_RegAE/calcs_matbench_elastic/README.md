This folder contains results from MODNet calculations on the matbench_elastic dataset using the best regular autoencoder found, with different compression ratios. The MODNet_elastic_encoded_* subfolders contain calculations performed with an autoencoder architecture N-2.2N-b with compression ratios of 100, 40, 60, and 80, respectively. Here, N represents the number of input features, and b represents the bottleneck size of the autoencoder. The filtered MODNet_elastic_filteredfeats subfolder contains calculations performed on a filtered set of the dataset that matches the autoencoder features. The MODNet_elastic subfolder contains calculations performed on the raw data without autoencoder compression.


| Model                                 | Final Score | Difference |
|---------------------------------------|-------------|------------|
| MODNet_elastic_filteredfeats          | 0.068       | 0.00%      |
| MODNet_elastic                       | 0.068       | 0.00%      |
| MODNet_elastic_encoded_2.2f_80       | 0.073       | 7.35%      |
| MODNet_elastic_encoded_2.2f_60       | 0.073       | 7.35%     |
| MODNet_elastic_encoded_2.2f_40       | 0.075       | 10.3%      |
| MODNet_elastic_encoded_2.2f_100      | 0.071       |  4.41%      |
