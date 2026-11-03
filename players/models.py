from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# These are the positions a player can choose from.
POSITION_CHOICES = [
("GK", "Goalkeeper"),
("CB", "Center Back"),
("RB", "Right Back"),
("LB", "Left Back"),
("DM", "Defensive Midfielder"),
("CM", "Central Midfielder"),
("AM", "Attacking Midfielder"),
("RW", "Right Winger"),
("LW", "Left Winger"),
("ST", "Striker"),
]


# Players can select the region in Ghana where they are based.
REGION_CHOICES = [
("AH", "Ahafo"),
("AS", "Ashanti"),
("BO", "Bono"),
("BE", "Bono East"),
("CE", "Central"),
("EA", "Eastern"),
("GA", "Greater Accra"),
("NE", "North East"),
("NO", "Northern"),
("OT", "Oti"),
("SA", "Savannah"),
("UE", "Upper East"),
("UW", "Upper West"),
("VO", "Volta"),
("WE", "Western"),
("WN", "Western North"),
]
# A player can be right-footed, left-footed, or comfortable with both feet.
FOOT_CHOICES = [
("R", "Right"),
("L", "Left"),
("B", "Both"),
]


def validate_youtube_link(url):
    """
    Make sure players only submit YouTube links
    when uploading their football highlights.
    """
    if not (
        url.startswith("https://www.youtube.com/")
        or url.startswith("https://youtu.be/")
    ):
        raise ValidationError("Please enter a valid YouTube link for your highlights.")


class PlayerProfile(models.Model):
    """
    Stores the basic information about a football player,including their personal details, playing position,physical attributes, and football statistics.
    """

    # Each player profile belongs to one registered user.
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    # Basic player information
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    # Football information
    position = models.CharField(
    max_length=2,
    choices=POSITION_CHOICES
    )

    # Where the player is based
    region = models.CharField(
    max_length=2,
    choices=REGION_CHOICES
    )

    town = models.CharField(
    max_length=100,
    blank=True
    )

    # The team the player currently plays for, if any
    current_team = models.CharField(
    max_length=100,
    blank=True
    ) 

    preferred_foot = models.CharField(
    max_length=1,
    choices=FOOT_CHOICES
    )

    # Physical details are optional, but values must be realistic.
    height_cm = models.PositiveIntegerField(
    null=True,
    blank=True,
    validators=[
    MinValueValidator(120),
    MaxValueValidator(220)
    ]
    )

    weight_kg = models.PositiveIntegerField(
    null=True,
    blank=True,
    validators=[
    MinValueValidator(30),
    MaxValueValidator(130)
    ]
    )

    # Basic football performance statistics
    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    matches_played = models.PositiveIntegerField(default=0)

    # Players can share a YouTube video of their football highlights.
    highlight_link = models.URLField(
    blank=True,
    validators=[validate_youtube_link]
    )

    # Used to record whether a parent or guardian has approved the profile.
    guardian_approved = models.BooleanField(default=False)

    # Automatically records when the player's profile was created.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    # Show the player's name when viewing profiles in Django admin.
        return self.full_name