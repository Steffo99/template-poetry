import re
from cookiecutter.utils import simple_filter


NON_ALNUM = re.compile(r"[^A-Za-z0-9]")


@simple_filter
def kebab(v):
    return NON_ALNUM.sub("-", v) if v else v


@simple_filter
def snake(v):
    return NON_ALNUM.sub("_", v) if v else v
