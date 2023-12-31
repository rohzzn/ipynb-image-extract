# ipynb-image-extractor

ipynb-image-extractor is a Python package that allows you to easily extract images from IPython Notebooks and save them to a specified output folder.

## Installation

You can install ipynb-image-extractor via pip:

```bash
pip install ipynb-image-extractor
```

## Usage
Once installed, you can use the extract-images command to extract images from an IPython Notebook file and save them to an output folder. Here's the basic usage:

```bash
extract-images input.ipynb output_folder
```
- `input.ipynb`: The path to the IPython Notebook file from which you want to extract images.
- `output_folder`: The folder where the extracted images will be saved.

## How it Works

The package utilizes the `nbformat` and `Pillow` libraries to parse the IPython Notebook and extract image data from 'image/png' outputs. The images are saved in PNG format.

## Contributions

Contributions are welcome! If you encounter issues, have ideas for improvements, or want to contribute to the project, please open an issue or submit a pull request on the [GitHub repository](https://github.com/rohzzn/ipynb-image-extractor).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
