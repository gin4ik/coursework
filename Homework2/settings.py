from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIR_PATH = Path.joinpath(ROOT, 'dir')
PROF_PATH = Path.joinpath(DIR_PATH, 'professions.json')
STUDENT_PATH = Path.joinpath(DIR_PATH, 'students.json')