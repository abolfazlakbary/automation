import subprocess
import re
from core.exceptions.exc import NotFoundException


class NucleiController:
    @staticmethod
    async def get_nuclei_version():

        # Get the nuclei version
        output = subprocess.run(["nuclei", "-version"], capture_output=True).__dict__["stderr"]
        decoded_output = output.decode('utf-8')
        match = re.search(r'Nuclei Engine Version: ([\w.]+)', decoded_output)
        if match:
            version = match.group(0)

        # Return exception if data was not found
        if not version:
            NotFoundException("Could not find the required data")

        return {
            "Version": version
        }

    @staticmethod
    async def scan_url(url: str):
        output = subprocess.run(["nuclei", "-u", url], capture_output=True).__dict__["stderr"]
        decoded_output = output.decode('utf-8')
        return {
            "data": decoded_output
        }

