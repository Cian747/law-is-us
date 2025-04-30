from django.contrib import admin
from .models import Attorney,PracticeArea,FAQ,Testimonial,ContactMessage

admin.site.register(Attorney)
admin.site.register(PracticeArea)
admin.site.register(FAQ)
admin.site.register(Testimonial)
admin.site.register(ContactMessage)