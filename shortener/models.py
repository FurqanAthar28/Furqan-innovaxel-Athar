from django.db import models
import string
import random

# Helper function to generate a random short code
def generate_shortcode(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

class ShortURL(models.Model):
    url = models.URLField()  # Original long URL
    short_code = models.CharField(max_length=10, unique=True, blank=True,null=True)  # Auto-generated
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)  # Set only on creation
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)  # Updated on every save
    access_count = models.PositiveIntegerField(default=0,blank=True,null=True)  # Number of times accessed

    def save(self, *args, **kwargs):
        # If no short_code is provided, generate a unique one automatically
        if not self.short_code:
            self.short_code = self.generate_unique_code()
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        while True:
            code = generate_shortcode()
            if not ShortURL.objects.filter(short_code=code).exists():
                return code

    def __str__(self):
        return f"{self.short_code} → {self.url}"
