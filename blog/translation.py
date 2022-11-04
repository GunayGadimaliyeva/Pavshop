from modeltranslation.translator import translator, TranslationOptions
from .models import Blog

class BlogsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_desc')

translator.register(Blog, BlogsTranslationOptions)

