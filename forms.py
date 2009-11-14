"""
Forms for adding and editing Snippets.

"""

from django import forms
from models import Language, Snippet

# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary.
attrs_dict = { 'class': 'required' }

class AddSnippetForm(forms.ModelForm):
    """
    Form used for adding Snippets.
    
    """
    class Meta:
        
        model = Snippet
        exclude = ['author', 'original']
    # def __init__(self, *args, **kwargs):
    #     super(AddSnippetForm, self).__init__(*args, **kwargs)
    #     self.fields['language'].choices = [('', '----------')] + [(lang.id, lang.name) for lang in Language.objects.all()]
    # 
    # title = forms.CharField(max_length=250, widget=forms.TextInput(attrs=attrs_dict))
    # description = forms.CharField(widget=forms.Textarea(attrs=attrs_dict))
    # code = forms.CharField(widget=forms.Textarea(attrs=attrs_dict))
    # tag_list = forms.CharField(max_length=250, widget=forms.TextInput(attrs=attrs_dict))
    # language = forms.ChoiceField(choices=(), widget=forms.Select(attrs=attrs_dict))


class EditSnippetForm(forms.ModelForm):
    """
    Form used for editing Snippets.
    
    This is a separate Form because on edit the language shouldn't be
    changing.
    
    """
    class Meta:
        
        model = Snippet
        exclude = ['language', 'author', 'original']
    # title = forms.CharField(max_length=250, widget=forms.TextInput(attrs=attrs_dict))
    # description = forms.CharField(widget=forms.Textarea(attrs=attrs_dict))
    # code = forms.CharField(widget=forms.Textarea(attrs=attrs_dict))
    # tag_list = forms.CharField(max_length=250, widget=forms.TextInput(attrs=attrs_dict))
