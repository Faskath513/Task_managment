from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def retrieve(self, request, *args, **kwargs):
        task = self.get_object()
        if task.user != request.user:
            raise PermissionDenied("You do not have permission to access this task.")
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.user != request.user:
            raise PermissionDenied("You do not have permission to update this task.")
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        if task.user != request.user:
            raise PermissionDenied("You do not have permission to delete this task.")
        return super().destroy(request, *args, **kwargs)