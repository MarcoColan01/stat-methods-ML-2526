from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASETS_DIR = PROJECT_ROOT / "datasets"
RESULTS_DIR = PROJECT_ROOT / "results"
FIGURES_DIR = PROJECT_ROOT / "report" / "figures"

for _directory in (DATASETS_DIR, RESULTS_DIR, FIGURES_DIR):
    _directory.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------------------------------
# Reproducibility
# --------------------------------------------------------------------------



SEED = 42
N_SEEDS = 10
SEEDS = tuple(SEED + i for i in range(N_SEEDS))


TEST_SIZE = 0.20    # 80/20 split
K_FOLDS = 5         # K-fold CV for hyperparameter tuning

# Real dataset
IONOSPHERE_UCI_ID = 52
IONOSPHERE_CACHE = DATASETS_DIR / "ionosphere.csv"
IONOSPHERE_CONSTANT_COLUMN = 1

# Sythetic dataset: two moons
SYNTH_N_SAMPLES = 351
SYNTH_NOISE_SIGMA = 0.25    # std dev of the Gaussian jitter added to positions
SYNTH_CACHE = DATASETS_DIR / "two_moons.csv"
SYNTH_N_SAMPLES_VIZ = 2000

NOISE_LEVELS = (0.0, 0.05, 0.10, 0.20)

T_MAX = 500

#Label encoding
POS_LABEL = 1
NEG_LABEL = -1