"""
Setup configuration for Hematology PDF Data Extractor
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open(os.path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='hematology-pdf-extractor',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='Automated extraction and analysis of hematology test data from PDF lab reports',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/hematology-pdf-extractor',
    project_urls={
        'Bug Reports': 'https://github.com/yourusername/hematology-pdf-extractor/issues',
        'Documentation': 'https://github.com/yourusername/hematology-pdf-extractor/blob/main/docs/README.md',
        'Source': 'https://github.com/yourusername/hematology-pdf-extractor',
    },
    packages=find_packages(exclude=['tests', 'docs', 'examples']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    keywords=[
        'medical', 'healthcare', 'hematology', 'pdf-extraction', 
        'data-automation', 'clinical-research', 'thalassemia',
        'laboratory', 'health-informatics', 'biomedical',
        'data-pipeline', 'medical-records', 'pdf-parser'
    ],
    python_requires='>=3.8',
    install_requires=requirements,
    extras_require={
        'dev': [
            'pytest>=7.4.0',
            'black>=23.7.0',
            'flake8>=6.1.0',
            'mypy>=1.5.0',
        ],
        'ocr': [
            'pytesseract>=0.3.10',
            'Pillow>=10.0.0',
        ],
        'viz': [
            'matplotlib>=3.7.0',
            'seaborn>=0.12.0',
        ],
        'excel': [
            'openpyxl>=3.1.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'hematology-extract=pdf_extractor_final:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
