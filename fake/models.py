from django.db import models

# Create your models here.


class Paper(models.Model):
    uid = models.CharField(max_length=30)  # test user id
    mid = models.CharField(max_length=30)  # test model id
    true_cnt = models.IntegerField()  # true positive count
    false_cnt = models.IntergerField()  # false positive count
