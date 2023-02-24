dirVAE40p='/globalscratch/users/r/g/rgouvea/ProjectVAE_MODNet/GeneticAlgorithmTest/GeneticVAE_MMmpgap/cr_0.4/tmp/'
VAE40pfile=dirVAE40p+'geneticVAE_MMmp_gap_custom_VAE0.8_cr0.4_bs256_ep170_loss_mse_lr0.0022_AutoEncoder.h5'
scalerfile=dirVAE40p+'Scaler_geneticVAE_MMmp_gap.pkl'
from autoencoder_tools.data_processing import encode_dataset
from autoencoder_tools.autoencoder_setup import SamplingLayer, VAELossLayer
from modnet.preprocessing import MODData
data=MODData.load('/globalscratch/users/r/g/rgouvea/MODNet_Perovskite_Benchmark/DATAFILES/matbench_perovskites_moddata.pkl.gz')
Xencoded = encode_dataset(dataset=data.df_featurized,
              scaler=scalerfile,
              columns_to_read=dirVAE40p+'encoded_columns.txt',
              autoencoder=VAE40pfile,
              save_name='PerovskitesMODNet_testVAE40p.pkl',
              feat_prefix="EncodedMatminerVAE40p",
              compile_model=False,
              custom_objs={'SamplingLayer': SamplingLayer, 'VAELossLayer': VAELossLayer},
              encoder_type="variational",
              )
