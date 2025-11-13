from algorithms.fsp import FSP

from problems.HS22 import HS22
from problems.HS232 import HS232
from problems.HS29 import HS29
from problems.HS65 import HS65
from problems.HS43 import HS43
from problems.AS6 import AS6
from problems.AS7 import AS7

from problems.HS29_original import HS29Original


# OPTIMIZATION PARAMS
MAX_IT = -1
"""maximum number of iterations (-1 means unlimited)"""
MAX_NF = 10**4
"""maximum number of function evaluation"""
VERBOSITY = False
"""verbosity activation"""
MIN_ALPHA = 1e-7
"""minimum alpha for the linesearch procedure"""
DIRECTION_MODE = 'Standard'
"""direction mode for the FSP algorithm - Possible values: 'Standard', 'Parallel'"""
OUTPUT_PATH = './output/'
"""output path for the results"""


SOLVERS = [FSP(max_it=MAX_IT, max_nf=MAX_NF, 
               verbosity=VERBOSITY, 
               min_alpha=MIN_ALPHA,
               direction_mode=DIRECTION_MODE)]

PROBLEMS = [HS22(), HS232(), HS29(), HS65(), HS43(),
            HS22(c=5), HS232(c=5), HS29(c=5), HS65(c=5), HS43(c=5),
            AS6(6), AS6(7), AS6(8),
            AS7(6), AS7(7), AS7(8), 
            AS6(6, c=5), AS6(7, c=5), AS6(8, c=5),
            AS7(6, c=5), AS7(7, c=5), AS7(8, c=5), 
            HS29Original()]

