#!/usr/bin/bash
source /home/sebas/miniforge3/etc/profile.d/conda.sh

conda activate iccd332 || source /home/sebas/miniforge3/bin/activate iccd332

python /home/sebas/Api/main.py
