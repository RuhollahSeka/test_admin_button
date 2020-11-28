from django.contrib import admin
from django.utils.safestring import mark_safe

from buttons.actions import my_action
from buttons.models import Button


@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'text', 'req_button')
    actions = (my_action,)

    def req_button(self, button: Button):
        button_html = '''
        <button target="_blank" onclick="doStuff({number})">{text}</button>
        '''.format(
            text=button.text,
            number=button.number,
        )

        return mark_safe(button_html)

    req_button.short_description = 'دکمه فلان'

    class Media:
        js = (
            'buttons/button.js',
        )
