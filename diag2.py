import os

folder = 'MYAMA/PROGETTOFINALE/Latex PDF/sezioni/'
files = os.listdir(folder)
for fn in files:
    if not fn.endswith('.tex'): continue
    with open(os.path.join(folder, fn), 'rb') as f:
        c = f.read()
    
    # check A"
    if b'A"' in c:
        print(fn, "has A\"")
    if b'A\xef\xbf\xbd' in c:
        print(fn, "has A (replacement)")
    if b'A\xc2\xb9' in c:
        print(fn, "has A1")
    if b'l\xef\xbf\xbd?T' in c:
        print(fn, "has l?T")
    if b'\xc3\xa8' in c:
        print(fn, "has normal \xc3\xa8 (è)")
    if b'\xc3\xa0' in c:
        print(fn, "has normal \xc3\xa0 (à)")

