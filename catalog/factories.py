import factory

from .models import Category


class ItemFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('company', locale='pt_BR')
    address = factory.Faker('address', locale='pt_BR')
    phone = factory.Faker('phone_number', locale='pt_BR')
    description = factory.Faker('text', locale='pt_BR')
    website = factory.Faker('url', locale='pt_BR')
    email = factory.Faker('email', locale='pt_BR')
    published = True


    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        category = Category.objects.filter().order_by('?')[0]
        self.categories.add(category)

    class Meta:
        model = 'catalog.Item'

