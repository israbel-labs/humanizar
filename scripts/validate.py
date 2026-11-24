"""Revisa que el paquete de humanizar esté coherente antes de publicar.

Uso: python scripts/validate.py
Solo usa la biblioteca estándar de Python 3.13.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPECTED_PATTERNS = 29
MAX_DESCRIPTION = 1024


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []
    skill = read("SKILL.md")
    readme = read("README.md")
    changelog = read("CHANGELOG.md")
    plugin = json.loads(read(".claude-plugin/plugin.json"))
    marketplace = json.loads(read(".claude-plugin/marketplace.json"))

    frontmatter = re.match(r"---\n(.*?)\n---\n", skill, re.S)
    if not frontmatter:
        return fail(["SKILL.md no tiene frontmatter YAML."])
    meta = frontmatter.group(1)

    version = re.search(r'^\s+version:\s*"([^"]+)"', meta, re.M)
    if not version:
        return fail(["SKILL.md no tiene metadata.version."])
    version = version.group(1)

    name = re.search(r"^name:\s*(\S+)", meta, re.M)
    if not name or name.group(1) != "humanizar":
        errors.append("El name del frontmatter debe ser humanizar.")

    description = re.search(r"^description:\s*(.+)$", meta, re.M)
    if not description:
        errors.append("Falta description en el frontmatter.")
    elif len(description.group(1)) > MAX_DESCRIPTION:
        errors.append(f"La description pasa de {MAX_DESCRIPTION} caracteres.")

    # El cuerpo repite la versión porque Claude no siempre ve el frontmatter.
    body_versions = set(re.findall(r"versión (\d+\.\d+\.\d+) de humanizar", skill))
    body_versions |= set(re.findall(r"mayor que (\d+\.\d+\.\d+)", skill))
    if body_versions != {version}:
        errors.append(f"Versiones en el cuerpo de SKILL.md {sorted(body_versions)} no coinciden con {version}.")

    if plugin.get("version") != version:
        errors.append(f"plugin.json tiene la versión {plugin.get('version')}, SKILL.md tiene {version}.")

    first_entry = re.search(r"^## (\S+)", changelog, re.M)
    if not first_entry or first_entry.group(1) != version:
        errors.append(f"La primera entrada de CHANGELOG.md debe ser ## {version}.")

    names = {plugin.get("name"), marketplace["plugins"][0].get("name")}
    if names != {"humanizar"}:
        errors.append(f"Los manifiestos deben llamar humanizar al plugin, no {sorted(map(str, names))}.")

    numbers = [int(n) for n in re.findall(r"^### (\d+)\. ", skill, re.M)]
    if numbers != list(range(1, EXPECTED_PATTERNS + 1)):
        errors.append(f"Los patrones deben ir del 1 al {EXPECTED_PATTERNS} sin saltos ni repeticiones: {numbers}")

    for cited in re.findall(r"^\| (\d+(?:, \d+)*) \|", readme, re.M):
        for number in cited.split(", "):
            if int(number) not in numbers:
                errors.append(f"El README cita el §{number}, que no existe en SKILL.md.")

    # GitHub mete la etiqueta en la cita anterior si no hay una línea en blanco.
    lines = skill.splitlines()
    for index, line in enumerate(lines[1:], start=1):
        if re.match(r"\*\*(Antes|Después|Busca|Problema|Regla)", line) and lines[index - 1].strip():
            errors.append(f"SKILL.md línea {index + 1}: falta una línea en blanco antes de '{line[:30]}'.")

    if errors:
        return fail(errors)
    print(f"Todo en orden: humanizar {version}, {len(numbers)} patrones.")
    return 0


def fail(errors: list[str]) -> int:
    for error in errors:
        print(f"ERROR: {error}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
