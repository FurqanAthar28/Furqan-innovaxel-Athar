from django.db import models
import string
import random

# Helper function to generate a random short code
def generate_shortcode(length=6):
    """Generates a random alphanumeric short code of specified length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


class ShortURL(models.Model):
    """
    Model to store original URLs with a unique short code and access tracking.
    """

    url = models.URLField()  # Original long URL
    short_code = models.CharField(max_length=10, unique=True, blank=True, null=True)  # Auto-generated if blank
    created_at = models.DateTimeField(auto_now_add=True)  # Set only once when record is created
    updated_at = models.DateTimeField(auto_now=True)      # Updated every time the record is saved
    access_count = models.PositiveIntegerField(default=0)  # Number of times the short URL was accessed

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to auto-generate a unique short_code if not provided.
        """
        if not self.short_code:
            self.short_code = self.generate_unique_code()
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        """
        Keeps generating random short codes until a unique one is found.
        """
        while True:
            code = generate_shortcode()
            if not ShortURL.objects.filter(short_code=code).exists():
                return code

    def __str__(self):
        return f"{self.short_code} → {self.url}"
