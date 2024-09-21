from core.utils.utils import get_proccess_result
import re
from core.exceptions.exc import NotFoundException
import asyncio
from core.utils import utils
from .operations.operate import NucleiOperations


operate = NucleiOperations()


class NucleiController:
    @staticmethod
    async def get_nuclei_version():

        # Get the nuclei version
        process = await asyncio.create_subprocess_exec(
            "nuclei", "-version", "-silent",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        process_result = await get_proccess_result(process)
        
        match = re.search(r'Nuclei Engine Version: ([\w.]+)', process_result["stderr_str"])
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
        configs = utils.get_configs()
        
        process = await asyncio.create_subprocess_exec(
        'nuclei', '-u', url, "-nc",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
        )
        
        process_result = await get_proccess_result(process, timeout=configs["packages"]["nuclei"]["request_timeout"])
        stderr = operate.remove_big_nuclei(process_result["stderr_str"])
        stdout = process_result["stdout_str"]
        
        return {
            "stderr": stderr,
            "stdout": stdout
        }

