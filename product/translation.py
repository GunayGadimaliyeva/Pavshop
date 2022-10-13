from unicodedata import category
from modeltranslation.translator import translator, TranslationOptions
from .models import productCategory

class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ["category_name"]

translator.register(productCategory, ProductCategoryTranslationOptions)