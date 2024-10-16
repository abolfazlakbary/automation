import subprocess
from core.utils.utils import read_script, get_configs
import asyncio
from core.utils.utils import get_proccess_result , get_proccess_result_shell

class ReconController:
    @staticmethod
    async def get_subenum_info():
        subenum = read_script(script_dir="subenum", script_name="subenum")
        command_1 = ["bash", subenum, "-v"]
        output_1, error_1 = await get_proccess_result(command_1)
        version = output_1.split("Version: ")[1].split("\n")[0]

        return {
            "Version": version
        }
        
    @staticmethod
    async def subenum_search(domain: str):
        configs = get_configs()
        subenum = read_script(script_dir="subenum", script_name="subenum")

        command = f"{subenum} -d {domain} -o {domain} && cat {domain} |dir |sort -u > dir && python3 paramminer.py dir output"

        stderr, stdout = await get_proccess_result_shell(command, timeout=configs["packages"]["subenum"]["request_timeout"])

        return {
            "stderr": stderr,
            "stdout": stdout
        }
