I'm having a problem with finding total 6-hourly precipitation on the CDS API when using GraphCastOperational and FuXi. Here's how to replicate the bug: 

## Steps
1. Setup
    1. Clone this repository under your Slate directory: `git clone <URL>`
    2. Make a uv project dir: `mkdir E2S && cd E2S`
    3. If you don't have uv installed (skip step otherwise): `curl -LsSf https://astral.sh/uv/install.sh | sh`
    4. `uv init --python=3.12`
    5. `uv add "earth2studio @ git+https://github.com/Joshua-Elms/earth2studio-cu126.git" --extra sfno pangu fuxi graphcast` (This is a fork of E2S from only a few days ago, so it's up-to-date... it solves a weird problem with the original version demanding cuda 12.8, whereas Quartz is on cuda 12.6. Shouldn't affect CDS API at all.)
    6. `uv pip install cdsapi dotenv`
    7. `source .venv/bin/activate; cd ..`
    8. `srun -p gpu-debug -A r00389 --mem=64GB --time=01:00:00 --gpus-per-node v100:1 --pty bash`
    9. Set cache location for model weights: `mkdir /N/slate/$USER/.E2S_cache;echo EARTH2STUDIO_CACHE=/N/slate/$USER/.E2S_cache > .env`
2. Run script: `python bug_generator.py`

Each model (SFNO, Pangu6, GraphCastOperational, and FuXi) will load and run, and if they are unsuccessful, produce error messages that are caught and printed. The one I'm targeting is:

"""
2025-07-30 13:38:32.014 | ERROR    | earth2studio.data.cds:_build_requests:255 - variable id tp06 not found in CDS lexicon
        Error encountered while running fuxi model: np.str_('tp06')
"""

Pangu has an OOM error that goes away if you run it before the other models, and SFNO seems to do fine. 