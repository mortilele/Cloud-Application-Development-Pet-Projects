import logging
import azure.functions as func


def render_template(template_file, images):
    from jinja2 import Environment, FileSystemLoader
    mimetype = 'text/html'
    try:
        fileloader = FileSystemLoader('templates')
        env = Environment(loader=fileloader)
        template = env.get_template(template_file)
        output = template.render(images=images)
        return output, mimetype
    except Exception as e:
        logging.exception(str(e))
        return '500 Server error', mimetype


def get_images():
    try:
        from azure.storage.blob import ContainerClient
        container_sas_url = "https://imgstoralik.blob.core.windows.net/publicfiles?sp=rl&st=2021-03-03T18:46:26Z&se=2021-03-11T02:46:26Z&spr=https&sv=2020-02-10&sr=c&sig=Xay%2FKkPR2nOF7YbzrvVcL8w1Xx%2FIj5Yd6ToUGL2tjG8%3D"
        container = ContainerClient.from_container_url(container_sas_url)
        blob_list = container.list_blobs()
        images_url = []
        for blob in blob_list:
            blob = container.get_blob_client(blob.name)
            images_url.append(blob.url)
        return images_url
    except Exception as e:
        logging.exception(f'[Failed to get images from container] {str(e)}')
        return []


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    images = get_images()
    template, mimetype = render_template('index.html', images)
    return func.HttpResponse(template, mimetype=mimetype)


"""
========================================================================================================================
EXPLANATION OF IMPLEMENTED SOLUTION:
    0. In order to implement full stack single page application, I used Azure Functions, [HTTP Trigger]
    1. Created SAS url on Storage Account for "publicfiles" container
    2. Initialize container client from SAS URL via SDK
    3. Iterate over blobs, init blob client from container SAS
    4. Retrieve safe URL for each blob
    5. Render HTML template using Jinja2, sending our generate image urls
    6. Return HTTP Response of HTML mime type
========================================================================================================================
"""