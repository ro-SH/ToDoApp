from django.db import models

# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Tasks(models.Model):
    title = models.CharField(max_length=200)
    deadline = models.DateTimeField('Time')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    is_done = models.BooleanField('Completed')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Tasks'
        ordering = ['is_done', 'deadline']
