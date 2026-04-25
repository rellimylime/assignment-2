OK_FORMAT = True

test = {   'name': 'q4',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> assert np.isclose(knn3_accuracy, 0.7418, atol=0.0001)\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert len(y_pred_knn3) == 2920\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert set(y_pred_knn3) == {0, 1}\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert knn3.n_neighbors == 3\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
