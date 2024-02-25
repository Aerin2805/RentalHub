from django import forms 

from .models import Item


INTPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm) :
    class Meta:
        model = Item
        fields = ('category','name','description','price','image',)
        widgets = {
        'category' : forms.Select(attrs={
            'class' : INTPUT_CLASSES
        }),
        'name' : forms.TextInput(attrs={
            'class' : INTPUT_CLASSES
        }),
        'price' : forms.TextInput(attrs={
            'class' : INTPUT_CLASSES
        }),
        'description' : forms.Textarea(attrs={
            'class' : INTPUT_CLASSES
        }),
        'image' : forms.FileInput(attrs={
            'class' : INTPUT_CLASSES
        })
    }
        
class EditItemForm(forms.ModelForm) :
    class Meta:
        model = Item
        fields = ('name','description','price','image','is_sold')
        widgets = {
        'name' : forms.TextInput(attrs={
            'class' : INTPUT_CLASSES
        }),
        'price' : forms.TextInput(attrs={
            'class' : INTPUT_CLASSES
        }),
        'description' : forms.Textarea(attrs={
            'class' : INTPUT_CLASSES
        }),
        'image' : forms.FileInput(attrs={
            'class' : INTPUT_CLASSES
        })
    }