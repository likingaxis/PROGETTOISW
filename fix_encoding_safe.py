# -*- coding: utf-8 -*-
import os

replacements = {
    'cittA\ufffd': 'citt\u00E0',
    'difficoltA\ufffd': 'difficolt\u00E0',
    'A"': '\u00E8',
    'puA\ufffd': 'pu\u00F2',
    'funzionalitA\ufffd': 'funzionalit\u00E0',
    'capacitA\ufffd': 'capacit\u00E0',
    'attivitA\ufffd': 'attivit\u00E0',
    'conformitA\ufffd': 'conformit\u00E0',
    'entitA\ufffd': 'entit\u00E0',
    'UniversitA\ufffd': 'Universit\u00E0',
    'modalitA\ufffd': 'modalit\u00E0',
    'validitA\ufffd': 'validit\u00E0',
    'quantitA\ufffd': 'quantit\u00E0',
    'qualitA\ufffd': 'qualit\u00E0',
    'proprietA\ufffd': 'propriet\u00E0',
    'prioritA\ufffd': 'priorit\u00E0',
    'possibilitA\ufffd': 'possibilit\u00E0',
    'disponibilitA\ufffd': 'disponibilit\u00E0',
    'PIA^': 'PI\u00C8',
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
        if file.endswith('.tex'):
            fix_file(os.path.join(root, file))