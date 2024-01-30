# Pyvenus96 and Panvenus96

This repository hosts the source files for both the Pyvenus and Panvenus packages.

Author: mizu-bai

## Pyvenus96

Pyvenus provides a means of reading a VENUS96 output file and return its contents as a dictionary of numpy arrays. Pyvenus exposes the following functions:

- `venus96_to_dict`: returns a dictionary of numpy arrays keyed by the energy type from a given path to a VENUS96 output file.
- `read_venus96`: parses an VENUS96 output file and returns the energy terms in a nested list
- `get_unit_dictionary`: returns a dictionary that holds the units of each energy term found in the VENUS96 output file.

## Panvenus96

Panvenus uses the Pyvenus libaray to read a VENUS96 output file and returns its contents as a pandas dataframe. Panvenus exposes the following functions.

- `venus96_to_df`: which gets the path to a VENUS96 output and returns a pandas dataframe.
- `get_unit_dictionary:` returns a dictionary that holds the units of each energy term found in the VENUS96 output file.

## Example

Using `pyvenus96`

```python
import pyvenus96

# read the VENUS96 output file
path = "ch4.out"
dic = pyvenus96.venus96_to_dict(path)

# get the unts
unit_dict = pyvenus96.get_unit_dictionary(path)
```

Using `panvenus96`

```python
import panvenus96

# read the VENUS96 output file
path = "ch4.out"
df = panvenus96.venus96_to_df(path)

# get the units
unit_dict = panvenus96.get_unit_dictionary(path)
```

## Install

Here is a shell script for installing `pyvenus96` and `panvenus96`:

```bash
$ bash install.sh
```

## License

BSD-2-Clause license
