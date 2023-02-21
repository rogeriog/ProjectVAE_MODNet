import pickle
OFMfeaturized=pickle.load(open('/globalscratch/users/r/g/rgouvea/autoencode_OFM/OFM_93k_mp_gap.pkl','rb'))
OFMfeaturized=OFMfeaturized.drop('structure',axis=1)
Xtoencode=OFMfeaturized.fillna(-1)
print(Xtoencode)
autoencoder_path='/globalscratch/users/r/g/rgouvea/GeneticAlgorithmTest/tmp/'
autoencoder_file='geneticVAE_OFM93k_custom_VAE2.1_cr0.2_bs64_ep90_loss_mse_lr0.001_AutoEncoder.h5'
from autoencoder_tools.data_processing import encode_dataset
loss='mse'
from keras.losses import mean_squared_error as keras_mean_squared_error
from tensorflow.keras import backend as K

Xencoded=encode_dataset(Xtoencode,
        scaler = autoencoder_path+'Scaler_geneticVAE_OFM93k.pkl',
        columns_to_read = autoencoder_path+'encoded_columns.txt',
        autoencoder = autoencoder_path+autoencoder_file,
        save_name = './VAE_OFM2.1p_0.2compress.pkl',
        feat_prefix = 'OFM_VAEencoded2.1p_20p',
        # custom_objs = {'vae_loss':vae_loss}
        compile_model = False,
        encoder_type = 'variational',
        )
print(Xencoded, Xencoded.shape)
