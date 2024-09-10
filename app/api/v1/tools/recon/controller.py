import subprocess
from core.utils.utils import read_script


class ReconController:
    @staticmethod
    async def get_subenum_info():
        subenum = read_script(script_dir="subenum", script_name="subenum")
        data = subprocess.run(["bash", subenum, "-v"], capture_output=True).__dict__["stdout"]
        output = data.decode("utf-8")
        version = output.split("Version: ")[1].split("\n")[0]
        return {
            "Version": version
        }
        
    @staticmethod
    async def subenum_search(domain: str):
        subenum = read_script(script_dir="subenum", script_name="subenum")
        data = subprocess.run(
            [
            "bash",
            subenum,
            "-d", domain,
            "-o", f"./files/subenum/{domain}.txt"
            ], capture_output=True).__dict__["stdout"]
        return {
            "data": data
        }
    
    @staticmethod
    async def subenum_process(subenum_filename: str):
        domain_proccess = read_script(script_dir="subenum", script_name="domain_process")

        