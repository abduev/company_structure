from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(upload_to='employee_photos/', null=True, blank=True)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    age = models.IntegerField()
    department = models.ForeignKey('department.Department', related_name='employees',
                                   on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
