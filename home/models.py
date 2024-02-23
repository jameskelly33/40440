from django.db import models

# Create your models here.
class Goal(models.Model):
    
    music = 'music'
    food = 'hamburger'
    drink = 'martini-glass-citrus'
    coding = 'computer'
    health = 'heart-pulse'
    other = 'otter'
    languages = 'language'
    travel='location-dot'
    forty='list-ol'
    admin='briefcase'
    arts='palette'
    
    categories=[
        (music,'Music'),
        (food,'Food'),
        (drink,'Drink'),
        (coding,'Coding'),
        (health,'Health and Fitness'),
        (other,'Other'),
        (languages,'Languages'),
        (travel,'Travel'),
        (forty,'Forty Day Challenges'),
        (admin,'Admin'),
        (arts,'Creativity'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    categories = models.CharField(max_length=50, choices=categories, default='Other')
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title}"

class Objective(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.goal.title} - Objective: {self.description[:20]}..."