OK_FORMAT = True

test = {   'name': 'q5',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> optimal_k == 15\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(cv_mean_scores) == 20\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert np.isclose(best_cv_score, 0.7743, atol=0.001)\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert cv_mean_scores.argmax() == 14\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
