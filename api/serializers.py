from rest_framework import serializers
from .models import Board, Task, TimeTracker

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'title', 'description', 'is_public', 'created_by', 'members']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'deadline', 'progress', 'board', 'assigned_to']

class TimeTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTracker
        fields = ['id', 'task', 'user', 'start_time', 'end_time']