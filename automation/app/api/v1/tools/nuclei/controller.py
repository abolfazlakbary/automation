from core.utils.utils import get_proccess_result, get_app_path, get_configs
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
        command_1 = ["nuclei", "-version", "-silent"] # See version
        output_1, error_1 = await get_proccess_result(command_1)
        
        match = re.search(r'Nuclei Engine Version: ([\w.]+)', error_1)
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
        config_data = get_configs()
        request_timeout = config_data["packages"]["nuclei"]["request_timeout"]
        
        # 0 - make a random path for the file
        file_path = operate.get_nuclei_path_file()
        
        # 1 - Request the desired url for scan
        command_1 = ['nuclei', '-u', url, "-nc", "-json-export", file_path]
        output_1, error_1 = await get_proccess_result(command_1, request_timeout)
    
        # 2 - Get Json data
        command_2 = ["cat", file_path]
        output_2, error_2 = await get_proccess_result(command_2, request_timeout)
        
        # 3 - Try to load json data
        try:
            standard_json = json.loads(output_2)
        except:
            raise ProccessFailedException("There was an error in loading json data")
        
        # 4 - Remove the file
        command_3 = ["rm", file_path]
        output_3, error_3 = await get_proccess_result(command_3, request_timeout)
        
        return standard_json

