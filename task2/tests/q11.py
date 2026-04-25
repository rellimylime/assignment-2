OK_FORMAT = True

test = {   'name': 'q11',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> cm_lr.shape == (2, 2)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> cm_lr.sum() == len(y_test)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert (cm_lr == np.array([[1693, 277], [379, 571]])).all()\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
