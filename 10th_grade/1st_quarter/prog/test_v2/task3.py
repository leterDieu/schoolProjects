from typing import Callable
from functools import wraps
import inspect
import re


class Logger:
    log_levels = {
        'debug': 0,
        'info': 1,
        'warning': 2,
        'error': 3
    }

    pattern_print = r"^(?P<indent>\s*)print\((?P<args_and_kwargs>.*?)\)\s*$"
    pattern_decorator = r'(\n)?@.*'

    def __init__(self, func, log_level: str = 'warning') -> None:
        self.log_level = log_level

    def log(self, log_level: str) -> Callable:

        def decorator(func):

            @wraps(func)
            def wrapper(*args, **kwargs):
                source_code = inspect.getsource(func)
                pattern = re.compile(self.pattern_print, re.MULTILINE)

                def replation(match) -> str:
                    indent = match.group("indent")
                    args_and_kwargs = match.group("args_and_kwargs")

                    if self.log_levels[log_level] < self.log_levels[self.log_level]:
                        return f'{indent}print()'

                    else:
                        return f"""{indent}print("{log_level.upper()}: ", {args_and_kwargs})"""

                modified_code_dash = re.sub(
                    pattern, replation, source_code, re.MULTILINE)
                modified_code = re.sub(
                    self.pattern_decorator, '', modified_code_dash, 1)

                exec_globals = func.__globals__.copy()
                exec(modified_code, exec_globals)
                modified_func = exec_globals[func.__name__]

                return modified_func(*args, **kwargs)
            return wrapper
        return decorator
