import random
import string
from datetime import date
import os
from core.utils.utils import get_app_path

class NucleiOperations:
    @staticmethod
    def remove_big_nuclei(stderr: str):
        output = stderr.replace("\n                     __     _\n   ____  __  _______/ /__  (_)\n  / __ \\/ / / / ___/ / _ \\/ /\n / / / / /_/ / /__/ /  __/ /\n/_/ /_/\\__,_/\\___/_/\\___/_/   ", "Nuclei: ")
        return output

    @staticmethod
    def get_random_string(length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str


    def get_nuclei_path_file(self):
        nuclei_files_dir = os.path.join(get_app_path(), "files/nuclei")
        random_str = self.get_random_string(10)
        filename = f"{random_str}_{date.today()}.json"
        file_path = os.path.join(nuclei_files_dir, filename)
        return file_path