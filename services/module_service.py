from models.module_model import Module

from repositories.module_repository import (
    add_module,
    get_module_by_id,
    save_module,
    module_exists,
)


def find_module(module_id):
    """
    Find a module by its ID.
    """
    return get_module_by_id(module_id)


def module_available(module_id):
    """
    Check if a module ID is available.
    """
    return not module_exists(module_id)


def register_module(module_data):
    """
    Register a new module.
    """
    module_id, module_name, course_id, lecturer_id = module_data

    if module_exists(module_id):
        return False, "Module ID already exists."

    module = Module(
        module_id,
        module_name,
        course_id,
        lecturer_id,
    )

    add_module(module)

    return True, "Module added successfully."


def update_module(module_id, name=None, course_id=None, lecturer_id=None):
    """
    Update an existing module.
    """
    module = get_module_by_id(module_id)

    if module is None:
        return False, "Module not found."

    if name is not None:
        module.module_name = name

    if course_id is not None:
        module.course_id = course_id

    if lecturer_id is not None:
        module.lecturer_id = lecturer_id

    save_module(module)

    return True, module