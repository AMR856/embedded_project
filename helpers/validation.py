import re
from email_validator import validate_email, EmailNotValidError
from typing import Tuple
import requests
import os

def email_validator_regex(email: str) -> bool:
    """
    Validates an email address using a regular expression.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid according to the regex, False otherwise.

    The regex pattern checks for the following:
    - The email address must not start with a dot (.)
    - The email address must not contain consecutive dots (..)
    - The local part (before @) can contain alphanumeric characters and certain special characters
    - The domain part (after @) must be alphanumeric and followed by a valid TLD (2 or more letters)
    """
    pattern = (r"^(?!\.)(?!.*\.\.)[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"
               r"@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$")
    return re.fullmatch(pattern, email) is not None

def validate_email_address_with_package(email: str) -> Tuple[bool, str]:
    """
    Validates an email address using the `email_validator` package.

    Args:
        email (str): The email address to validate.

    Returns:
        Tuple[bool, str]:
            - A boolean indicating whether the email is valid.
            - If valid, the normalized email address is returned.
            If invalid, an error message describing why the email is invalid is returned.

    Uses the `email_validator` package to check:
    - Syntax correctness.
    - Domain validity (e.g., if the domain exists).
    """
    try:
        valid = validate_email(email)
        return True, valid.email
    except EmailNotValidError as e:
        return False, str(e)

def check_username(username: str) -> bool:
    """
    Validates a username using regex.

    Args:
        username (str): The username.

    Returns:
        bool:
            - A boolean indicating whether the user is valid.

    The regex pattern checks for the following:
    - The username contains only alphanumeric chraceters and underscores
    - The length of the username is from 7 to 29 chars
    """
    username_pattern: str = r"^[A-Za-z][A-Za-z0-9_]{7,29}$"
    return re.fullmatch(username_pattern, username) is not None

def validate_email_using_mailboxapi(email: str) -> bool:
    """
    Validates the given email address using an external Mailbox API.

    This function sends a GET request to an API endpoint that performs various checks on the email address:
    - Validates the format of the email.
    - Checks if the email domain has valid MX (Mail Exchange) records.
    - Verifies if SMTP is available for the email domain.
    - Ensures the email address is not disposable (temporary).

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: `True` if the email is valid (format is correct, MX records exist, SMTP is available, and it's not disposable),
            `False` otherwise.
    """
    url = f"{os.getenv('API_URL')}?access_key={os.getenv('ACCESS_KEY')}&email={email}&smtp=1&format=1"
    response = requests.get(url)
    if response.status_code == 200:
        response_result = response.json()
        return response_result.get('format_valid') and \
        response_result.get('mx_found') and \
        response_result.get('smtp_check') and \
        not response_result.get('disposable')
    else:
        print('Error happened while validating the email')
        return False
