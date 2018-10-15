import os
import shutil
from data.chatito.chatito_properties import partials
import properties

COMMONS_DIRECTORY ='commons/'
PARTIALS_DIRECTORY = 'partials/'
GENERATED_DIRECTORY = 'generated/'

def generate(chatito_path, output_path):
    commons_path = chatito_path + COMMONS_DIRECTORY
    partials_path = chatito_path + PARTIALS_DIRECTORY
    generated_path = chatito_path + GENERATED_DIRECTORY

    _create_generated_path(partials_path, generated_path)
    common_files = os.listdir(commons_path)
    generated_files = os.listdir(generated_path)

    for partial_file in generated_files:
        with open(generated_path + partial_file, 'a', encoding="utf-8") as output_file:
            for common_file in common_files:
                with open(commons_path + common_file, encoding="utf-8") as input_file:
                    output_file.write("\n" + input_file.read())

    _create_training_dataset(chatito_path, output_path)

def _create_generated_path(partials_path, generated_path):
    if (os.path.isdir(generated_path)):
        try:
            shutil.rmtree(generated_path)
        except Exception as e:
            print('Se ha producido un error al eliminar el directorio: %s' % e)
    try:
        os.mkdir(generated_path)
        partial_files = os.listdir(partials_path)
        for file in partial_files:
            for index in range(0, partials[file]):
                shutil.copyfile(partials_path + file, generated_path + str(index) + file)
    except shutil.Error as e:
        print('Se ha producido un error al generar el directorio: %s' % e)
    except OSError as e:
        print('Se ha producido un error al generar el directorio. Error: %s' % e)

def _create_training_dataset(chatito_path, output_path):
    generated_path = chatito_path + GENERATED_DIRECTORY
    os.system("npx chatito " + generated_path + " --format=rasa --outputPath=" + output_path)

generate(properties.chatito_path, properties.dataset_path)