import re
from cookiecutter.utils import simple_filter


NON_ALNUM = re.compile(r"[A-Za-z0-9]")


@simple_filter
def kebab(v):
    return re.sub(NON_ALNUM, "-", v)


@simple_filter
def snake(v):
    return re.sub(NON_ALNUM, "_", v)
