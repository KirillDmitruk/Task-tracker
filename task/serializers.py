from rest_framework import serializers

from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for model Task."""

    class Meta:
        model = Task
        fields = (
            'name', 'executor', 'deadline', 'status', 'description', 'created_at', 'updated_at', 'parent_task',
            'is_taken')
