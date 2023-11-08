def set_filter(value):
    if isinstance(value, list):
        # For lists, use a list comprehension to keep the first occurrence of each dictionary
        return [dict(t) for t in {tuple(d.items()) for d in value}]
    elif isinstance(value, dict):
        # For dictionaries, convert it to a list of dictionaries
        return [value]
    else:
        return value

# You can also define the `unique` filter for clarity
def unique_filter(value):
    return set_filter(value)
