import pickle
import numpy as np
from tqdm import tqdm
import os
from warnings import warn

from utils.latex_utils import create_table
from config import MAX_IT, MAX_NF, VERBOSITY, MIN_ALPHA, OUTPUT_PATH, SOLVERS, PROBLEMS


os.makedirs(OUTPUT_PATH, exist_ok=True)

if os.path.exists(os.path.join(OUTPUT_PATH, 'benchmark_results.pkl')):
    warn(f'Looks like experiments have already been run. '
         f'If you want to re-execute them. Please delete {os.path.join(OUTPUT_PATH, "benchmark_results.pkl")}')

    with open(os.path.join(OUTPUT_PATH, 'benchmark_results.pkl'), 'rb') as f:
        results = pickle.load(f)

else:
    results = {'max_it': MAX_IT, 'max_nf': MAX_NF, 
               'verbosity': VERBOSITY, 'min_alpha': MIN_ALPHA,
               'solvers': dict()}

    for idx_s, s in enumerate(SOLVERS):
        
        print('Running benchmark for solver: {}\n'.format(str(s)))
        results['solvers'][str(s)] = {}
        
        pbar = tqdm(PROBLEMS)
        for prob in pbar:
            pbar.set_postfix_str(f'problem: {prob.name}')
            
            x_bar, history = s.solve(prob.f, prob.proj_op, prob.x0)
            
            x0, _ = prob.proj_op(np.copy(prob.x0))
            x_bar, _ = prob.proj_op(np.copy(x_bar))

            results['solvers'][str(s)][prob.name] = {'x_0': x0, 'f_x0': prob.f(x0),
                                                             'f_x': np.array([prob.f(x) for x in history.iterates['x']]),
                                                             'x_bar': x_bar, 'f_xbar': prob.f(x_bar),
                                                             'viol_0': np.linalg.norm(np.maximum(prob.g(x0), 0)),
                                                             'viol_x': np.array([np.linalg.norm(np.maximum(prob.g(x), 0)) for x in history.iterates['x']]),
                                                             'viol_xbar': np.linalg.norm(np.maximum(prob.g(x_bar), 0)),
                                                             'n_it': len(history.iterates['x']),
                                                             'nf': min(history.dataframe['num_f'].cumsum().iloc[-1], MAX_NF),
                                                             'np': min(int(history.dataframe.iloc[-1]['n_proj']), MAX_NF),
                                                             'T': history.dataframe['time'].cumsum().iloc[-1],
                                                             'hist': history.dataframe}

    with open(os.path.join(OUTPUT_PATH, 'benchmark_results.pkl'), 'wb') as f:
        pickle.dump(results, f)

print(f'Exporting table in {OUTPUT_PATH}...')
create_table(results['solvers'])
