
import ast
import sys
from pathlib import Path

BASE = Path(__file__).parent
modules = set()

for file in BASE.rglob("*.py"):
    if any(part in {".venv", "venv", "__pycache__"} for part in file.parts):
        continue

    try:
        tree = ast.parse(file.read_text(encoding="utf-8-sig"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    modules.add(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules.add(node.module.split(".")[0])
    except (SyntaxError, UnicodeDecodeError, OSError):
        print("Skipped:", file.relative_to(BASE))

standard_library = set(sys.stdlib_module_names)

external = sorted(modules - standard_library)

print("PYTHON VERSION:", sys.version.split()[0])
print("\nEXTERNAL IMPORTS:")
for module in external:
    print("-", module)

print("\nINSTALLED PACKAGE VERSIONS:")
from importlib.metadata import PackageNotFoundError, version

for package in external:
    try:
        print(f"{package}: {version(package)}")
    except PackageNotFoundError:
        print(f"{package}: package mapping/version needs checking")
