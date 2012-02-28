
def _to_str(name):
    """Add _ if given string is a digit."""
    if name.isdigit():
        name = '_%s' % name

    return name
