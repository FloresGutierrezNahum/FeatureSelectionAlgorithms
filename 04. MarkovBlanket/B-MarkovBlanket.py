from pycit.markov_blanket import MarkovBlanket
from numpy import array

# specify CI test configuration
cit_funcs = {
    'it_args': {
        'test_args': {
            'statistic': 'ksg_mi',
            'n_jobs': 2
        }
    },
    'cit_args': {
        'test_args': {
            'statistic': 'ksg_cmi',
            'n_jobs': 2
        }
    }
}

# find Markov blanket of Y. x_data contains data from predictor variables, X_1,...,X_m

mb = MarkovBlanket(x_data, y_data, cit_funcs)
markov_blanket = mb.find_markov_blanket()