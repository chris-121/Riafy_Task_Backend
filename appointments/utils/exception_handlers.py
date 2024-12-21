from rest_framework import status
from rest_framework.exceptions import NotFound, ValidationError


def handle_exception(e):
    """
    Handles known exceptions and returns an appropriate response object.
    """
    if isinstance(e, NotFound):
        return {"Error": str(e), "Status": status.HTTP_404_NOT_FOUND}
    elif isinstance(e, ValidationError):
        return {"Error": str(e), "Status": status.HTTP_400_BAD_REQUEST}
    else:
        return {"Error": str(e), "Status": status.HTTP_500_INTERNAL_SERVER_ERROR}
