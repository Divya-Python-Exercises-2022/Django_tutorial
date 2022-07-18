from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50, null=True)
    pub_date = models.DateField()

    class Meta:
        ordering = ['pub_date']

#     def latest_books(request):
#         book_list = Book.objects.order_by('-pub_date')[:10]
#
#     return render(request, 'latest_books.html', {'book_list': book_list})
#
# urlpatterns = patterns('',
# (r'^latest/$', views.latest_books),
# )