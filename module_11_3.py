import inspect


def introspection_info(obj):
    obj_info = {}

    obj_info['type'] = type(obj).__name__

    obj_info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]

    obj_info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]

    obj_info['module'] = inspect.getmodule(obj)

    return obj_info

number_info = introspection_info(42)
print(number_info)
