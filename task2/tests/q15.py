OK_FORMAT = True

test = {   'name': 'q15',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> assert (cm_knn == np.array([[1717, 253], [401, 549]])).all()\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert np.isclose(precision_knn, 0.6845, atol=0.001)\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert np.isclose(recall_knn, 0.5779, atol=0.001)\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert np.isclose(f1_knn, 0.6267, atol=0.001)\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
