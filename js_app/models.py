from django.db import models
# from django_mysql.models import ListCharField

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class IDCode(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    img_url = models.CharField(max_length=512, blank=True, default='')
    code = models.TextField()
    # content = ListCharField(
    #     base_field = models.CharField(max_length=8, blank=True),
    #     size=3,
    #     max_length = (3 * 12)  # 4 * 12 character nominals, plus commas
    # )
    content = models.CharField(max_length=128, blank=True, default='')
    recognition = models.TextField()


