from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from . import services
from .utils.exception_handlers import handle_exception

# from . import services


@api_view(["GET", "POST"])
def appointment(request):
    try:
        if request.method == "GET":
            date = request.query_params.get("date", None)
            slots = services.get_all_available_slots(date)
            return Response(slots, status=status.HTTP_200_OK)
        elif request.method == "POST":
            appointment = request.data
            appointment = services.create_appointment(appointment)
            return Response(appointment, status=status.HTTP_201_CREATED)

    except Exception as e:
        error_object = handle_exception(e)
        return Response({"Error": error_object["Error"]}, status=error_object["Status"])
