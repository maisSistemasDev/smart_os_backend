from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Groups
from .serializers import GroupsSerializer
from rest_framework.permissions import IsAuthenticated

class GroupView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        groups = Groups.objects.all()
        serializer = GroupsSerializer(groups, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Groups(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        data = request.data
        name = data.get('name')
        group_id = data.get('group_id')
        description = data.get('description')
        
        if(group_id):
            group = Groups.objects.filter(id=group_id).first()
            if(name):
                group.name = name
            if(description):
                group.description = description
            return Response({'message':'ok'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error':'Group not found'}, status=status.HTTP_400_BAD_REQUEST)
    
    


