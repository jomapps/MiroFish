import os
import re
import json

def extract_chinese_strings(directory):
    chinese_map = {}
    # Regex for Chinese characters
    # We want to match whole phrases if possible.
    chinese_regex = re.compile(r'[\u4e00-\u9fff][\u4e00-\u9fff\s\w\d\.\!/,，。？！]*')

    for root, dirs, files in os.walk(directory):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        if '.git' in dirs:
            dirs.remove('.git')
        
        for file in files:
            if file.endswith(('.vue', '.js', '.py')):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        matches = chinese_regex.finditer(content)
                        for match in matches:
                            string = match.group().strip()
                            if string:
                                chinese_map[string] = ""
                except:
                    pass

    return chinese_map

if __name__ == "__main__":
    # Frontend translation
    frontend_src = r"d:\Projects\sales-simulation\MiroFish\frontend\src"
    frontend_map = extract_chinese_strings(frontend_src)
    frontend_output = r"d:\Projects\sales-simulation\MiroFish\frontend\en-map.json"
    
    with open(frontend_output, 'w', encoding='utf-8') as f:
        json.dump(frontend_map, f, ensure_ascii=False, indent=2)
    
    print(f"Extracted {len(frontend_map)} frontend strings.")

    # Backend translation
    backend_app = r"d:\Projects\sales-simulation\MiroFish\backend\app"
    backend_map = extract_chinese_strings(backend_app)
    backend_output = r"d:\Projects\sales-simulation\MiroFish\backend\app\prompts_map.json"
    
    with open(backend_output, 'w', encoding='utf-8') as f:
        json.dump(backend_map, f, ensure_ascii=False, indent=2)
    
    print(f"Extracted {len(backend_map)} backend strings.")
