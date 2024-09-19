from django.db import models


class BaseTimeStampedModel(models.Model):
    """
    BaseTimeStampedModel to enforce all models to contain `create_time`, `update_time`
    and also to show respect to DRY principle.
    this model could also contain some sort of uuid field in order to hide db ids,
    but here this is not the case :)
    """
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
