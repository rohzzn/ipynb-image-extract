import nbformat
import os
from nbconvert.preprocessors import ExecutePreprocessor
from IPython.display import Image as IPImage
from PIL import Image
import base64

def extract_images_from_ipynb(ipynb_file, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    with open(ipynb_file, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    image_counter = 1

    for cell in notebook['cells']:
        if 'outputs' in cell:
            for output in cell['outputs']:
                if 'data' in output and 'image/png' in output['data']:
                    image_data = output['data']['image/png']
                    image_data = base64.b64decode(image_data)
                    image_path = os.path.join(output_folder, f'image_{image_counter}.png')
                    with open(image_path, 'wb') as img_file:
                        img_file.write(image_data)
                    image_counter += 1

    return f'{image_counter - 1} images extracted to {output_folder}'

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: extract-images input.ipynb output_folder")
    else:
        input_ipynb = sys.argv[1]
        output_folder = sys.argv[2]
        result = extract_images_from_ipynb(input_ipynb, output_folder)
        print(result)
