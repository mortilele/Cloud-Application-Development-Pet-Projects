import uuid

from forms.pet import PetForm


class Pet:

    def __init__(self, name, category, price, description, id=None):
        self.name = name
        self.category = category
        self.price = price
        self.description = description
        if id:
            self.id = id
        else:
            self.id = str(uuid.uuid4())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'description': self.description,
            'image_url': 'https://i.pinimg.com/originals/6a/97/3a/6a973acc6f9e9fb337ba5509bb77e58e.jpg'
        }

    @classmethod
    def from_dict(cls, body):
        return Pet(name=body['name'],
                   category=body['category'],
                   price=body['price'],
                   description=body.get('description'),
                   id=body.get('id'))

    @classmethod
    def from_form(cls, form: PetForm, id=None):
        return Pet(name=form.name.data,
                   category=form.category.data,
                   price=form.price.data,
                   description=form.description.data,
                   id=id)

    def __str__(self):
        return f'{self.name} - {self.category}'
