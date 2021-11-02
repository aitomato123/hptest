from django.db import models
from django.db.models import CASCADE


class UserInfo(models.Model):
    userid = models.CharField(max_length=64, unique=True)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)


class ProjInfo(models.Model):
    project_id = models.CharField(max_length=20, unique=True)
    date = models.CharField(max_length=20)
    client = models.CharField(max_length=100)
    applicant = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    contacts = models.CharField(max_length=30)
    counterman = models.CharField(max_length=30)
    customer = models.CharField(max_length=30)
    plan_date_sample =models.CharField(max_length=20)
    report_agree_date = models.CharField(max_length=20)
    number_of_reports = models.CharField(max_length=5)
    test_style = models.CharField(max_length=5)
    report_type = models.CharField(max_length=5)
    quality_control_report = models.CharField(max_length=2)
    split_or_not = models.CharField(max_length=2)
    subpackage_or_not = models.CharField(max_length=2)
    mission_link = models.CharField(max_length=100)
    voluntary_standards = models.CharField(max_length=255)
    collector = models.CharField(max_length=25)
    sample_date = models.CharField(max_length=20)
    progress = models.CharField(max_length=5)
    status_bar = models.CharField(max_length=2)
    def __str__(self):
        return self.project_id


class SampleType(models.Model):
    sample_type = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.sample_type


# class MissionInfo(models.Model):
#     project_id = models.ForeignKey(to='ProjInfo', on_delete=CASCADE)
#     sample_type = models.ForeignKey(to='SampleType', on_delete=CASCADE)
#     sampling_position = models.CharField(max_length=20)
#     number_of_position = models.IntegerField()
#     sampling_times = models.IntegerField()
#     sampling_of_days = models.IntegerField()
#     test_items = models.CharField(max_length=255)
#     status_bar = models.CharField(max_length=2)


class Storage(models.Model):
    storage = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.storage


class SampleHandover(models.Model):
   sh_pid = models.ForeignKey(to='ProjInfo', on_delete=CASCADE)
   sh_spt = models.ForeignKey(to='SampleType', on_delete=CASCADE)
   sample_ids = models.CharField(max_length=105)
   analysis_items = models.CharField(max_length=255)
   sample_number = models.CharField(max_length=5)
   sh_sto = models.ForeignKey(to='Storage', on_delete=CASCADE)
   char_person = models.CharField(max_length=15)
   status_bar = models.CharField(max_length=2)
   def __str__(self):
       return self.sample_ids


# class SampleInfo(models.Model):
#     project_id = models.ForeignKey(to='ProjInfo', on_delete=CASCADE)
#     sample_type = models.ForeignKey(to='SampleType', on_delete=CASCADE)
#     sample_id = models.CharField(max_length=20, unique=True)
#     sampling_position = models.CharField(max_length=20)
#     coordinate = models.CharField(max_length=30)
#     analysis_items = models.CharField(max_length=255)
#     sampling_date = models.DateField()
#     sampling_of_days = models.IntegerField()
#     sample_traits = models.CharField(max_length=50)
#     status_bar = models.CharField(max_length=2)
#     def __str__(self):
#         return self.sample_id
#
#
class JudgeChoose(models.Model):
    judge = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.judge


class UnitChoose(models.Model):
    unit = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.unit


# class ItemInfo(models.Model):
#     project_id = models.ForeignKey(to='ProjInfo', on_delete=CASCADE)
#     sample_id = models.ForeignKey(to='SampleInfo', on_delete=CASCADE)
#     item = models.CharField(max_length=20)
#     test_method = models.CharField(max_length=100)
#     result = models.CharField(max_length=20)
#     unit = models.ForeignKey(to='UnitChoose', on_delete=CASCADE)
#     limit_of_detection = models.CharField(max_length=20)
#     standard_limit = models.CharField(max_length=20)
#     standard_limit_unit = models.CharField(max_length=20)
#     equipment = models.CharField(max_length=20)
#     equipment_id = models.CharField(max_length=20)
#     analyst = models.CharField(max_length=20)
#     analysis_date = models.CharField(max_length=20)
#     tips = models.CharField(max_length=20)
#     judge = models.ForeignKey(to='JudgeChoose', on_delete=CASCADE)
#     status_bar = models.CharField(max_length=2)
