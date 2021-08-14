from django.contrib import admin
from .models import News
from .models import Details
from .models import Subscribe
from .models import Testimonial
from .models import Top

admin.site.register(Details)
admin.site.register(News)
admin.site.register(Subscribe)
admin.site.register(Testimonial)
admin.site.register(Top)


