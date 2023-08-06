from django.db import models


class User(models.Model):
    idname = models.fields.CharField(max_length=250, unique=True)
    display_name = models.fields.CharField(max_length=250)
    email = models.fields.CharField(max_length=250)
    phone  = models.fields.CharField(max_length=250)
    

    def __str__(self):
        return f'{self.display_name}'

class Question(models.Model):
    question = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    option5 = models.TextField()
    answer= models.IntegerField()
    explain = models.TextField()
    Favorite_Question = models.ForeignKey('FavoriteQuestion', null=True, on_delete=models.SET_NULL)
    Read_Question = models.ForeignKey('ReadQuestion', null=True, on_delete=models.SET_NULL)

class FavoriteQuestion(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

class ReadQuestion(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)


