def decorate_module_functions(decorator):
    import builtins
    original_import = builtins.__import__

    def new_import(name, globals=None, locals=None, fromlist=(), level=0):
        module = original_import(name, globals, locals, fromlist, level)
        if hasattr(module, '__decorate__'):
            for attr in getattr(module, '__decorate__'):
                setattr(module, attr, decorator(getattr(module, attr)))
        return module

    builtins.__import__ = new_import
