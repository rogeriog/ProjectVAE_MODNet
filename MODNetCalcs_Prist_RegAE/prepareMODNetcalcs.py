import os, shutil 
from modnet.preprocessing import MODData 
#initialize_data(,dirnames,sampling=[None],target_name=None):
import sys
sys.path.append('../')
from modnet_misctools.PreprocessForMODNet import initialize_dirs
from autoencoder_tools.data_processing import encode_dataset
from autoencoder_tools.data_processing import filter_features_dataset
'''
The following code is provided as example, and was used to encode the 
datasets with the AutoEncoders and then save the encoded datasets as 
MODData objects. These objects are then used to train the MODNet models
which are initialized with the initialize_dirs function. That takes into
account specific configurations to run MODNet in the cluster.
'''


'''
## code to filter datasets
X=MODData.load('./MODNet_elastic/matbench_elastic/precomputed/matbench_elastic_moddata.pkl.gz')
encoded_columns='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt'
Xfiltered=filter_features_dataset(dataset=X.df_featurized , allowed_features_file=encoded_columns)
X.df_featurized=Xfiltered
X.save('MODNet_elastic_filteredfeats/matbench_elastic/precomputed/matbench_elastic_moddata_filter.pkl.gz')
print(Xfiltered)



dirs=initialize_dirs('matbench_phonons',["MODNet_phonons"])
print(dirs)
dirs=initialize_dirs('matbench_mp_gap',["MODNet_mp_gap"])
print(dirs)
dirs=initialize_dirs('matbench_phonons',["MODNet_elastic"])
print(dirs)
dirs=initialize_dirs('matbench_phonons',["MODNet_elastic_filteredfeats"])
print(dirs)

data=MODData.load('./mb_perovskites_original/fullset/matbench_perovskites/precomputed/matbench_perovskites_moddata.pkl.gz')
data=MODData.load('./MODNet_phonons/matbench_phonons/precomputed/matbench_phonons_moddata.pkl.gz')
data.df_featurized=data.df_featurized.fillna(-1)
encoded_columns='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt'
dirs=initialize_dirs('matbench_phonons',["MODNet_phonons_Ph2.2f_80"])
Xencoded=encode_dataset(dataset=data, 
              scaler='../DATAFILES/MB_PhononsFeats_2.2final_custom_n_b/Scaler_MB_PhononsFeats_2.2final.pkl', 
              columns_to_read='../DATAFILES/MB_PhononsFeats_2.2final_custom_n_b/encoded_columns.txt',
              autoencoder='../DATAFILES/MB_PhononsFeats_2.2final_custom_n_b/MB_PhononsFeats_2.2final_2.2custom_n_b_cr0.7999999999999998_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5',
              save_name='MODNet_phonons_Ph2.2f_80/matbench_phonons/precomputed/matbench_phonons_ph80cr.pkl.gz',
              feat_prefix = "EncodedFeat2.2f_80cr",
              mode = "MODData")
dirs=initialize_dirs('matbench_perovskites',["MODNet_perovskites_MM2.2f80_OFM2.5f50"])
dirs=initialize_dirs('matbench_perovskites',["MODNet_perovskites_MM2.2f80_OFM2.5f50_MEGNet32"])
dirs=initialize_dirs('matbench_perovskites',["MODNet_MEGNet32"])
dirs=initialize_dirs('matbench_perovskites',["MODNet_perovskites_MNetencodMM60p_MNetencodOFM20p_MEGNet32"])

data=MODData.load('./MODNet_phonons/matbench_phonons/precomputed/matbench_phonons_moddata.pkl.gz')
data.df_featurized=data.df_featurized.fillna(-1)
encoded_columns='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt'
dirs=initialize_dirs('matbench_phonons',["MODNet_phonons_Ph2.2f_100"])
Xencoded=encode_dataset(dataset=data, 
               scaler='../DATAFILES/MB_PhononsFeats_2.2final_custom_n_b/Scaler_MB_PhononsFeats_2.2final.pkl', 
               columns_to_read='../DATAFILES/MB_PhononsFeats_2.2final_custom_n_b/encoded_columns.txt',
               autoencoder='../DATAFILES/MB_PhononsFeats_2.2final_custom_n_b/MB_PhononsFeats_2.2final_2.2custom_n_b_cr1.0_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5',
               save_name='MODNet_phonons_Ph2.2f_100/matbench_phonons/precomputed/matbench_phonons_ph100cr.pkl.gz',
               feat_prefix = "EncodedFeat2.2f_100cr",
               mode = "MODData")
#MB_PhononsFeats_2.2final_2.2custom_n_b_cr1.0_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5

data=MODData.load('./mb_perovskites_original/fullset/matbench_perovskites/precomputed/matbench_perovskites_moddata.pkl.gz')
data.df_featurized=data.df_featurized.fillna(-1)
encoded_columns='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt'
dirs=initialize_dirs('matbench_perovskites',["MODNet_perovskites_encoded_2.2f_80"])
Xencoded=encode_dataset(dataset=data, 
               scaler='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/Scaler_MP_GapFeats_2.2final.pkl', 
               columns_to_read='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt',
               autoencoder='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/MP_GapFeats_2.2final_2.2custom_n_b_cr0.7999999999999998_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5',
               save_name='MODNet_perovskites_encoded_2.2f_80/matbench_perovskites/precomputed/matbench_phonons_80cr.pkl.gz',
               feat_prefix = "EncodedFeat2.2f_80cr",
               mode = "MODData")
data=MODData.load('./mb_perovskites_original/fullset/matbench_perovskites/precomputed/matbench_perovskites_moddata.pkl.gz')
dirs=initialize_dirs('matbench_perovskites',["MODNet_perovskites_encoded_2.2f_60"])
Xencoded=encode_dataset(dataset=data, 
               scaler='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/Scaler_MP_GapFeats_2.2final.pkl', 
               columns_to_read='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt',
               autoencoder='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/MP_GapFeats_2.2final_2.2custom_n_b_cr0.5999999999999996_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5',
               save_name='MODNet_perovskites_encoded_2.2f_60/matbench_perovskites/precomputed/matbench_phonons_moddata_60cr.pkl.gz',
               feat_prefix = "EncodedFeat2.2f_60cr",
               mode = "MODData")

data=MODData.load('./mb_perovskites_original/fullset/matbench_perovskites/precomputed/matbench_perovskites_moddata.pkl.gz')
dirs=initialize_dirs('matbench_perovskites',["MODNet_perovskites_encoded_2.2f_40"])
Xencoded=encode_dataset(dataset=data, 
               scaler='../DATAFILES/MP_GapFeats_2.2final2_custom_n_b/Scaler_MP_GapFeats_2.2final2.pkl', 
               columns_to_read='../DATAFILES/MP_GapFeats_2.2final2_custom_n_b/encoded_columns.txt',
               autoencoder='../DATAFILES/MP_GapFeats_2.2final2_custom_n_b/MP_GapFeats_2.2final2_2.2custom_n_b_cr0.3999999999999997_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5',
               save_name='MODNet_perovskites_encoded_2.2f_40/matbench_perovskites/precomputed/matbench_phonons_moddata_40cr.pkl.gz',
               feat_prefix = "EncodedFeat2.2f_40cr",
               mode = "MODData")

data=filter_features_dataset(dataset=data, allowed_features_file=encoded_columns,mode='MODData')
dirs=initialize_dirs('matbench_perovskites',["MODNet_perovskites_filtered"])
data.save('./MODNet_perovskites_filtered/matbench_perovskites/precomputed/matbench_perovskites_filtered.pkl.gz')

dirs=initialize_dirs('matbench_perovskites',["MODNet_perovskites_2.2f_100cr"])
Xencoded=encode_dataset(dataset=data, 
               scaler='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/Scaler_MP_GapFeats_2.2final.pkl', 
               columns_to_read='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt',
               autoencoder='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/MP_GapFeats_2.2final_2.2custom_n_b_cr1.0_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5',
               save_name='MODNet_perovskites_2.2f_100cr/matbench_perovskites/precomputed/matbench_perovskites_100cr_g2.2f.pkl.gz',
               feat_prefix = "EncodedFeat2.2f_100cr",
               mode = "MODData")

data=MODData.load('./MODNet_phonons/matbench_phonons/precomputed/matbench_phonons_moddata.pkl.gz')
data.df_featurized=data.df_featurized.fillna(-1)
encoded_columns='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt'
data=filter_features_dataset(dataset=data, allowed_features_file=encoded_columns,mode='MODData')
dirs=initialize_dirs('matbench_phonons',["MODNet_phonons_filtered"])
data.save('./MODNet_phonons_filtered/matbench_phonons/precomputed/matbench_phonons_filtered.pkl.gz')
data=MODData.load('./MODNet_phonons_filtered/matbench_phonons/precomputed/matbench_phonons_filtered.pkl.gz')
dirs=initialize_dirs('matbench_phonons',["MODNet_phonons_encoded_2.2f_100"])
Xencoded=encode_dataset(dataset=data, 
               scaler='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/Scaler_MP_GapFeats_2.2final.pkl', 
               columns_to_read='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt',
               autoencoder='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/MP_GapFeats_2.2final_2.2custom_n_b_cr1.0_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5',
               save_name='MODNet_phonons_encoded_2.2f_100/matbench_phonons/precomputed/matbench_phonons_1.0cr.pkl.gz',
               feat_prefix = "EncodedFeat2.2f_100cr",
               mode = "MODData")
data=MODData.load('./MODNet_phonons_filtered/matbench_phonons/precomputed/matbench_phonons_filtered.pkl.gz')
dirs=initialize_dirs('matbench_phonons',["MODNet_phonons_encoded_2.2f_80"])
Xencoded=encode_dataset(dataset=data, 
               scaler='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/Scaler_MP_GapFeats_2.2final.pkl', 
               columns_to_read='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt',
               autoencoder='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/MP_GapFeats_2.2final_2.2custom_n_b_cr0.7999999999999998_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5',
               save_name='MODNet_phonons_encoded_2.2f_80/matbench_phonons/precomputed/matbench_phonons_80cr.pkl.gz',
               feat_prefix = "EncodedFeat2.2f_80cr",
               mode = "MODData")
data=MODData.load('./MODNet_phonons_filtered/matbench_phonons/precomputed/matbench_phonons_filtered.pkl.gz')
dirs=initialize_dirs('matbench_phonons',["MODNet_phonons_encoded_2.2f_60"])
Xencoded=encode_dataset(dataset=data, 
               scaler='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/Scaler_MP_GapFeats_2.2final.pkl', 
               columns_to_read='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt',
               autoencoder='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/MP_GapFeats_2.2final_2.2custom_n_b_cr0.5999999999999996_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5',
               save_name='MODNet_phonons_encoded_2.2f_60/matbench_phonons/precomputed/matbench_phonons_moddata_60cr.pkl.gz',
               feat_prefix = "EncodedFeat2.2f_60cr",
               mode = "MODData")

data=MODData.load('./MODNet_phonons_filtered/matbench_phonons/precomputed/matbench_phonons_filtered.pkl.gz')
dirs=initialize_dirs('matbench_phonons',["MODNet_phonons_encoded_2.2f_40"])
Xencoded=encode_dataset(dataset=data, 
               scaler='../DATAFILES/MP_GapFeats_2.2final2_custom_n_b/Scaler_MP_GapFeats_2.2final2.pkl', 
               columns_to_read='../DATAFILES/MP_GapFeats_2.2final2_custom_n_b/encoded_columns.txt',
               autoencoder='../DATAFILES/MP_GapFeats_2.2final2_custom_n_b/MP_GapFeats_2.2final2_2.2custom_n_b_cr0.3999999999999997_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5',
               save_name='MODNet_phonons_encoded_2.2f_40/matbench_phonons/precomputed/matbench_phonons_moddata_40cr.pkl.gz',
               feat_prefix = "EncodedFeat2.2f_40cr",
               mode = "MODData")

data=MODData.load('MODNet_phonons_filteredfeats/matbench_elastic/precomputed/matbench_elastic_moddata_filter.pkl.gz')
dirs=initialize_dirs('matbench_phonons',["MODNet_elastic_encoded_2.2f_100"])
Xencoded=encode_dataset(dataset=data, 
               scaler='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/Scaler_MP_GapFeats_2.2final.pkl', 
               columns_to_read='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt',
               autoencoder='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/MP_GapFeats_2.2final_2.2custom_n_b_cr1.0_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5',
               save_name='MODNet_phonons_encoded_2.2f_100/matbench_elastic/precomputed/matbench_elastic_moddata_1.0cr.pkl.gz',
               feat_prefix = "EncodedFeat2.2f_100cr",
               mode = "MODData")
data=MODData.load('MODNet_phonons_filteredfeats/matbench_elastic/precomputed/matbench_elastic_moddata_filter.pkl.gz')
dirs=initialize_dirs('matbench_phonons',["MODNet_elastic_encoded_2.2f_80"])
Xencoded=encode_dataset(dataset=data, 
               scaler='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/Scaler_MP_GapFeats_2.2final.pkl', 
               columns_to_read='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt',
               autoencoder='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/MP_GapFeats_2.2final_2.2custom_n_b_cr0.7999999999999998_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5',
               save_name='MODNet_phonons_encoded_2.2f_80/matbench_elastic/precomputed/matbench_elastic_moddata_80cr.pkl.gz',
               feat_prefix = "EncodedFeat2.2f_80cr",
               mode = "MODData")
data=MODData.load('MODNet_phonons_filteredfeats/matbench_elastic/precomputed/matbench_elastic_moddata_filter.pkl.gz')
dirs=initialize_dirs('matbench_phonons',["MODNet_elastic_encoded_2.2f_60"])
Xencoded=encode_dataset(dataset=data, 
               scaler='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/Scaler_MP_GapFeats_2.2final.pkl', 
               columns_to_read='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt',
               autoencoder='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/MP_GapFeats_2.2final_2.2custom_n_b_cr0.5999999999999996_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5',
               save_name='MODNet_phonons_encoded_2.2f_60/matbench_elastic/precomputed/matbench_elastic_moddata_60cr.pkl.gz',
               feat_prefix = "EncodedFeat2.2f_60cr",
               mode = "MODData")

data=MODData.load('MODNet_phonons_filteredfeats/matbench_elastic/precomputed/matbench_elastic_moddata_filter.pkl.gz')
dirs=initialize_dirs('matbench_phonons',["MODNet_elastic_encoded_2.2f_40"])
Xencoded=encode_dataset(dataset=data, 
               scaler='../DATAFILES/MP_GapFeats_2.2final2_custom_n_b/Scaler_MP_GapFeats_2.2final2.pkl', 
               columns_to_read='../DATAFILES/MP_GapFeats_2.2final2_custom_n_b/encoded_columns.txt',
               autoencoder='../DATAFILES/MP_GapFeats_2.2final2_custom_n_b/MP_GapFeats_2.2final2_2.2custom_n_b_cr0.3999999999999997_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5',
               save_name='MODNet_phonons_encoded_2.2f_40/matbench_elastic/precomputed/matbench_elastic_moddata_40cr.pkl.gz',
               feat_prefix = "EncodedFeat2.2f_40cr",
               mode = "MODData")

dirs=initialize_dirs('matbench_mp_gap',["MODNet_mp_gap_filtered"])
data=MODData.load('./MODNet_mp_gap/matbench_mp_gap/precomputed/matbench_mp_gap_light_featurized.pkl')
data.df_featurized=data.df_featurized.fillna(-1)
encoded_columns='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt'
data=filter_features_dataset(dataset=data, allowed_features_file=encoded_columns,mode='MODData')
data.save('./MODNet_mp_gap_filtered/matbench_mp_gap/precomputed/matbench_mp_gap_filtered.pkl.gz')

data=MODData.load('./MODNet_mp_gap/matbench_mp_gap/precomputed/matbench_mp_gap_light_featurized.pkl')
data.df_featurized=data.df_featurized.fillna(-1)
encoded_columns='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt'
data=MODData.load('./MODNet_mp_gap_filtered/matbench_mp_gap/precomputed/matbench_mp_gap_filtered.pkl.gz')
dirs=initialize_dirs('matbench_mp_gap',["MODNet_mp_gap_2.2f_100"])
Xencoded=encode_dataset(dataset=data, 
               scaler='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/Scaler_MP_GapFeats_2.2final.pkl', 
               columns_to_read='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt',
               autoencoder='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/MP_GapFeats_2.2final_2.2custom_n_b_cr1.0_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5',
               save_name='MODNet_mp_gap_2.2f_100/matbench_mp_gap/precomputed/matbench_mp_gap_100cr.pkl.gz',
               feat_prefix = "EncodedFeat2.2f_100cr",
               mode = "MODData")

data=MODData.load('./MODNet_mp_gap_filtered/matbench_mp_gap/precomputed/matbench_mp_gap_filtered.pkl.gz')
dirs=initialize_dirs('matbench_mp_gap',["MODNet_mp_gap_2.2f_80"])
Xencoded=encode_dataset(dataset=data, 
               scaler='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/Scaler_MP_GapFeats_2.2final.pkl', 
               columns_to_read='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt',
               autoencoder='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/MP_GapFeats_2.2final_2.2custom_n_b_cr0.7999999999999998_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5',
               save_name='MODNet_mp_gap_2.2f_80/matbench_mp_gap/precomputed/matbench_mp_gap_80cr.pkl.gz',
               feat_prefix = "EncodedFeat2.2f_80cr",
               mode = "MODData")

data=MODData.load('./MODNet_mp_gap_filtered/matbench_mp_gap/precomputed/matbench_mp_gap_filtered.pkl.gz')
dirs=initialize_dirs('matbench_mp_gap',["MODNet_mp_gap_2.2f_60"])
Xencoded=encode_dataset(dataset=data, 
               scaler='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/Scaler_MP_GapFeats_2.2final.pkl', 
               columns_to_read='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/encoded_columns.txt',
               autoencoder='../DATAFILES/MP_GapFeats_2.2final_custom_n_b/MP_GapFeats_2.2final_2.2custom_n_b_cr0.5999999999999996_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5',
               save_name='MODNet_mp_gap_2.2f_60/matbench_mp_gap/precomputed/matbench_mp_gap_60cr.pkl.gz',
               feat_prefix = "EncodedFeat2.2f_60cr",
               mode = "MODData")
data=MODData.load('./MODNet_mp_gap_filtered/matbench_mp_gap/precomputed/matbench_mp_gap_filtered.pkl.gz')
dirs=initialize_dirs('matbench_mp_gap',["MODNet_mp_gap_2.2f_40"])
Xencoded=encode_dataset(dataset=data, 
               scaler='../DATAFILES/MP_GapFeats_2.2final2_custom_n_b/Scaler_MP_GapFeats_2.2final2.pkl', 
               columns_to_read='../DATAFILES/MP_GapFeats_2.2final2_custom_n_b/encoded_columns.txt',
               autoencoder='../DATAFILES/MP_GapFeats_2.2final2_custom_n_b/MP_GapFeats_2.2final2_2.2custom_n_b_cr0.3999999999999997_bs64_ep200_loss_mse_lr0.0005_AutoEncoder.h5',
               save_name='MODNet_mp_gap_2.2f_40/matbench_mp_gap/precomputed/matbench_mp_gap_40cr.pkl.gz',
               feat_prefix = "EncodedFeat2.2f_40cr",
               mode = "MODData")

print(dirs)
print(dirs)
dirs=initialize_dirs('matbench_phonons',["MODNet_elastic_encoded_2.2f_60"])
print(dirs)
dirs=initialize_dirs('matbench_phonons',["MODNet_elastic_encoded_2.2f_40"])
print(dirs)
'''
