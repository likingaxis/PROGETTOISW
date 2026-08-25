# -*- coding: utf-8 -*-
import os

replacements = {
    'cittA': 'città',
    'difficoltA': 'difficoltà',
    'A"': 'è',
    'puA': 'può',
    'funzionalitA': 'funzionalità',
    'capacitA': 'capacità',
    'attivitA': 'attività',
    'conformitA': 'conformità',
    'entitA': 'entità',
    'UniversitA': 'Università',
    'modalitA': 'modalità',
    'validitA': 'validità',
    'quantitA': 'quantità',
    'qualitA': 'qualità',
    'proprietA': 'proprietà',
    'prioritA': 'priorità',
    'possibilitA': 'possibilità',
    'disponibilitA': 'disponibilità',
    'PIA^': 'PIÈ',
}

def fix_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    new_content = content
    for k, v in replacements.items():
        new_content = new_content.replace(k, v)
        
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Fixed {path}')

for root, dirs, files in os.walk('MYAMA/PROGETTOFINALE'):
    for file in files:
        if file.endswith('.tex') or file.endswith('.md'):
            fix_file(os.path.join(root, file))