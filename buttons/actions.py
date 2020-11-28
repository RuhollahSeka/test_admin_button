from django.contrib import messages


def do_stuff(number):
    print(number)


def my_action(modeladmin, request, queryset):
    if queryset.count() > 5:
        messages.error(request, 'You can not choose more than 5 items.')
    for element in queryset:
        do_stuff(element.number)


my_action.short_description = 'فلان کار'
