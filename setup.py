try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name="nbs-python",
    version="0.1",
    description="Needs Based Segmentation for survey respondents",
    author="Martin Lopatka and Fredrik Wollsen",
    packages=find_packages(),
    install_requires=['numpy >= 1.7', 'scipy >= 0.9',
                      'scikit-learn >= 0.16', 'numexpr >= 2.5',
                      'sompy >= 1.0', 'pandas >= 0.20',
                      'ipdb >= 0.11', 'matplotlib >= 2.0']
)
