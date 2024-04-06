import random
from django.core.management.base import BaseCommand
from post.models import Comment, CommentImage  # Replace 'your_app' with the name of your Django app
from django.utils.text import slugify

image_urls = [
   "https://www.javatpoint.com/fullformpages/images/URL.jpg",
    "https://d27jswm5an3efw.cloudfront.net/app/uploads/2019/08/image-url-3.jpg",
    "https://www.gemoo-resource.com/tools/img/image_urlgenerator_step1@2x.png",
    # Add more image URLs as needed
]

class Command(BaseCommand):
    help = 'Populates the PostImage model with random images for each post'

    def handle(self, *args, **options):
        CommentImage.objects.all().delete()  # Clear existing post images
        posts = Comment.objects.all()
        for post in posts:
            # Decide how many images to assign to this post (between 0 and 3)
            num_images = random.randint(0, 3)
            for _ in range(num_images):
                # Choose a random image URL
                image_url = random.choice(image_urls)
                # Create a PostImage instance and link it to the current post
                CommentImage.objects.create(comment=post, comment_image=image_url)
                self.stdout.write(self.style.SUCCESS(f'Successfully added image to post "{post.post.name}"'))
        self.stdout.write(self.style.SUCCESS('Successfully populated PostImage model with random images'))
