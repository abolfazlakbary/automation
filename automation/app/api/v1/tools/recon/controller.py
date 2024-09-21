import subprocess
from core.utils.utils import read_script, get_configs
import asyncio
from core.utils.utils import get_proccess_result

class ReconController:
    @staticmethod
    async def get_subenum_info():
        configs = get_configs()
        subenum = read_script(script_dir="subenum", script_name="subenum")
        
        process = await asyncio.create_subprocess_exec(
        "bash", subenum, "-v",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
        )
        
        process_result = await get_proccess_result(process, timeout=configs["packages"]["subenum"]["request_timeout"])
        stdout = process_result["stdout_str"]
        version = stdout.split("Version: ")[1].split("\n")[0]
        
        return {
            "Version": version
        }
        
    @staticmethod
    async def subenum_search(domain: str):
        configs = get_configs()
        subenum = read_script(script_dir="subenum", script_name="subenum")

        process = await asyncio.create_subprocess_exec(
        "bash", subenum, "-d", domain, 
        "-o", f"./files/subenum/{domain}.txt",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
        )
        
        process_result = await get_proccess_result(process, timeout=configs["packages"]["subenum"]["request_timeout"])
        stdout = process_result["stdout_str"]
        stderr = process_result["stderr_str"]
        
        return {
            "stderr": stderr,
            "stdout": stdout
        }
