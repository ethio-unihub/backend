import random
from django.core.management.base import BaseCommand
from file.models import UserFile
from user.models import Profile
from post.models import Tag  # Import the necessary models from your app

class Command(BaseCommand):
    help = 'Populates the UserFile model with tags'

    def handle(self, *args, **options):
        UserFile.objects.all().delete()  # Clear existing user files
        files = [
        {"name": "Worksheet of Algebraic Equations for Grade 10 Students", "file": "files/document1.pdf"},
        {"name": "Detailed Notes on World History: Ancient Civilizations and Cultures", "file": "files/document2.pdf"},
        {"name": "Presentation on Quantum Physics: Theoretical Concepts and Applications", "file": "files/presentation1.pptx"},
        {"name": "Study Guide for Advanced Mathematics: Differential Equations and Calculus", "file": "files/document3.pdf"},
        {"name": "Comprehensive Overview of European Renaissance Art and Architecture", "file": "files/document4.pdf"},
        {"name": "Research Paper on Environmental Sustainability and Renewable Energy Sources", "file": "files/document5.pdf"},
        {"name": "Tutorial Series on Machine Learning Algorithms and Applications", "file": "files/document6.pdf"},
        {"name": "Thesis Proposal: Exploring the Impact of Social Media on Mental Health", "file": "files/document7.pdf"},
        {"name": "Educational Video Series on Organic Chemistry: Chemical Reactions and Mechanisms", "file": "files/video1.mp4"},
        {"name": "Presentation on Modern Economic Theories: Macroeconomic Analysis and Policy Implications", "file": "files/presentation2.pptx"},
        # Add more files as needed
    ]

        tags = Tag.objects.all()

        # Generate random school module names as author names
        module_names = [
            "Mathematics",
            "Science",
            "History",
            "English",
            "Computer Science",
            "Physics",
            "Biology",
            "Chemistry",
            # Add more module names as needed
        ]

        for user in Profile.objects.all():
            # Randomly decide the number of files for each user (up to 10)
            num_files = random.randint(0, 1)
            for _ in range(num_files):
                file_data = random.choice(files)
                file_instance = UserFile.objects.create(name=file_data['name'], file=file_data['file'], author=user)

        
                # Decide how many tags to assign to this file (up to 5)
                num_tags = random.randint(0, 5)
                tags_to_assign = random.sample(list(tags), min(num_tags, len(tags)))
                file_instance.tag.add(*tags_to_assign)

                # Assign the file to the current user
                file_instance.save()
                user.my_files.add(file_instance)

                self.stdout.write(self.style.SUCCESS(f'Successfully created UserFile"'))

        self.stdout.write(self.style.SUCCESS('Successfully populated UserFile model with tags'))
