from core.utils.utils import get_proccess_result
import re
from core.exceptions.exc import NotFoundException
import asyncio


class NucleiController:
    @staticmethod
    async def get_nuclei_version():

        # Get the nuclei version
        process = await asyncio.create_subprocess_exec(
            "nuclei", "-version",
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
        process = await asyncio.create_subprocess_exec(
        'nuclei', '-u', url,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
        )
        process_result = await get_proccess_result(process)

        return {
            "data": process_result["stderr_str"]
        }

