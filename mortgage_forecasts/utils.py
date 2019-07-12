'''Auxilary tools for working with rate models.'''

import pandas as pd
from scipy.stats import norm

def compute_margin(stderr, confint=0.95):
    '''Compute margin of error from standard error

    Paramters
    ---------
    stderr: The standard error of a prediction
    confint: The desired confidence interval
             (defaults to 0.95)

    Returns
    -------
    margin_of_error: fractional margin of error'''

    z = norm.ppf((1+confint)/2)
    return stderr * z

def read_data(filename):
    '''Read mortgage rate data

    Parameters
    ----------
    filename: path to CSV file
              Formatted as https://fred.stlouisfed.org/series/MORTGAGE30US

    Returns
    -------
    rates: Pandas Series with datetime index'''

    df = pd.read_csv(filename, index_col='DATE', parse_dates=True)
    rates = df['MORTGAGE30US']
    monthly = rates.resample('MS').first()
    return monthly
