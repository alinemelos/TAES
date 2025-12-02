import subprocess
import sys
from pipeline.render import render_with_kroki


PIPELINE_SCRIPTS = [
    "pipeline/extractor.py",
    "pipeline/usecase.py",
    "pipeline/classes.py",
    "pipeline/sequence.py",
    "pipeline/verify.py"
]

def run_script(path: str):
    print(f"\n[RUNNING] {path} ...")
    result = subprocess.run([sys.executable, path], capture_output=True, text=True)

    if result.returncode != 0:
        print(f"[ERROR] An error occurred while executing {path}:")
        print(result.stderr)
        sys.exit(1)
    
    print(f"[OK] {path} completed successfully.")

def render_all_diagrams():
    print("\n=== Rendering UML diagrams via Kroki ===")

    diagrams = [
        ("data/usecase.puml", "diagrams/usecase.png"),
        ("data/classes.puml", "diagrams/classes.png"),
        ("data/sequence.puml", "diagrams/sequence.png")
    ]

    for src, dst in diagrams:
        try:
            render_with_kroki(src, dst)
        except Exception as e:
            print(f"[ERROR] Failed to render {src}: {e}")
            sys.exit(1)

def main():
    print("\n=== STARTING UML PIPELINE ===")

    # Executa cada etapa
    for script in PIPELINE_SCRIPTS:
        run_script(script)

    print("\n=== PIPELINE EXECUTION FINISHED SUCCESSFULLY ===")
    print("Generated outputs in /data:")
    print("- root.json")
    print("- usecase.puml")
    print("- classes.puml")
    print("- sequence.puml")
    print("- verify.json")

    # Renderização das imagens PNG via Kroki
    render_all_diagrams()

    print("\n=== ALL DIAGRAM PNG FILES GENERATED SUCCESSFULLY ===")
    print("Files available in /data:")
    print("- usecase.png")
    print("- classes.png")
    print("- sequence.png")

if __name__ == "__main__":
    main()