from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .utils.exception_handlers import handle_exception
from . import services


@api_view(["GET", "POST"])
def appointment(request):
    try:
        if request.method == "GET":
            todos = services.get_all_todos()
            return Response(todos)
        elif request.method == "POST":
            todo = services.add_todo(request.data)
            return Response(todo, status=status.HTTP_201_CREATED)

    except Exception as e:
        error_object = handle_exception(e)
        return Response({"Error": error_object["Error"]}, status=error_object["Status"])
