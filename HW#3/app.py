from flask import Flask, render_template, redirect, request

from db.models import Pet
from forms.pet import PetForm
from db import client as cosmos_client, blob_storage
import config


app = Flask(__name__)
app.config['SECRET_KEY'] = config.APP_SECRET_KEY


@app.route('/pets', methods=['GET'])
def get_pets():
    pets = cosmos_client.get_pets()
    return render_template('pets.html', pets=pets)


@app.route('/pets/add', methods=['GET', 'POST'])
def create_pet():
    form = PetForm()
    if form.validate_on_submit():
        pet = Pet.from_form(form)
        image_url = blob_storage.upload_image(request.files['image'])
        pet.set_image_url(image_url)
        cosmos_client.create_pet(pet.to_dict())
        return redirect('/pets')
    return render_template('pet_form.html', form=form, method='post')


@app.route('/pets/<category>/<uuid:pet_id>', methods=['GET', 'POST'])
def pet_get_or_update(category, pet_id):
    form = PetForm()
    pet_id = str(pet_id)
    pet_json = cosmos_client.get_pet(pet_id, category)
    pet = Pet.from_dict(pet_json)
    if request.method == 'GET':
        form.name.data = pet.name
        form.category.data = pet.category
        form.price.data = pet.price
        form.description.data = pet.description
    if form.validate_on_submit():
        new_pet = Pet.from_form(form, id=pet_id)
        image_content = request.files.get('image')
        if image_content:
            image_url = blob_storage.upload_image(image_content)
            new_pet.set_image_url(image_url)
        else:
            new_pet.set_image_url(pet.get_image_url())
        cosmos_client.edit_pet(new_pet.id, new_pet.to_dict())
        return redirect('/pets')
    return render_template('pet_form.html', form=form, method='put')


@app.route('/pets/<category>/<uuid:pet_id>/delete', methods=['GET'])
def remove_pet(category, pet_id):
    cosmos_client.delete_pet(str(pet_id), category)
    return redirect('/pets')
