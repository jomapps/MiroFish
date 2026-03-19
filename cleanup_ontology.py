import os

file_path = r"d:\Projects\sales-simulation\MiroFish\backend\app\services\ontology_generator.py"
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if 'ONTOLOGY_SYSTEM_PROMPT = ""' in line:
        new_lines.append(line)
        skip = True
        continue
    if skip and 'class OntologyGenerator:' in line:
        skip = False
    
    if not skip:
        new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Cleaned up ontology_generator.py")
