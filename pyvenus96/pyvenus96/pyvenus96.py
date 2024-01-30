from typing import Dict, List, Tuple

import numpy as np

all_energyies_type = List[List[float]]
all_names_type = List[str]
times_type = List[float]
read_venus_return_type = Tuple[
    all_energyies_type,
    all_names_type,
    times_type,
]


def read_venus96(
    path: str,
) -> read_venus_return_type:
    """Parse VENUS96 output and make contents available in Python.

    Arguments:
        path (str): Path to VENUS96 output.

    Returns:
        all_energies (List[List[float]]): A nested containing the energy values
            for each frame found in the VENUS96 output.
        all_names (List[str]): A list containing the names of the energy terms
            found in the file.
        times (List[float]): A list containing the time of each step/frame.
    """

    times = []
    kinetic = []
    potential = []
    total = []

    with open(path, "r") as f:
        while line := f.readline():
            if "THE CYCLE COUNT IS" in line:
                arr = line.split()

                # venus time 10e-14 s to ps
                t = float(arr[-1]) * 1.0e-02
                times.append(t)
            elif "KINETIC ENERGY" in line:
                arr = line.split()

                # kcal/mol to kJ/mol
                kt = float(arr[2].replace("D", "e")) * 4.184
                kinetic.append(kt)

                # kcal/mol to kJ/mol
                pot = float(arr[5].replace("D", "e")) * 4.184
                potential.append(pot)
            elif "TOTAL ENERGY" in line:
                arr = line.split()

                # kcal/mol to kJ/mol
                tot = float(arr[2].replace("D", "e")) * 4.184
                total.append(tot)

    all_energyies = list(zip(*[times, kinetic, potential, total]))
    all_names = ["Time", "Kinetic En.", "Potential", "Total Energy"]

    return (all_energyies, all_names, times)


def get_unit_dictionary(
    path: str,
) -> Dict[str, str]:
    """Reads the names and units of a VENUS96 output and returns as a
    dictionary mapping column names (str) to unit names (str).

    Arguments:
        path (str): Path to VENUS96 output.

    Returns:
        unit_dict (Dict[str, str]): A dictionary mapping the term names to
            their units.
    """

    unit_dict = {
        "Time": "ps",
        "Kinetic En.": "kJ/mol",
        "Potential": "kJ/mol",
        "Total Energy": "kJ/mol",
    }

    return unit_dict


def venus96_to_dict(
    path: str,
) -> Dict[str, np.ndarray]:
    """Calls `read_venus` and packs its return values into a dictionary.

    Arguments:
        path (str): Path to VENUS96 output.

    Returns:
        energy_dict (Dict[str, np.ndarray]): Dictionary that holds all energy
            terms found in the VENUS96 output.
    """

    all_energies, all_names, times = read_venus96(path)

    energy_dict = {}

    for idx, name in enumerate(all_names):
        energy_dict[name] = np.array(
            [all_energies[frame][idx] for frame in range(len(times))])

    return energy_dict


if __name__ == "__main__":
    import sys
    print(venus96_to_dict(sys.argv[1]))
