import json
import requests
import re
import platform
from pathlib import Path
import asyncio
from core.exceptions.exc import ProccessFailedException

def get_configs():
    script_path = Path(__file__).resolve()
    core_root = script_path.parent.parent.__str__()
    if platform.system() == "Windows":
        file_path = core_root + '\\config\\configs.json'
    elif platform.system() == "Linux":
        file_path = core_root + '/config/configs.json'
    else:
        raise SystemError()
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def read_script(script_dir: str, script_name: str):
    script_path = Path(__file__).resolve()
    core_root = script_path.parent.parent.__str__()
    if platform.system() == "Windows":
        file_path = core_root + f'\\scripts\\{script_dir}\\{script_name}.sh'
    elif platform.system() == "Linux":
        file_path = core_root + f'/scripts/{script_dir}/{script_name}.sh'
    return file_path

### This part must become an API for proccessing SubEnum file output
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36"

session = requests.Session()
session.headers.update({'User-Agent': USER_AGENT})

def extract_html_info(html_content):
    pattern = re.compile(r'\b(?:name|id)="([^"]*)"')
    matches = pattern.findall(html_content)
    return matches

def extract_js_info(js_content):
    pattern = re.compile(r'\b(?:var|let|const|function)\s+([a-zA-Z_$][a-zA-Z0-9_$]*)\b')
    matches = pattern.findall(js_content)
    return matches

def process_url(url, output_file):
    try:
        response = session.get(url, allow_redirects=True)
        response.raise_for_status()
        
        content_type = response.headers.get('Content-Type', '')
        
        with open(output_file, 'a') as out_file:
            if 'text/html' or 'text/xml' or 'application/html' or 'application/xml' in content_type:
                html_info = extract_html_info(response.text)
                out_file.write('\n'.join(html_info) + '\n')
            
            elif 'application/javascript' in content_type:
                js_info = extract_js_info(response.text)
                out_file.write('\n'.join(js_info) + '\n')
    
    except requests.exceptions.RequestException:
        pass  

def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]
    return urls


async def get_proccess_result(process, timeout=120) -> dict:
    try:
        stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=timeout)
    except asyncio.exceptions.TimeoutError:
        raise ProccessFailedException("No Response from server")
    
    stderr_str = stderr.decode() if stderr else ''
    stdout_str = stdout.decode() if stdout else ''
    return {
        "stderr_str": stderr_str,
        "stdout_str": stdout_str
    }


config_data = get_configs()