from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def project_path(*parts):
    return BASE_DIR.joinpath(*parts)
