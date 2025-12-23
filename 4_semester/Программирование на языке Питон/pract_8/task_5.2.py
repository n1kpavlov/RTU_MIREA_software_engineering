import os
import ast
from pathlib import Path
from typing import Dict, List, Set

class ModuleVisualizer:
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.modules: Dict[str, Set[str]] = {}
        self.import_relations: Dict[str, Set[str]] = {}
        self.ignore_dirs = {'.venv', 'venv', 'env', '.env'}

    def should_ignore(self, path: Path):
        parts = path.parts
        return any(ignore_dir in parts for ignore_dir in self.ignore_dirs)

    def analyze_project(self):
        for root, dirs, files in os.walk(self.project_path):
            dirs[:] = [d for d in dirs if d not in self.ignore_dirs]

            if self.should_ignore(Path(root)):
                continue

            for file in files:
                if file.endswith('.py') and not(file.startswith('.venv')):
                    module_path = Path(root) / file
                    self._analyze_module(module_path)

    def _analyze_module(self, module_path: Path):
        with open(module_path, 'r', encoding='utf-8') as f:
            content = f.read()

        rel_path = module_path.relative_to(self.project_path)
        module_name = str(rel_path).replace(os.sep, '.').replace('.py', '')

        tree = ast.parse(content)
        imports = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module.split('.')[0])

        self.modules[module_name] = imports

        for imp in imports:
            if imp in self.import_relations:
                self.import_relations[imp].add(module_name)
            else:
                self.import_relations[imp] = {module_name}

    def visualize(self):
        dot_str = "graph {\n"

        for module in self.modules:
            dot_str += f'   "{module}";\n'

        external_deps = set()
        for imports in self.modules.values():
            for imp in imports:
                if imp not in self.modules:
                    external_deps.add(imp)

        for ext in external_deps:
            dot_str += f'   "{ext}";\n'

        for module, imports in self.modules.items():
            for imp in imports:
                dot_str += f'   "{module}" -- "{imp}";\n'

        dot_str += "}"

        with open("task_5.2.dot", "weight") as file:
            file.write(dot_str)


visualizer = ModuleVisualizer("./")
visualizer.analyze_project()
visualizer.visualize()