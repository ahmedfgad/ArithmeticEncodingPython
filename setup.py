from setuptools import setup, find_packages

setup(
    name='ArithmeticEncodingPython',
    version='1.0.0',
    packages=find_packages(),
    description='Data Compression using Arithmetic Encoding in Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ahmed Fawzy Gad',
    author_email='ahmed.f.gad@gmail.com',
    url='https://github.com/ahmedfgad/ArithmeticEncodingPython',
    py_modules=['pyae'],
    install_requires=[
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
