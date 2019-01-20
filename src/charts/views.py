from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [qs_count, 23, 22, 31, 19, 12]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)
