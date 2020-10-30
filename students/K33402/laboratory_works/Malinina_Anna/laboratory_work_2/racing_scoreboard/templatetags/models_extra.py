from django import template
register = template.Library()


@register.filter(name='has_registered')
def has_benefit(user, race_id):
    return user.racer.raceracer_set.filter(race_id=race_id).count() > 0
