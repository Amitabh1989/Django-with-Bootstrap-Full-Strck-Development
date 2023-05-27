from django.shortcuts import render
from .models import WingManConfig
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt



class WingConfigView(APIView):
    def get(self, request):
        queryset = WingManConfig.objects.all().values()
        return Response(queryset)
    
    def post(self, request):
        instance = WingManConfig.objects.create(
            raid=request.data.get('raid'),
            drivees=request.data.get('drivees'),
            init=request.data.get('init'),
            expected_res=request.data.get('expected_res')
        )

        return Response("Created")

    
    


    



    