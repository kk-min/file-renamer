from pathlib import Path

# Current working directory
dir = Path(__file__).resolve().parent

for filepath in dir.glob('*(z-lib.org)*'):
    print(filepath)
    renamed_filepath = str(filepath).replace(' (z-lib.org)', '')
    print(renamed_filepath)
    filepath.rename(renamed_filepath)
