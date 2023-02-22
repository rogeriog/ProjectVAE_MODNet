'''
This script is an example using the hypertune_autoencoder function to perform a 
grid search over a range of hyperparameters for a regular autoencoder.
The use of Genetic Algorithms is implemented now in genetic_hypertune 
module and performs a more efficient search.
'''
def main():
    from autoencoder_tools import hypertune_autoencoder
    from modnet.preprocessing import MODData
    import pickle
    data=MODData.load('../matbench_mp_gap_light_featurized.pkl')
    Xtoencode=data.df_featurized.fillna(-1)
    # for OFM data
    #OFMfeaturized=pickle.load(open('../OFM_mp_gap.pkl','rb'))
    #OFMfeaturized=OFMfeaturized.drop('structure',axis=1)
    #Xtoencode=OFMfeaturized.fillna(-1)

    print(Xtoencode)

    hypertune_autoencoder( dataset = Xtoencode,
        prefix_name = 'MP_GapFeats',
        bottleneck_ratios = [0.3, 0.5, 0.8], 
        batch_sizes = [16,32,64],
        epochs_list = [100,200,300],
        loss_functions = ['mse'],
        learning_rates = [0.0005, 0.001, 0.002],
        architectures = [ {'arch':'n_b' },
                          {'arch':'2n_b' },
                          {'arch':'custom_n_b', 'n_factor': 2.2 },
                          {'arch':'3n_b' }, ] ,

        savedir = './DATAFILES/',
        )

if __name__ == '__main__':
    main()
