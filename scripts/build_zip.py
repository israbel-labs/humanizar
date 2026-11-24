"""Arma dist/humanizar.zip para subirlo en Claude Desktop o claude.ai.

Uso: python scripts/build_zip.py
El .zip contiene la carpeta humanizar/ con SKILL.md y LICENSE.
"""

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ["SKILL.md", "LICENSE"]


def main() -> None:
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    target = dist / "humanizar.zip"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for name in FILES:
            archive.write(ROOT / name, f"humanizar/{name}")
    print(f"Listo: {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
