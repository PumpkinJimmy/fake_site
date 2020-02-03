from django.db import models

# Create your models here.


class Paper(models.Model):
    uid = models.CharField(max_length=30)  # test user id
    mid = models.CharField(max_length=30)  # test model id
    cnt = models.IntegerField()  # total count count
    true_cnt = models.IntegerField()  # true positive count
    def __str__(self):
        return f"Paper from User {self.uid} for Model {self.mid}"
