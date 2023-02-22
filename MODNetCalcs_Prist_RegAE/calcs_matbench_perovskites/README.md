This folder contains results from MODNet calculations on the matbench_perovskites dataset using the best regular autoencoder found, with different compression ratios. The MODNet_perovskites_encoded_* subfolders contain calculations performed with an autoencoder architecture N-2.2N-b with compression ratios of 100, 40, 60, and 80, respectively. Here, N represents the number of input features, and b represents the bottleneck size of the autoencoder. The filtered MODNet_perovskites_filtered subfolder contains calculations performed on a filtered set of the dataset that matches the autoencoder features.

In addition, this folder contains subfolders with results from MODNet calculations using other feature sets and models. The MODNet_perovskites_MM2.2f80_OFM2.5f50 subfolder contains calculations performed using a combination of MatMiner features encoded with the 2.2f model at 80% compression and Orbital Field Matrix (OFM) features with a N-2.5N-b encoder at 50% compression. The MODNet_perovskites_MM2.2f80_OFM2.5f50_MEGNet32 subfolder contains calculations performed using the same feature set as the MODNet_perovskites_MM2.2f80_OFM2.5f50 subfolder, but with MEGNet pretrained models including a dense layer with 32 neurons as features for MODNet.

The 'MODNet_perovskites_MNetencodMM60p_MNetencodOFM20p' subfolder contains calculations performed using predictions made with a MEGNet model trained to reproduce the encoded features for MatMiner and OFM, respectively. The 'MODNet_perovskites_MNetencodMM60p_MNetencodOFM20p_MEGNet32' subfolder contains calculations performed using the same feature set as the 'MODNet_perovskites_MNetencodMM60p_MNetencodOFM20p' subfolder, but with MEGNet pretrained models including a dense layer with 32 neurons as features for MODNet.

Lastly, the 'MODNet_perovskites_MEGNetPred_encodMM60p' subfolder contains calculations performed using predictions made with a MEGNet model trained on the same dataset.


| Model                                      | Final Score | Difference |
| ------------------------------------------ | ----------- | ---------- |
| MODNet_perovskites_filtered                | 0.090       | 0.0%       |
| MODNet_perovskites_MEGNetPred_encodMM60p   | 0.105       | 16.7%      |
| MODNet_perovskites_MNetencodMM60p_MNetencodOFM20p    | 0.097       | 7.4%       |
| MODNet_perovskites_encoded_2.2f_40         | 0.084       | -5.3%      |
| MODNet_perovskites_encoded_2.2f_60         | 0.079       | -11.1%     |
| MODNet_perovskites_encoded_2.2f_80         | 0.079       | -11.1%     |
| MODNet_perovskites_encoded_2.2f_100        | 0.077       | -14.4%     |
| MODNet_perovskites_MM2.2f80_OFM2.5f50      | 0.070       | -22.2%     |
| MODNet_perovskites_MM2.2f80_OFM2.5f50_MEGNet32 | 0.063    | -29.3%     |
| MODNet_perovskites_MNetencodMM60p_MNetencodOFM20p_MEGNet32 | 0.073 | -18.9%     |
