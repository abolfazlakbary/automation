import random
import string


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