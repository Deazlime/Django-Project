from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Board, Task, TimeTracker
from .serializers import BoardSerializer, TaskSerializer, TimeTrackerSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"board_{serializer.instance.board.id}",
            {"type": "task_update", "task": TaskSerializer(serializer.instance).data}
        )

class TimeTrackerViewSet(viewsets.ModelViewSet):
    queryset = TimeTracker.objects.all()
    serializer_class = TimeTrackerSerializer
    permission_classes = [IsAuthenticated]

# Create your views here.
