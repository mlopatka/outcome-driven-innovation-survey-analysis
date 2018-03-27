SOMPY
-----
A Python Library for performing needs-based segmentation of survey respondents

The input space relies on a specific schematic structure for the survey responses, Multiple imputation can be used to account for incomplete responses, but warnings will be thrown for high sparsity datasets.

Survey schema is described in SURVEY_SCHEMA.md

### Dependencies:
SOMPY has the following dependencies (tested only with Python 2.7x):
- numpy
- scipy
- scikit-learn
- numexpr
- matplotlib
- pandas
- ipdb
- sompy

### Installation:
```Python
python setup.py install
```


Many thanks to @sebastiandev, the library is now standardized in a pythonic tradition. Below you can see some basic examples, showing how to use the library.
But I recommend you to go through the codes. There are several functionalities already implemented, but not documented. I would be very happy to add your new examples here. 

[Basice Example](https://gist.github.com/sevamoo/035c56e7428318dd3065013625f12a11)

### Citation

There is no published paper about this analysis. If you find this code useful, please accknowledge the main contributors.

```
Main Contributers:
Martin Lopatka [mlopatka@mozilla.com]
Fredreik Wollesen [fwollsen@mozilla.com]
```
