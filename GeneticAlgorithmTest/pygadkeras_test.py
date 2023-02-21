import tensorflow.keras
import pygad.kerasga
import numpy
import pygad

def fitness_func(solution, sol_idx):
    global data_inputs, data_outputs, keras_ga, model

    predictions = pygad.kerasga.predict(model=model,
                                        solution=solution,
                                        data=data_inputs)

    mae = tensorflow.keras.losses.MeanAbsoluteError()
    abs_error = mae(data_outputs, predictions).numpy() + 0.00000001
    solution_fitness = 1.0/abs_error

    return solution_fitness

def callback_generation(ga_instance):
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution()[1]))
    print("All solutions' fitness : {solutions}".format(solutions=ga_instance.last_generation_fitness))
# input_layer  = tensorflow.keras.layers.Input(3)
#bnormalization = tensorflow.keras.layers.BatchNormalization()(input_layer)
#dense_layer1 = tensorflow.keras.layers.Dense(5, activation="relu")(bnormalization)
# dense_layer1 = tensorflow.keras.layers.Dense(5, activation="relu")(input_layer)
# output_layer = tensorflow.keras.layers.Dense(1, activation="linear")(dense_layer1)

# model = tensorflow.keras.Model(inputs=input_layer, outputs=output_layer)

## load keras model from h5 file

from keras.models import load_model

model = load_model('/globalscratch/users/r/g/rgouvea/GeneticAlgorithmTest/tmp/testmodel_default_cr0.5_bs8_ep25_loss_mse_lr0.0012000000000000001_AutoEncoder.h5')

## all the batchnormalization layers of the model will be set to trainable=False
## this is done to avoid the batchnormalization layers to be trained by the genetic algorithm
for layer in model.layers:
    if isinstance(layer, tensorflow.keras.layers.BatchNormalization):
        layer.trainable = False


keras_ga = pygad.kerasga.KerasGA(model=model,
                                 num_solutions=40,
                                 mode='from_optimized',
                                 epsilon=0.0001)

# # Data inputs
# data_inputs = numpy.array([[0.02, 0.1, 0.15],
#                            [0.7, 0.6, 0.8],
#                            [1.5, 1.2, 1.7],
#                            [3.2, 2.9, 3.1]])

## following code is just loading the data from perovskite benchmark
## this data is a simple pandas dataframe
# # Data outputs
# data_outputs = numpy.array([[0.1],
#                             [0.6],
#                             [1.3],
#                             [2.5]])

from modnet.preprocessing import MODData
data=MODData.load('/globalscratch/users/r/g/rgouvea/MODNet_Perovskite_Benchmark/DATAFILES/matbench_perovskites_moddata.pkl.gz')
Xtoencode=data.df_featurized.sample(100, random_state=42)
from autoencoder_tools.data_processing import filter_features_dataset
Xtoencode=filter_features_dataset(Xtoencode,
                        allowed_features_file='/globalscratch/users/r/g/rgouvea/GeneticAlgorithmTest/tmp/encoded_columns.txt')
data_inputs=Xtoencode.to_numpy()
data_outputs=Xtoencode.to_numpy()

print(data_inputs)
print('Data shapes are: ', data_inputs.shape, data_outputs.shape)

# Prepare the PyGAD parameters. Check the documentation for more information: https://pygad.readthedocs.io/en/latest/README_pygad_ReadTheDocs.html#pygad-ga-class
num_generations = 100 # Number of generations.
num_parents_mating = 10 # Number of solutions to be selected as parents in the mating pool.
initial_population = keras_ga.population_weights # Initial population of network weights

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       initial_population=initial_population,
                       fitness_func=fitness_func,
                       on_generation=callback_generation,
                       mutation_percent_genes=2, # 1
                       save_best_solutions=True,
                       save_solutions=True,
                       parent_selection_type= 'sss',
                       mutation_type="random",
                       random_mutation_min_val=-0.01,# -0.01,
                       random_mutation_max_val=0.01 # 0.01 
                       )

ga_instance.run()

# After the generations complete, some plots are showed that summarize how the outputs/fitness values evolve over generations.
ga_instance.plot_fitness(title="PyGAD & Keras - Iteration vs. Fitness", linewidth=4)

# Returning the details of the best solution.
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

# Make prediction based on the best solution.
predictions = pygad.kerasga.predict(model=model,
                                    solution=solution,
                                     data=data_inputs)
print("Predictions : \n", predictions)

mae = tensorflow.keras.losses.MeanAbsoluteError()
abs_error = mae(data_outputs, predictions).numpy()
print("Absolute Error : ", abs_error)
