from django.db import models
from common.models import CommonModel


class Feedlike(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    feed = models.ForeignKey(
        "feeds.Feed",
        on_delete=models.CASCADE,
    )


class Commentlike(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    comment = models.ForeignKey(
        "comments.Comment",
        on_delete=models.CASCADE,
    )
