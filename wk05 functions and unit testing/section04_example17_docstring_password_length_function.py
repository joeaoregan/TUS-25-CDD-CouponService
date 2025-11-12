# Purpose: to check is a password is a valid length
# Example of: returning a boolean value from a function
def is_valid_password_length(password, min_len=8, max_len=32):
    """
    Check if a password length is within the allowed range.

    Parameters
    ----------
    password : str
        The password to check.
    min_len : int, optional
        The minimum allowed length (default is 8).
    max_len : int, optional
        The maximum allowed length (default is 32).

    Returns
    -------
    bool
        True if the password length is between min_len and max_len (inclusive), False otherwise.

    Examples
    --------
    >>> is_valid_password_length("secret")
    False
    >>> is_valid_password_length("mypassword123")
    True
    >>> is_valid_password_length("my very excellent password which is too long", 8, 16)
    False
    """
    return min_len <= len(password) <= max_len

# Example of testing with doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)




