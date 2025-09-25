import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "dados" / "raw"
TRUSTED_DIR = BASE_DIR / "dados" / "trusted"

# Arquivos brutos
PARTICIPANTES_RAW = RAW_DIR / "participantes-2024.parquet"
NOTA_RAW = RAW_DIR / "resultados-2024.parquet"

# Arquivo final tratado
OUTPUT_TRUSTED = TRUSTED_DIR / "nota-participates-enem2024.parquet"

REFINED_DIR = BASE_DIR / "dados" / "refined"