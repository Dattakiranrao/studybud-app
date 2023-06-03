from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from rest_framework.schemas.coreapi import serializers
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoute(requests):
    routes = [
            'GET /api',
            'GET /api/rooms',
            'GET /api/room/:id',
            ]

    return Response(routes)

@api_view(['GET'])
def getRooms(requests):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(requests, primaryKey):
    rooms = Room.objects.get(id=primaryKey)
    serializer = RoomSerializer(rooms, many=False)
    return Response(serializer.data)
