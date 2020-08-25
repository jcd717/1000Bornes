from setuptools import find_packages, setup

setup(
    name='Mille-Bornes',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    description='Jeu du 1000 Bornes',
    install_requires=[
        'Flask-Session',
        'Flask',
        'Pillow',
        'markdown',
    ],
    python_requires='>=3.8',
    author='Grand Dub',
    author_email='',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License ::  :: CC BY-NC-SA",
        "Operating System :: OS Independent",
    ],
)
