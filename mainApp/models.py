from django.db import models

# Create your models here.


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class About(models.Model):
    bio = models.CharField(max_length=500)

    def __str__(self):
        return 'About'


class Project(models.Model):
    headline = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    organization = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    about = models.ForeignKey(About, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline


class Skill(models.Model):
    description = models.CharField(max_length=100)
    rate = IntegerRangeField(min_value=1, max_value=5)
    about = models.ForeignKey(About, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Job(models.Model):
    title = models.CharField(max_length=50, default='Dummy Project')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    summary = models.CharField(max_length=200)
    github = models.CharField(max_length=50, null=True, blank=True)
    link = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

    def summary_text(self):
        return self.summary.split('image_static')[0]

    def summary_img(self):
        if(len(self.summary.split('image_static')) > 1):
            return self.summary.split('image_static')[1].strip()
        else:
            return None