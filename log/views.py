import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from log.tasks import log_create


class LogView(APIView):
    def post(self, request):
        data = str(json.dumps(request.data))
        log_create.delay(568439, 1, data, blockchain="eth")
        return Response({"message": "ok"})
