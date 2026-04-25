OK_FORMAT = True

test = {   'name': 'q3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> X_train.shape[0] + X_test.shape[0] == df_model.shape[0]\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> X_train.shape[1] == 3\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> ((X_train >= 0) & (X_train <= 1)).all()\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert X_train.shape[0] == 6813 and X_test.shape[0] == 2920\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
