import os


def get_problem_from_cwd():
    return os.path.basename(os.getcwd())