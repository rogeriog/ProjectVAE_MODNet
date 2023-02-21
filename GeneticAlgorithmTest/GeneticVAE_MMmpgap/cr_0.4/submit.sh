#!/bin/bash
#SBATCH --job-name=VAE-MM40p
#SBATCH --time=1-00:00:00
#SBATCH --output=log.txt
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=40000
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
## #SBATCH --nodelist=mb-rom[101,102,103,104]
source ~/.bashrc
module load CUDA cuDNN/8.0.4.30-CUDA-11.1.1 
# TensorFlow/2.5.0-fosscuda-2020b
#export XLA_FLAGS="--xla_gpu_cuda_data_dir=/home/ucl/modl/rgouvea/anaconda3/envs/env_megnetgpu/lib/"
CUDA_DIR=/home/ucl/modl/rgouvea/anaconda3/envs/env_modnetmod/lib/python3.8/site-packages/nvidia/cuda_nvcc/
export XLA_FLAGS="--xla_gpu_cuda_data_dir=/home/ucl/modl/rgouvea/anaconda3/envs/env_modnetmod/lib/python3.8/site-packages/nvidia/cuda_nvcc/" 
# /home/ucl/modl/rgouvea/xla/nvvm/libdevice"

conda activate env_modnetmod
echo "start"
date
#python3 -u autoencoderMODNetFeats0.py >> log0.txt
#python3 -u autoencoder_MP_Gap_final_testcomp.py >> log0.txt
python3 -u genetic.py >> log.txt
date
echo "done"
