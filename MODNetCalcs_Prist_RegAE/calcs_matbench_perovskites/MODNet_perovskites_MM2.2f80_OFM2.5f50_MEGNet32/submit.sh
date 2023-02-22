#!/bin/bash
#SBATCH --job-name=MODNet_perovskites_MM2.2f80_OFM2.5f50_MEGNet32
#SBATCH --time=1-00:00:00
#SBATCH --output=log.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=24
#SBATCH --partition=keira
#SBATCH --mem-per-cpu=2000
source ~/.bashrc

conda activate env_modnet
#export PYTHONUSERBASE=intentionally-disabled  ##it was loading local modnet...
echo "start"
date
nproc=24 # $(nproc --all)
python3 run_benchmark.py --task matbench_perovskites --n_jobs $nproc >> log.txt
echo "done"
date
