from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_file: Path
    

@dataclass(frozen=True)
class DataPreprocessConfig:
    root_dir: Path
    load_file_path: Path
    local_file: Path
    params_select_columns: list


@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    load_file_path: Path
    test_data_save: Path
    model_save: Path