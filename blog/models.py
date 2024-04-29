from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

from wagtail.search import index

class BlogIndexPage(Page):
  intro = RichTextField(blank=True)
  def get_context(self, request):
    context = super().get_context(request)
    blogpages = self.get_children().live().order_by('-first_published_at')
    context['blogpages'] = blogpages
    return context

  content_panels = Page.content_panels + [
    FieldPanel('intro')
  ]

class BlogPage(Page):
  date = models.DateField("Post date")
  intro = models.CharField(max_length=250)
  body = RichTextField(blank=True)

  def main_image(self):
    gallery_item = self.gallery_images.first()
    if gallery_item:
      return gallery_item.image
    else:
      return None

  search_fields = Page.search_fields + [
    index.SearchField('intro'),
    index.SearchField('body'),
  ]

  content_panels = Page.content_panels + [
    FieldPanel('date'),
    FieldPanel('intro'),
    FieldPanel('body'),
    InlinePanel('gallery_images', label="Galley images"),
  ]

class BlogPageGalleyImage(Orderable):
  page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
  image = models.ForeignKey(
    'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
  )
  caption = models.CharField(blank=True, max_length=250)
  panels = [
    FieldPanel('image'),
    FieldPanel('caption'),
  ]

