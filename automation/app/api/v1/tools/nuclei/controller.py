from core.utils.utils import get_proccess_result, get_app_path
import re
from core.exceptions.exc import NotFoundException, ProccessFailedException
import asyncio
from core.utils import utils
from .operations.operate import NucleiOperations
from datetime import date
import json
import os


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

        nuclei_files_dir = os.path.join(get_app_path(), "files/nuclei")
    
        random_str = operate.get_random_string(10)
        filename = f"{random_str}_{date.today()}.json"
        file_path = os.path.join(nuclei_files_dir, filename)
        
        process_1 = await asyncio.create_subprocess_exec(
        'nuclei', '-u', url, "-nc", "-json-export", f"{file_path}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
        )
        
        await get_proccess_result(process_1, timeout=configs["packages"]["nuclei"]["request_timeout"])
        process_2 = await asyncio.create_subprocess_exec(
        "cat", f"{file_path}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
        )
        json_data = await get_proccess_result(process_2, timeout=configs["packages"]["nuclei"]["request_timeout"])
        try:
            standard_json = json.loads(json_data["stdout_str"])
        except Exception as e:
            print({"json_data": json_data})
            print(e)
            raise ProccessFailedException("There was an error in loading json data")
        
        process_3 = await asyncio.create_subprocess_exec(
            "rm", f"{file_path}",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        await get_proccess_result(process_3, timeout=configs["packages"]["nuclei"]["request_timeout"])
        return standard_json

