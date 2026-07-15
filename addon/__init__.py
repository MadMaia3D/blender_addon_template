from . import template_list_example
from . import operator_example
from . import panel_example


def register_addon() -> None:
    template_list_example.register()
    operator_example.register()
    panel_example.register()


def unregister_addon() -> None:
    panel_example.unregister()
    operator_example.unregister()
    template_list_example.unregister()