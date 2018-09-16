from pathlib import Path

from setuptools import find_packages, setup

requirements = Path(__file__).parent / 'requirements/core.txt'

with requirements.open(mode='rt', encoding='utf-8') as fp:
    install_requires = [line.strip() for line in fp]

readme = Path(__file__).parent / 'README.rst'

with readme.open(mode='rt', encoding='utf-8') as fp:
    readme_text = fp.read()

setup(
    name='langoustine',
    version='0.0.1',
    description='Multilingual text utilites.',
    long_description=readme_text,
    license='MIT',
    author='Luka Shostenko',
    author_email='luka.shostenko@gmail.com',
    url='https://github.com/lshostenko/langoustine/',
    packages=find_packages(include=['langoustine.*']),
    py_modules=['langoustine.settings'],
    python_requires='>=3.5.0',
    install_requires=install_requires,
    include_package_data=True,
)
