from django.core.management.base import BaseCommand, CommandError
from post.models import Post
from user.models import User

class Command(BaseCommand):
    help = 'Populates the database. Deletes old entries'

    def handle(self, *args, **options):
        print("Deleting old entries...")
        Post.objects.all().delete()
        print("Populating...")
        test = User.objects.get(user_id='wltjd1014')
        for i in range(300):
            Post.objects.create(writer=test,title=str(i),content=str(i))
        print("Done.")