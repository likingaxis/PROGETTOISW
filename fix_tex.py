import os
fp = 'MYAMA/PROGETTOFINALE/Latex PDF/sezioni/06_design_patterns.tex'
with open(fp, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    "\\fbox{\\parbox[c][5cm][c]{0.85\\textwidth}{\\centering \\textsf{[ Inserire qui il Diagramma UML dell'Observer Pattern esportato da Visual Paradigm ]}}}",
    "\\includegraphics[width=0.95\\textwidth]{figure/pattern_observer.jpg}"
)

with open(fp, 'w', encoding='utf-8') as f:
    f.write(c)
