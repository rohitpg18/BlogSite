

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# from django.utils import timezone



class Blog(models.Model):
    title  = models.CharField(max_length = 120, default=None)
    body   = models.TextField(max_length = 3000, default=None)
    author = models.ForeignKey(User , on_delete = models.CASCADE)
    date_posted = models.DateTimeField(auto_now=True, null=True)
   
    
    def __str__(self):
        return self.title[:50]
    
    def get_absolute_url(self):
        return reverse('blog_detail', args = [str(self.id)])

# i created this get_absolute_url so that after updation the user can get redirected to the
#  detail page, not on the list page. 
# Reason for creating this function is that, the blog_detail page needs blog id and we cannot
# mention that inside submit button class neither with the class of views.py beacause doing so
# leads to errors.  
