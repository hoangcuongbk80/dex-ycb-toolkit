import os

from dex_ycb_toolkit.hpe_eval import HPEEvaluator

name = 's0_test'
hpe_eval = HPEEvaluator(name)

res_file = os.path.join("results", "example_results_hpe_{}.txt".format(name))

hpe_eval.evaluate(res_file)
