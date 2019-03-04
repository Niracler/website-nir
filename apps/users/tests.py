from django.test import TestCase

# Create your tests here.
from users.models import VerifyCode

print(VerifyCode.objects.filter(mobile="13427498660").order_by("-add_time"))
