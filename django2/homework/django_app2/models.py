from django.db import models

STATUS_CHOICES = (
    (1, "new"),
    (2, "old"),
)


class Film(models.Model):
    name = models.CharField(max_length=32),
    rate = models.IntegerField(),
    created_at = models.IntegerField(),
    is_published = models.BooleanField()
    status = models.IntegerField(choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.name} {self.status}"