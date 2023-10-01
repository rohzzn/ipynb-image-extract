from setuptools import setup, find_packages

setup(
    name='ipynb-image-extractor',
    version='2.0',
    description='Extract images from IPython Notebooks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    author='Rohan Sanjeev Pothuru',
    author_email='rohan.mbox@gmail.com',
    install_requires=[
        'nbformat',
        'Pillow'
    ],
    entry_points={
        'console_scripts': [
            'extract-images = ipynb_image_extractor.extractor:main',
        ],
    },
)
