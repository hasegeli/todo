from django.db import models

class Priority(models.Model):
    name = models.CharField(max_length=200, unique=True)
    sortOrder = models.SmallIntegerField(unique=True)

    class Meta:
        ordering = 'sortOrder',
        verbose_name_plural = 'Priorities'

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=1000)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    dueTo = models.DateTimeField(null=True, blank=True)
    priority = models.ForeignKey(Priority, null=True)

    class Meta:
        ordering = 'createdAt',
        verbose_name_plural = 'Todo List'

    def __str__(self):
        return self.title

