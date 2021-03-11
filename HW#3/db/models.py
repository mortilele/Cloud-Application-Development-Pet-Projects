import uuid

from forms.pet import PetForm


class Pet:
    DEFAULT_IMAGE_URL = 'https://i.pinimg.com/originals/6a/97/3a/6a973acc6f9e9fb337ba5509bb77e58e.jpg'

    def __init__(self, name, category, price, description, id=None):
        self.name = name
        self.category = category
        self.price = price
        self.description = description
        if id:
            self.id = id
        else:
            self.id = str(uuid.uuid4())

        self._image_url = self.DEFAULT_IMAGE_URL

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'description': self.description,
            'image_url': self._image_url
        }

    @classmethod
    def from_dict(cls, body):
        new_pet = Pet(name=body['name'],
                      category=body['category'],
                      price=body['price'],
                      description=body.get('description'),
                      id=body.get('id'))
        new_pet.set_image_url(body.get('image_url'))
        return new_pet

    @classmethod
    def from_form(cls, form: PetForm, id=None):
        return Pet(name=form.name.data,
                   category=form.category.data,
                   price=form.price.data,
                   description=form.description.data,
                   id=id)

    def __str__(self):
        return f'{self.name} - {self.category}'

    def get_image_url(self):
        return self._image_url

    def set_image_url(self, image_url):
        self._image_url = image_url
