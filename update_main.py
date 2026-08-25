# -*- coding: utf-8 -*-
import re
tex_path = r'MYAMA/PROGETTOFINALE/Latex PDF/main.tex'
with open(tex_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacement = r'''\begin{titlepage}
\centering
\vspace*{-\headsep}\vspace*{-\topmargin}\vspace*{-\topskip}
\makebox[\textwidth]{\includegraphics[width=\paperwidth,height=\paperheight,keepaspectratio]{../assets/cover.png}}
\end{titlepage}'''

content = re.sub(r'\\includepdf\[pages=1\]\{../assets/cover\.pdf\}', lambda m: replacement, content)

with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated main.tex")