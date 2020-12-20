from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from uuslug import uuslug
from .utils import company_logo_directory_path


class Category(MPTTModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='Родительская категория')
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuslug(self.name, instance=self)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    class MPTTMeta:
        order_insertion_by = ['name']


class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='companies',
                                 verbose_name='Категория')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    logo = models.ImageField(upload_to=company_logo_directory_path, null=True, blank=True, verbose_name='Лого')
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuslug(self.name, instance=self)
        super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
