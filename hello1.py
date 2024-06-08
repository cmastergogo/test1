import numpy as np
import time
import scipy.linalg as la
from scipy.sparse import dok_matrix
from scipy.sparse.linalg import eigs, eigsh
import warnings
from scipy.optimize import curve_fit
import cmath