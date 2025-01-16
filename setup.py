import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='sap_rpa',
    version='1.0.0',
    author="Richard Raphael Banak",
    description="Library for scrapping and RPA in the SAP S3 and S/4HANA systems.",
    url="https://github.com/Richardbnk/sap_rpa",
    packages=['sap_rpa'],
    
    py_modules = [],
    
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[required],
)
