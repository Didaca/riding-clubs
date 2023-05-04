from django.contrib import admin

from riding_sport_clubs.web_clubs.models import Club, Trainer, HorseBreed


class TrainerInlineAdmin(admin.StackedInline):
    model = Trainer


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('club_name', 'owner',)
    inlines = (TrainerInlineAdmin,)
    ordering = ('club_name',)


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('trainer_first_name', 'trainer_last_name', 'trainer_age', 'clubs',)
    ordering = ('trainer_first_name', 'trainer_last_name', 'clubs',)


@admin.register(HorseBreed)
class HorseBreedAdmin(admin.ModelAdmin):
    list_display = ('breed',)
    ordering = ('breed',)
