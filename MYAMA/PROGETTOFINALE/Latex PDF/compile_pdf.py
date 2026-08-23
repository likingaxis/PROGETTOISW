#!/usr/bin/env python3
"""
Script di compilazione automatica per documenti LaTeX (MyAma).
Tutti i file ausiliari (.aux, .log, .toc, ecc.) vengono salvati nella cartella 'build/',
lasciando la cartella 'consegna/' perfettamente pulita con il solo 'main.pdf'.

Uso:
    python compile_pdf.py           # Compilazione a 2 passate + apertura PDF
    python compile_pdf.py --clean   # Svuota la cartella build/
    python compile_pdf.py --no-open # Compila senza aprire il visualizzatore
    python compile_pdf.py --single  # Singola passata rapida
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

# Assicura supporto UTF-8 per il terminale Windows
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Percorsi principali
SCRIPT_DIR = Path(__file__).resolve().parent
TEX_FILE = "main.tex"
PDF_FILE = "main.pdf"
BUILD_DIR = SCRIPT_DIR / "build"

# Estensioni dei file ausiliari generati da LaTeX
AUX_EXTENSIONS = [
    ".aux", ".log", ".out", ".toc", ".lof", ".lot", 
    ".fls", ".fdb_latexmk", ".synctex.gz"
]

def find_pdflatex():
    """Cerca l'eseguibile pdflatex nel PATH o nei percorsi noti di installazione."""
    pdflatex_path = shutil.which("pdflatex")
    if pdflatex_path:
        return pdflatex_path

    possible_paths = [
        Path.home() / "AppData" / "Local" / "Programs" / "MiKTeX" / "miktex" / "bin" / "x64" / "pdflatex.exe",
        Path("C:/Program Files/MiKTeX/miktex/bin/x64/pdflatex.exe"),
        Path("C:/Program Files (x86)/MiKTeX/miktex/bin/pdflatex.exe"),
        Path("C:/texlive/2025/bin/windows/pdflatex.exe"),
        Path("C:/texlive/2026/bin/windows/pdflatex.exe"),
    ]

    for p in possible_paths:
        if p.exists():
            return str(p)

    return None

def clean_root_aux():
    """Rimuove eventuali file temporanei rimasti nella cartella radice."""
    for ext in AUX_EXTENSIONS:
        for f in SCRIPT_DIR.glob(f"*{ext}"):
            try:
                f.unlink()
            except Exception:
                pass

def clean_build_dir():
    """Svuota completamente la cartella build/."""
    print("[*] Pulizia della cartella build/ in corso...")
    clean_root_aux()
    count = 0
    if BUILD_DIR.exists():
        for item in BUILD_DIR.iterdir():
            try:
                if item.is_file():
                    item.unlink()
                    count += 1
                elif item.is_dir():
                    shutil.rmtree(item)
                    count += 1
            except Exception as e:
                print(f"  [!] Impossibile eliminare {item.name}: {e}")
    print(f"  Rimossi {count} file temporanei da build/.\n")

def compile_latex(pdflatex_bin, passes=2):
    """Esegue la compilazione di main.tex indirizzando i file ausiliari in build/."""
    target_tex = SCRIPT_DIR / TEX_FILE
    if not target_tex.exists():
        print(f"[X] Errore: File {TEX_FILE} non trovato in {SCRIPT_DIR}")
        sys.exit(1)

    # Crea la cartella build se non esiste
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    
    # Rimuove file ausiliari sparsi nella root
    clean_root_aux()

    print("=" * 60)
    print(f"[+] Avvio compilazione LaTeX: {TEX_FILE}")
    print(f"    Compilatore:    {pdflatex_bin}")
    print(f"    Cartella temp:  build/")
    print("=" * 60)

    for i in range(1, passes + 1):
        desc = "struttura e bozza" if i == 1 else "sincronizzazione indici e riferimenti"
        print(f"\n>> Passata {i}/{passes} ({desc})...")
        cmd = [
            pdflatex_bin,
            "-aux-directory=build",
            "-interaction=nonstopmode",
            "-halt-on-error",
            TEX_FILE
        ]
        
        result = subprocess.run(
            cmd,
            cwd=SCRIPT_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace"
        )

        if result.returncode != 0:
            print(f"\n[X] Errore durante la compilazione (passata {i}):\n")
            log_lines = result.stdout.splitlines()
            errors = [line for line in log_lines if line.startswith("!") or "Error" in line]
            if errors:
                for err in errors[:10]:
                    print(f"   - {err}")
            else:
                for line in log_lines[-20:]:
                    print(f"   {line}")
            print(f"\nConsulta 'build/main.log' per il log completo degli errori.")
            return False

    pdf_path = SCRIPT_DIR / PDF_FILE
    if pdf_path.exists():
        size_kb = pdf_path.stat().st_size / 1024
        print("\n" + "=" * 60)
        print("[V] COMPILAZIONE COMPLETATA CON SUCCESSO!")
        print(f"    File generato: {pdf_path}")
        print(f"    Dimensione:    {size_kb:.1f} KB")
        print("=" * 60)
        return True
    else:
        print("\n[X] Errore imprevisto: il file PDF non e' stato generato.")
        return False

def open_pdf():
    """Apre il file PDF con il visualizzatore predefinito del sistema."""
    pdf_path = SCRIPT_DIR / PDF_FILE
    if not pdf_path.exists():
        return

    print(f"\n[*] Apertura di {PDF_FILE} con il visualizzatore di sistema...")
    try:
        if sys.platform.startswith("win"):
            os.startfile(str(pdf_path))
        elif sys.platform.startswith("darwin"):
            subprocess.run(["open", str(pdf_path)])
        else:
            subprocess.run(["xdg-open", str(pdf_path)])
    except Exception as e:
        print(f"  [!] Impossibile aprire automaticamente il PDF: {e}")

def main():
    args = sys.argv[1:]
    should_clean = "--clean" in args
    no_open = "--no-open" in args
    single_pass = "--single" in args

    if should_clean and len(args) == 1:
        clean_build_dir()
        return

    pdflatex_bin = find_pdflatex()
    if not pdflatex_bin:
        print("[X] Errore: pdflatex non e' stato trovato nel sistema.")
        print("    Assicurati che MiKTeX sia installato.")
        sys.exit(1)

    passes = 1 if single_pass else 2
    success = compile_latex(pdflatex_bin, passes=passes)

    if success:
        if not no_open:
            open_pdf()

if __name__ == "__main__":
    main()
