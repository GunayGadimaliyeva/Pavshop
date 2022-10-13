from modeltranslation.translator import translator, TranslationOptions
from .models import blog

class BlogsTranslationOptions(TranslationOptions):
    fields = ('blog_title', 'desc')

translator.register(blog, BlogsTranslationOptions)

