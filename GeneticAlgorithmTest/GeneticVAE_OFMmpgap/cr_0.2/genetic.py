# # need to load some functions from a file two folders above
import sys
sys.path.append('../../')
from genetic_hypertune import genetic_hypertune_autoencoder
import pickle
# this loads the featurized data from matbench mp gap
OFMfeaturized=pickle.load(open('/globalscratch/users/r/g/rgouvea/autoencode_OFM/OFM_93k_mp_gap.pkl','rb'))
OFMfeaturized=OFMfeaturized.drop('structure',axis=1)
Xtoencode=OFMfeaturized.fillna(-1)
print(Xtoencode)
import os
os.environ['TF_ENABLE_AUTO_MIXED_PRECISION'] = '1'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '1'

genetic_hypertune_autoencoder(prefix_name = 'geneticVAE_OFMmp_gap',
    dataset=Xtoencode,
    compress_ratio = 0.2,
    architecture={'arch':'custom_VAE'},
    gene_space = [[1.0,1.5,2.0,2.5],list(range(30,240,30)),
                  [0.0005, 0.001, 0.002],[64, 128,256],[1,2]],
    # initial_population = [
    # [1.5, 145, 0.0012, 256, 1], 
    # [1.6, 145, 0.0014, 128, 1], 
    # [1.6, 145, 0.0014, 32, 1], 
    # [1.5, 150, 0.001, 32, 1],
    # [1.5, 70, 0.0005, 16, 2],
    # [2.5, 50, 0.0005, 32, 1],
    # [2.0, 110, 0.0005, 8, 2],
    # [2.0, 170, 0.0005, 16, 2],
    # [2.0, 10, 0.001, 16, 1],
    # [1.5, 90, 0.001, 32, 1],],
    ga_settings = {'num_generations': 20, 'num_parents_mating': 4, 
    'sol_per_pop': 10, 'parent_selection_type': 'rws', 'keep_elitism': 2},
    savedir = './tmp/',
    logfile = 'EncoderResults.txt',
    random_state = 1,
    )

