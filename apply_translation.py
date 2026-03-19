import os
import json
import re

def apply_translation(directory, map_path):
    if not os.path.exists(map_path):
        print(f"Map not found: {map_path}")
        return
    
    with open(map_path, 'r', encoding='utf-8') as f:
        translation_map = json.load(f)
    
    # Sort keys by length descending to avoid partial matches
    sorted_keys = sorted(translation_map.keys(), key=len, reverse=True)
    
    for root, dirs, files in os.walk(directory):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        
        for file in files:
            if file.endswith(('.vue', '.js', '.html', '.py')):
                path = os.path.join(root, file)
                print(f"Translating {path}...")
                
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    translated_content = content
                    count = 0
                    for key in sorted_keys:
                        val = translation_map[key]
                        if val and val.strip() != "" and key in translated_content:
                            # Escape special regex characters in the key
                            escaped_key = re.escape(key)
                            # Simple replacement
                            # Use a while loop or replaceAll equivalent if needed
                            # In Python, str.replace() replaces all by default
                            translated_content = translated_content.replace(key, val)
                            count += 1
                    
                    if translated_content != content:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(translated_content)
                        print(f"  Done. Replaced {count} unique strings.")
                except Exception as e:
                    print(f"  Error on {file}: {e}")

if __name__ == "__main__":
    import sys
    target_dir = sys.argv[1] if len(sys.argv) > 1 else r"d:\Projects\sales-simulation\MiroFish\frontend-english"
    frontend_dir = r"d:\Projects\sales-simulation\MiroFish\frontend-english"
    map_path = os.path.join(frontend_dir, "en-map.json")
    apply_translation(target_dir, map_path)
