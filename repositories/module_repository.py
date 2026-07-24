from file_manager import (
    read_modules,
    write_modules,
)

from models.module_model import Module


def get_all_modules() -> list[Module]:
    """
    Return all modules.
    """
    records = read_modules()
    return [Module.from_record(record) for record in records]


def get_module_by_id(module_id: str) -> Module | None:
    """
    Find a module by its ID.
    """
    for module in get_all_modules():
        if module.module_id == module_id:
            return module
    return None


def save_all_modules(modules: list[Module]):
    """
    Save all modules.
    """
    records = [module.to_record() for module in modules]
    write_modules(records)


def add_module(module: Module):
    """
    Add a new module.
    """
    modules = get_all_modules()
    modules.append(module)
    save_all_modules(modules)


def save_module(updated_module: Module):
    """
    Update an existing module.
    """
    modules = get_all_modules()

    for i, module in enumerate(modules):
        if module.module_id == updated_module.module_id:
            modules[i] = updated_module
            break

    save_all_modules(modules)


def module_exists(module_id: str) -> bool:
    """
    Check if a module already exists.
    """
    return get_module_by_id(module_id) is not None