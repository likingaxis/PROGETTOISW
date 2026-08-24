import os

folder = 'MYAMA/PROGETTOFINALE/Latex PDF/sezioni/'
files = os.listdir(folder)
for fn in files:
    if not fn.endswith('.tex'): continue
    with open(os.path.join(folder, fn), 'rb') as f:
        c = f.read()
    
    # Let's find all occurrences of 'A' followed by non-ascii or weird ascii
    print(f"--- {fn} ---")
    for i in range(len(c) - 1):
        if c[i] == ord('A') and c[i+1] > 127:
            print(f"Found A + {c[i+1:i+3]}")
        elif c[i:i+4] == b'l\xe2\x80\x99':
            print("Found l + smart quote")
        elif c[i:i+4] == b'l\xef\xbf\xbd':
            print("Found l + replacement char")
