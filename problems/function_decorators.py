from functools import wraps
import re


t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def postprocess(chars):
    def postprocess_logic(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            base = func(*args, **kwargs)

            logic = dict.fromkeys(chars, '-')
            template = str.maketrans(logic)
            base = base.translate(template)

            base = re.sub(r"(-)\1+", r"\1", base)

            return base
        return wrapper
    return postprocess_logic


@postprocess(chars="?!:;,. ")
def format(string):
    template = str.maketrans(t)
    return string.lower().translate(template)


print(format(input()))










