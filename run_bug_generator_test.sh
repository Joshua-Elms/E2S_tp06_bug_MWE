#!/bin/bash

#SBATCH -J graphcast_install
#SBATCH -p hopper
#SBATCH -o output.out
#SBATCH -e log.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jmelms@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node h100:1
#SBATCH --cpus-per-task=1
#SBATCH --time=3:00:00
#SBATCH --mem=128GB
#SBATCH -A r00389

conda deactivate
cd /N/slate/jmelms/projects/dcmip2025_idealized_tests/E2S_tp06_bug_MWE
source /N/slate/jmelms/projects/dcmip2025_idealized_tests/E2S_tp06_bug_MWE/test_E2S/.venv/bin/activate
python -m bug_generator_controller