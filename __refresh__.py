def reload_addon(entry_file_name: str) -> None:
    import sys
    
    dotted_name = entry_file_name + "."
    for name in tuple(sys.modules):
        if name.startswith(dotted_name):
            del sys.modules[name]