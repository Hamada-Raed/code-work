import random
import string
from django.db import models
 
class Transaction(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference_number = models.CharField(max_length=12, unique=True, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
 
    def save(self, *args, **kwargs):
        if not self.reference_number:
            self.reference_number = self.generate_unique_reference()
        super().save(*args, **kwargs)
 
    def generate_unique_reference(self):
        while True:
            reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
            if not Transaction.objects.filter(reference_number=reference).exists():
                return reference