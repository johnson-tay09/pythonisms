from functools import wraps


class Pythonisms:
    def __init__(self, values):
        self.values = values

    def quote_generator_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            orig_val = func(*args, **kwargs)
            return f'"{orig_val}" - Taylor'

        return wrapper

    def return_text(txt):
        return txt

    @quote_generator_decorator
    def taylor_quote(txt):
        return txt

    def add_emphasis(txt):
        return f"I LOVE {txt} MORE THAN ANYTHING IN THE WORLD!"

    def fill_spaces(txt):
        filled_string = []
        filled_text = txt.replace(" ", "X")
        filled_string.append(filled_text)
        return filled_string


print(Pythonisms.fill_spaces("test     if     spaces   filled."))
print(Pythonisms.return_text("Test return text!"))
print(Pythonisms.taylor_quote("You can call me Lazer!"))
print(Pythonisms.add_emphasis("memorizing data structures and algorithms"))
