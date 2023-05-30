from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

RAID_TYPES = (
    ("R0", "RAID0"),
    ("R1", "RAID1"),
    ("R5", "RAID5"),
    ("R6", "RAID6"),
    ("R10", "RAID10"),
    ("R50", "RAID50"),
    ("R60", "RAID60"),
    ("JBODs", "JBODs"),
)

STRIPE_SIZE = (
    (256, 256),
    (1024, 1024)
)

NUM_DRIVES = [(i, str(i)) for i in range(0, 240)]

class Configuration(models.Model):
    raid_type = models.CharField(max_length=6, choices=RAID_TYPES, null=False)
    stripe_size = models.IntegerField(choices=STRIPE_SIZE)
    num_drives = models.IntegerField(choices=NUM_DRIVES, validators=(MinValueValidator(1), MaxValueValidator(240)))

    def __str__(self) -> str:
        return f'Create {self.raid_type} with {self.num_drives}'