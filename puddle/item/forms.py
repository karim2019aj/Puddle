from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta: 
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', )
        widgets = {
            'name' : forms.TextInput(attrs={
                'placeholder' : 'Item name',
                'class' : 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none'
            }),
            'category' : forms.Select(attrs={
                'class' : 'mt-1 block w-full rounded-md border border-gray-300 bg-white py-2 px-3 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm'
            }),
            'description' : forms.Textarea(attrs={
                'class' : 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none'
            }),
            'price' : forms.NumberInput(attrs={
                'class' : 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none'
            }),
            'image' : forms.FileInput(attrs={
                'name' : 'image',
                'type': 'file',
            })
            
        }    


class EditItemForm(forms.ModelForm):
    class Meta: 
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold' )
        widgets = {
            'name' : forms.TextInput(attrs={
                'placeholder' : 'Item name',
                'class' : 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none'
            }),
            'description' : forms.Textarea(attrs={
                'class' : 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none'
            }),
            'price' : forms.NumberInput(attrs={
                'class' : 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none'
            }),
            'image' : forms.FileInput(attrs={
                'name' : 'image',
                'type': 'file',
            })
            
        }  
