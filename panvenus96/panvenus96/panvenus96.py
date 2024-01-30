import pandas as pd

from pyvenus96 import get_unit_dictionary, read_venus96


def venus96_to_df(
    path: str,
) -> pd.DataFrame:
    """Calls `read_venus` from ``pyvenus`` and packs its return values into a
    ``pandas.DataFrame``.

    Arguments:
        path (str): Path to VENUS96 output.

    Returns:
        df (pandas.DataFrame): `pandas.DataFrame` object that holds all energy
            terms found in the VENUS96 output.
    """

    all_energies, all_names, times = read_venus96(path)
    df = pd.DataFrame(all_energies, columns=all_names, index=times)
    return df
