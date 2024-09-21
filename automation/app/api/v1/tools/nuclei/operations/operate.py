class NucleiOperations:
    @staticmethod
    def remove_big_nuclei(stderr: str):
        output = stderr.replace("\n                     __     _\n   ____  __  _______/ /__  (_)\n  / __ \\/ / / / ___/ / _ \\/ /\n / / / / /_/ / /__/ /  __/ /\n/_/ /_/\\__,_/\\___/_/\\___/_/   ", "Nuclei: ")
        return output
