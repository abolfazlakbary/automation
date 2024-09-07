import json
import argparse
import requests
from bs4 import BeautifulSoup
import re
import platform
from pathlib import Path


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

def read_subenum_script():
    script_path = Path(__file__).resolve()
    core_root = script_path.parent.parent.__str__()
    if platform.system() == "Windows":
        file_path = core_root + '\\scripts\\subenum\\subenum.sh'
    elif platform.system() == "Linux":
        file_path = core_root + '/scripts/subenum/subenum.sh'
    return file_path

config_data = get_configs()
subenum = read_subenum_script()

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