"""My nifty plot-level RGB algorithm
"""

# Importing modules. Please add any additional import statements below
import numpy as np

# Definitions
# Please replace these definition's values with the correct ones
VERSION = '1.0'

# Information on the creator of this algorithm
ALGORITHM_AUTHOR = 'Chris Schnaufer'
ALGORITHM_AUTHOR_EMAIL = 'schnaufer@email.arizona.edu'
ALGORITHM_CONTRIBUTORS = ["Zongyang Li"]

ALGORITHM_NAME = 'canopycover'
ALGORITHM_DESCRIPTION = 'Canopy Cover by Plot (Percentage of Green Pixels)'
ALGORITHM_METHOD = 'Canopy Cover Estimation from RGB images'

# Citation information for publication (more information in HOW_TO.md)
CITATION_AUTHOR = '"Zongyang, Li"'
CITATION_TITLE = 'Maricopa Field Station Data and Metadata'
CITATION_YEAR = '2016'

# The name of one or more variables returned by the algorithm, separated by commas (more information in HOW_TO.md)
# If only one name is specified, no comma's are used.
# Note that variable names cannot have comma's in them: use a different separator instead. Also,
# all white space is kept intact; don't add any extra whitespace since it may cause name comparisons
# to fail.
VARIABLE_NAMES = 'canopy_cover'

# Variable units matching the order of VARIABLE_NAMES, also comma-separated.
# For each variable name in VARIABLE_NAMES add the unit of measurement the value represents.
# !! Replace the content of this string with your variables' unit
VARIABLE_UNITS = 'percent'

# Variable labels matching the order of VARIABLE_NAMES, also comma-separated.
# This is an optional definition and can be left empty.
VARIABLE_LABELS = 'Canopy Cover'

# Optional override for the generation of a BETYdb compatible csv file
# Set to False to suppress the creation of a compatible file
WRITE_BETYDB_CSV = True

# Optional override for the generation of a TERRA REF Geostreams compatible csv file
# Set to False to suppress the creation of a compatible file
WRITE_GEOSTREAMS_CSV = True


def calculate_canopycover_masked(pxarray) -> float:
    """Return greenness percentage of given numpy array of pixels.
    Args:
      pxarray (numpy array): rgb image
    Return:
      (float): greenness percentage
    """
    # For masked images, all nonzero pixels are considered canopy
    nonzeros = np.count_nonzero(pxarray)
    ratio = nonzeros/float(pxarray.size)
    # Scale ratio from 0-1 to 0-100
    ratio *= 100.0

    return ratio


# Entry point for plot-level RBG algorithm
def calculate(pxarray: np.ndarray):
    """Calculates one or more values from plot-level RGB data
    Arguments:
        pxarray: Array of RGB data for a single plot
    Return:
        Returns one or more calculated values
    """
    canopy_cover = calculate_canopycover_masked(pxarray)

    return canopy_cover
