from django import forms

from catalog.models import Product, Version, Category


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CategoryForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(StyleFormMixin, forms.ModelForm):

    banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        exclude = ('owner',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for word in self.banned_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('В названии есть запрещенные слова!')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for word in self.banned_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('В описании есть запрещенные слова!')
        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
