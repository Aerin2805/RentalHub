from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border bg-gray-900 text-white'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('area', 'name', 'description', 'price', 'image',)
        widgets = {
            'area': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': f'{INPUT_CLASSES} resize-none',  # Disable textarea resize
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': f'{INPUT_CLASSES} resize-none',  # Disable textarea resize
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
