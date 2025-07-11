from django.contrib import admin
from .models import Voter, Candidate, Votes, Position

admin.site.register(Voter)
admin.site.register(Candidate)
admin.site.register(Votes)
admin.site.register(Position)
# Register your models here.
