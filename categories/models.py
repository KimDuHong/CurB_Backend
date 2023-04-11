from django.db import models
from common.models import CommonModel


class Category(CommonModel):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
    )
    unique_together = ("name", "group")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "categories"

    # def add_default_data():
    #     Category.objects.get_or_create(name='전체글')

    def save(self):
        if not self.name:
            self.name = "전체글"
        super().save()
