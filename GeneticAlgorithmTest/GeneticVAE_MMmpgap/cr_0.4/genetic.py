# # need to load some functions from a file two folders above
import sys
sys.path.append('../../')
from genetic_hypertune import genetic_hypertune_autoencoder, continue_run_ga
# this loads the featurized data from matbench mp gap
from modnet.preprocessing import MODData
data=MODData.load('/globalscratch/users/r/g/rgouvea/matbench_mp_gap_light_featurized.pkl')
## check if there are nan values
Xtoencode=data.df_featurized
print('NAN values:',Xtoencode.isna().sum().sum())
Xtoencode=data.df_featurized.fillna(-1)
## check if there are nan values
print('NAN values remaining:',Xtoencode.isna().sum().sum())
print(Xtoencode)
import os
os.environ['TF_ENABLE_AUTO_MIXED_PRECISION'] = '1'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '1'
os.environ['TF_GPU_ALLOCATOR'] = 'cuda_managed'
genetic_hypertune_autoencoder(prefix_name = 'geneticVAE_MMmp_gap',
    dataset=Xtoencode,
    compress_ratio = 0.2,
    architecture={'arch':'custom_VAE'},
    gene_space = [[0.5,1.0,1.5,2.0,2.5],list(range(30,240,30)),
                  [0.0005, 0.001, 0.002],[32,64],[1,2]],
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

# ga=continue_run_ga('tmp/ga_instance_generation_5.pkl')
