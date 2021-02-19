from setuptools import setup
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='readimg',
    version='0.0.1',
    packages=['readimg'],
    author="lvyunze",
    author_email="17817462542@163.com",
    description="This is a package that read the folder picture and convert it into a digital",
    keywords="read the folder picture and convert it into a digital",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'cycler==0.10.0',
        'decorator==4.4.2',
        'imageio==2.9.0',
        'joblib==1.0.1',
        'kiwisolver==1.3.1',
        'matplotlib==3.3.4',
        'networkx==2.5',
        'numpy==1.20.1',
        'Pillow==8.1.0',
        'pyparsing==2.4.7',
        'python-dateutil==2.8.1',
        'PyWavelets==1.1.1',
        'scikit-image==0.18.1',
        'scikit-learn==0.24.1',
        'scipy==1.6.1',
        'six==1.15.0',
        'threadpoolctl==2.1.0',
        'tifffile==2021.2.1'
    ],
)