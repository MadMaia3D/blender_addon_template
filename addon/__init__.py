from . import panel_example
from . import operator_example

def register_addon() -> None:
    operator_example.register()
    panel_example.register()


def unregister_addon() -> None:
    panel_example.unregister()
    operator_example.unregister()