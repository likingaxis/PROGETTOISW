# -*- coding: utf-8 -*-
import os
import re

def clean_latex(s):
    if not s:
        return ''
    # convert italics *text* to \textit{text} or _text_ to \textit{text}
    s = re.sub(r'\*([^*]+)\*', r'\\textit{\1}', s)
    s = re.sub(r'_([^_]+)_', r'\\textit{\1}', s)
    # convert bold **text** to \textbf{text}
    s = re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', s)
    # convert inline code code to \texttt{code}
    s = re.sub(r'([^]+)', r'\\texttt{\1}', s)
    # convert quotes
    s = s.replace('“', '"').replace('”', '"')
    # clean multiple whitespace
    s = ' '.join(s.split())
    return s

def sync_glossario():
    with open('MYAMA/PROGETTOFINALE/versioneMD/2_Glossario/2_Glossario.md', 'r', encoding='utf-8') as f:
        text = f.read()

    raw_rows = re.findall(r'\|\s*\*\*([^*]+)\*\*\s*\|\s*(.*?)\s*\|', text, re.DOTALL)
    
    header = '''\\section{Glossario dei Termini di Dominio}

La presente sezione definisce in modo formale i termini specialistici, gli attori e i concetti fondamentali impiegati nella specifica del sistema \\textbf{MyAma}.

\\begin{center}
\\renewcommand{\\arraystretch}{1.3}
\\begin{longtable}{|p{4.2cm}|p{10.5cm}|}
\\caption{Glossario dei termini e definizioni di dominio} \\label{tab:glossario} \\\\ \\hline
\\rowcolor{tableheader} \\textbf{Termine} & \\textbf{Definizione e Significato nel Sistema} \\\\ \\hline
\\endfirsthead

\\hline
\\rowcolor{tableheader} \\textbf{Termine} & \\textbf{Definizione e Significato nel Sistema} \\\\ \\hline
\\endhead
'''
    rows_tex = []
    for term, defn in raw_rows:
        t_clean = clean_latex(term.strip())
        # clean defn
        d_clean = ' '.join(defn.split())
        d_clean = clean_latex(d_clean)
        # fix any special chars
        d_clean = d_clean.replace('pia- nificazione', 'pianificazione').replace('valutrne', 'valutarne').replace('l\'efficenza', 'l\'efficienza')
        rows_tex.append(f'\\textbf{{{t_clean}}} & {d_clean} \\\\ \\hline')
        
    footer = '''\\end{longtable}
\\end{center}
'''
    full_glossario = header + '\n' + '\n\n'.join(rows_tex) + '\n' + footer
    with open('MYAMA/PROGETTOFINALE/Latex PDF/sezioni/02_glossario.tex', 'w', encoding='utf-8') as f:
        f.write(full_glossario)
    print(f'Sync glossario: {len(raw_rows)} terms.')

sync_glossario()