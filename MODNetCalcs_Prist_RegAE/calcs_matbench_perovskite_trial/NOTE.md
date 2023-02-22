This folder contains the first trial test of regular autoencoder in the matbench_perovskite dataset, in here multiple settings have been used and different model sizes considered


| Model                                           | Size   |   Score |   % improvement |
|:------------------------------------------------|:-------|--------:|----------------:|
| mb_perovskites_original/remake_fullset          | Full   |  0.0888 |            0    |
| mb_perovskites_original/fullset                 | Full   |  0.0928 |            4.5  |
| mb_perovskites_wOFM/fullset                     | Full   |  0.0903 |            1.69 |
| MODNetCompressed/fullset                        | Full   |  0.0917 |            3.27 |
| MODNetCompressed80/fullset                      | Full   |  0.0839 |           -5.52 |
| mb_perovskites_original/fullset_precomputednmi  | Full   |  0.0829 |           -6.64 |
| MODNet_MM80_OFM50/fullset                       | Full   |  0.0728 |          -18.02 |
| MODNet_MM_MEGNet16/fullset                      | Full   |  0.0752 |          -15.32 |
| MODNet_MM_MEGNet32/fullset                      | Full   |  0.0726 |          -18.24 |
| MODNet_MM80_OFM50_MEGNet32/fullset              | Full   |  0.0653 |          -26.46 |
| MODNet_MM088encod/fullset                       | Full   |  0.1055 |           18.81 |
| mb_perovskites_original/subset5k                | 5k     |  0.1667 |            0    |
| mb_perovskites_wOFM/subset5k                    | 5k     |  0.1646 |           -1.26 |
| mb_perovskites_original/subset5k_precomputednmi | 5k     |  0.1642 |           -1.5  |
| MODNetCompressed/subset5k                       | 5k     |  0.162  |           -2.82 |
| MODNetCompressed80/subset5k                     | 5k     |  0.155  |           -7.02 |
| MODNet_MM088encod/subset5k                      | 5k     |  0.1795 |            7.68 |
| MODNet_MM80_OFM50/subset5k                      | 5k     |  0.1401 |          -15.96 |
| MODNet_MM_MEGNet16/subset5k                     | 5k     |  0.1202 |          -27.89 |
| MODNet_MM80_OFM50_MEGNet32/subset5k             | 5k     |  0.1171 |          -29.75 |
| MODNet_MM_MEGNet32/subset5k                     | 5k     |  0.1167 |          -29.99 |
| mb_perovskites_original/subset1k                | 1k     |  0.2802 |            0    |
| mb_perovskites_wOFM/subset1k                    | 1k     |  0.2811 |            0.32 |
| mb_perovskites_original/remake_subset1k         | 1k     |  0.2747 |           -1.96 |
| mb_perovskites_original/subset1k_precomputednmi | 1k     |  0.2727 |           -2.68 |
| MODNet_MM80_OFM50/subset1k                      | 1k     |  0.2656 |           -5.21 |
| MODNetCompressed80/subset1k                     | 1k     |  0.304  |            8.49 |
| MODNetCompressed/subset1k                       | 1k     |  0.3164 |           12.92 |
| MODNet_MM088encod/subset1k                      | 1k     |  0.3236 |           15.49 |
| MODNet_MM80_OFM50_MEGNet32/subset1k             | 1k     |  0.1936 |          -30.91 |
| MODNet_MM_MEGNet16/subset1k                     | 1k     |  0.1862 |          -33.55 |
| MODNet_MM_MEGNet32/subset1k                     | 1k     |  0.1749 |          -37.58 |