

#
# Check if a string is an integer
#
def is_int(string: str) -> bool:
    try:
        int(string)
        return True
    except ValueError:
        return False
