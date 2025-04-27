from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=255, help_text="URL или имя маршрута")
    active_on_url_match = models.BooleanField(default=False, help_text="Активность пункта при совпадении URL")
    
    def is_active(self, current_path):
        if self.active_on_url_match:
            return current_path.startswith(self.url)
        
        try:
            resolved_url = reverse(self.url)
            return current_path.startswith(resolved_url)
        except Exception as e:
            print(f"Error resolving {self.url}: {e}")
            return False
        
    def get_absolute_url(self):
        return self.url
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"