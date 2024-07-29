from django import forms
from .models import MenuItem


class MenuItemForm(forms.ModelForm):

    class Meta:
        model = MenuItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs:

            if kwargs['instance'] is not None:
                menu_id = kwargs['instance'].menu_id
            else:
                menu_id = None

            if menu_id:
                self.fields['parent'].queryset = MenuItem.objects.filter(menu_id=menu_id)
            else:
                self.fields['parent'].queryset = MenuItem.objects.none()
