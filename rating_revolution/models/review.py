from django.db import models


class Review(models.Model):
    reviewer = models.ForeignKey('Reviewer', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    rating = models.FloatField()
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_likes(self):
        return ReviewEvent.objects.filter(review=self, type=ReviewEvent.LIKE).count()

    def get_dislikes(self):
        return ReviewEvent.objects.filter(review=self, type=ReviewEvent.DISLIKE).count()


from django.db import models


class ReviewEvent(models.Model):
    LIKE = 'L'
    DISLIKE = 'D'
    OPTIONS = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    )
    type = models.CharField(max_length=1, choices=OPTIONS)
    review = models.ForeignKey('Review', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type
