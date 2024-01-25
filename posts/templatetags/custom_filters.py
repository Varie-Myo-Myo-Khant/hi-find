from django import template
from django.utils import timezone  # Import the timezone module
from datetime import timedelta

register = template.Library()

@register.filter
def custom_naturaltime(timestamp):
    now = timezone.now()
    delta = now - timestamp

    if delta < timedelta(minutes=1):
        return f'{delta.seconds}s ago'
    elif delta < timedelta(hours=1):
        return f'{delta.seconds // 60}m ago'
    elif delta < timedelta(days=1):
        return f'{delta.seconds // 3600}hr ago'
    else:
        return timestamp.strftime('%Y-%m-%d %H:%M:%S')
