import subprocess
from core.utils.utils import subenum
from datetime import datetime


class ReconController:
    @staticmethod
    async def get_subenum_info():
        data = subprocess.run(["bash", subenum, "-v"], capture_output=True).__dict__["stdout"]
        output = data.decode("utf-8")
        version = output.split("Version: ")[1].split("\n")[0]
        return {
            "Version": version
        }
        
    @staticmethod
    async def subenum_search(domain: str):
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