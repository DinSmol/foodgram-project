from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    units = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# class Review(models.Model):
#     title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name="reviews")
#     author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="review_author")
#     text = models.TextField()
#     score = models.IntegerField(choices=[(x, str(x)) for x in range(1,11)], default=5,
#         validators=[MinValueValidator(1), MaxValueValidator(10)])
#     pub_date = models.DateTimeField("date published", auto_now_add=True, db_index=True)

#     class Meta:
#         ordering = ('pub_date',)

#     def __str__(self):
#         return self.title