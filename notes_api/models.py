from django.db import models

class Note(models.Model):
    text = models.CharField(max_length=1024)

    # Create / Insert / Add - POST
    # Retrieve / Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE

