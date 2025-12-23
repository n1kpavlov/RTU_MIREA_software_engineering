import inspect
import importlib.util
import sys


def generate_documentation(module_file: str) -> str:
    spec = importlib.util.spec_from_file_location("m", module_file)
    module = importlib.util.module_from_spec(spec)
    sys.modules["m"] = module
    spec.loader.exec_module(module)

    md_lines = []

    module_name = module.__name__
    md_lines.append(f"# Модуль {module_name}\n")

    module_doc = inspect.getdoc(module)
    if module_doc:
        md_lines.append(f"{module_doc}\n")

    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            md_lines.append(f"## Класс {name}\n")

            class_doc = inspect.getdoc(obj)
            if class_doc:
                md_lines.append(f"{class_doc}\n")

            for method_name, method_obj in inspect.getmembers(obj):
                if inspect.isfunction(method_obj) or inspect.ismethod(method_obj):
                    if method_name.startswith('__') and method_name.endswith('__'):
                        continue

                    sig = inspect.signature(method_obj)
                    md_lines.append(f"* **Метод** `{method_name}{sig}`\n")

                    method_doc = inspect.getdoc(method_obj)
                    if method_doc:
                        md_lines.append(f"{method_doc}\n")

    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj) and not name.startswith('_'):
            md_lines.append(f"## Функция {name}\n")

            sig = inspect.signature(obj)
            md_lines.append(f"Сигнатура: `{name}{sig}`\n")

            func_doc = inspect.getdoc(obj)
            if func_doc:
                md_lines.append(f"{func_doc}\n")

    return '\n'.join(md_lines)


documentation = generate_documentation("task_5_module.py")
print(documentation)