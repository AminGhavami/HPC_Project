#!/bin/bash
module purge
# load old environment
module load env/deprecated/2020b
echo "load old env"
# load essensial modules
echo "loading EESSI"
module load EESSI

echo "loading OSU-Micro-Benchmarks"
module load OSU-Micro-Benchmarks/7.2-gompi-2023b
echo "lading OpenMPI"
module load OpenMPI/4.1.6-GCC-13.2.0
echo "leading ReFrame"
module load ReFrame/4.6.2
reframe --version
echo "loading python"
module load Python/3.11.5-GCCcore-13.2.0

# module list
# check if it's needed to load python
# check if they loaded

# ReFrame test
# build the folder
# mkdir -p reframe/eessi

# vim reframe/eessi/osu_eessi_tests.py

# pyton code is in folder
reframe -C ./config/eessi_config.py -c ./reframe/eessi/osu_eessi.py -r

module load lang/Anaconda3/2020.11

python eessi_plot.py

