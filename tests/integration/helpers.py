from typing import Dict


def example_auth_header() -> Dict[str, str]:
    """
    Return an auth header that passes Firebase's internal checks, e.g. correct
    issuer and audience for the testing setup. It returns a user with the UID
    'test-user-123'
    """
    return {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vZGVtby1nYXRlYXUtdGVzdCIsInN1YiI6InRlc3QtdXNlci0xMjMiLCJhdWQiOiJkZW1vLWdhdGVhdS10ZXN0IiwiZXhwIjoxMzExMjgxOTcwLCJpYXQiOjEzMTEyODA5NzAsIm5hbWUiOiJKYW5lIERvZSIsImdpdmVuX25hbWUiOiJKYW5lIiwiZmFtaWx5X25hbWUiOiJEb2UiLCJnZW5kZXIiOiJmZW1hbGUiLCJiaXJ0aGRhdGUiOiIwMDAwLTEwLTMxIiwiZW1haWwiOiJqYW5lZG9lQGV4YW1wbGUuY29tIiwicGljdHVyZSI6Imh0dHA6Ly9leGFtcGxlLmNvbS9qYW5lZG9lL21lLmpwZyJ9.TA_E5rf6J3B2XYSZ0T6goQTR9K43xE55s8QHmW2TCQU"  # noqa: E501
    }
