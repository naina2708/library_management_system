from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

CATEGORY_CHOICES = [
    ('SC', 'Science'),
    ('EC', 'Economics'),
    ('FC', 'Fiction'),
    ('CH', 'Children'),
    ('PD', 'Personal Development'),
]

TYPE_CHOICES = [
    ('B', 'Book'),
    ('M', 'Movie'),
]

MEMBERSHIP_CHOICES = [
    (6, '6 Months'),
    (12, '1 Year'),
    (24, '2 Years'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_months = models.IntegerField(choices=MEMBERSHIP_CHOICES, default=6)
    membership_start = models.DateField(auto_now_add=True)

    def membership_end(self):
        return self.membership_start + timedelta(days=30*self.membership_months)


class Item(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    item_type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    quantity = models.IntegerField()
    code = models.CharField(max_length=20, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.code:
            count = Item.objects.filter(category=self.category).count() + 1
            self.code = f"{self.category}{self.item_type}{str(count).zfill(6)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    issue_date = models.DateField(default=datetime.now)
    due_date = models.DateField(blank=True)
    return_date = models.DateField(null=True, blank=True)

    fine_paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = self.issue_date + timedelta(days=15)
        super().save(*args, **kwargs)

    def fine(self):
        if self.return_date and self.return_date > self.due_date:
            days = (self.return_date - self.due_date).days
            return days * 10
        return 0