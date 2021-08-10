from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=70)
    tagline = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name



class Courses(models.Model):
    course_pic = models.ImageField(upload_to='images/')
    date_created = models.DateField(auto_now=False, auto_now_add=False)
    duration = models.DecimalField(max_digits=3, decimal_places=2)
    course_title = models.CharField(max_length=50)
    course_content = models.CharField(max_length=70)
    course_tutor = models.ForeignKey('Team', on_delete=models.CASCADE)
    course_tutor_pic = models.ForeignKey('Team', related_name='tutor_picture', on_delete=models.CASCADE)
    course_price = models.CharField(max_length=15)

    def __str__(self):
        return self.course_title
    

class Review(models.Model):
    name = models.CharField(max_length=70)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    star = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Review_detail", kwargs={"pk": self.pk})
