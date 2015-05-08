import unittest

import numpy as np
import scipy.sparse

from ParamSklearn.components.preprocessing.select_rates import \
    SelectRates
from ParamSklearn.util import _test_preprocessing, get_dataset


class SelectRatesComponentTest(unittest.TestCase):
    def test_default_configuration(self):
        transformation, original = _test_preprocessing(SelectRates)
        self.assertEqual(transformation.shape[0], original.shape[0])
        self.assertEqual(transformation.shape[1], 3)
        self.assertFalse((transformation == 0).all())

        transformation, original = _test_preprocessing(
            SelectRates, make_sparse=True)
        self.assertTrue(scipy.sparse.issparse(transformation))
        self.assertEqual(transformation.shape[0], original.shape[0])
        self.assertEqual(transformation.shape[1], int(original.shape[1] / 2))

    def test_preprocessing_dtype(self):
        # Dense
        # np.float32
        X_train, Y_train, X_test, Y_test = get_dataset("iris")
        self.assertEqual(X_train.dtype, np.float32)

        configuration_space = SelectRates.get_hyperparameter_search_space()
        default = configuration_space.get_default_configuration()
        preprocessor = SelectRates(random_state=1,
                                                      **{
                                                          hp.hyperparameter.name: hp.value
                                                          for hp
                                                          in
                                                          default.values.values()})
        preprocessor.fit(X_train, Y_train)
        Xt = preprocessor.transform(X_train)
        self.assertEqual(Xt.dtype, np.float32)

        # np.float64
        X_train, Y_train, X_test, Y_test = get_dataset("iris")
        X_train = X_train.astype(np.float64)
        configuration_space = SelectRates.get_hyperparameter_search_space()
        default = configuration_space.get_default_configuration()
        preprocessor = SelectRates(random_state=1,
                                                      **{
                                                          hp.hyperparameter.name: hp.value
                                                          for hp
                                                          in
                                                          default.values.values()})
        preprocessor.fit(X_train, Y_train)
        Xt = preprocessor.transform(X_train)
        self.assertEqual(Xt.dtype, np.float64)

        # Sparse
        # np.float32
        X_train, Y_train, X_test, Y_test = get_dataset("iris", make_sparse=True)
        self.assertEqual(X_train.dtype, np.float32)
        configuration_space = SelectRates.get_hyperparameter_search_space()
        default = configuration_space.get_default_configuration()
        preprocessor = SelectRates(random_state=1,
                                                      **{
                                                          hp.hyperparameter.name: hp.value
                                                          for hp
                                                          in
                                                          default.values.values()})
        preprocessor.fit(X_train, Y_train)
        Xt = preprocessor.transform(X_train)
        self.assertEqual(Xt.dtype, np.float32)

        # np.float64
        X_train, Y_train, X_test, Y_test = get_dataset("iris", make_sparse=True)
        X_train = X_train.astype(np.float64)
        configuration_space = SelectRates.get_hyperparameter_search_space()
        default = configuration_space.get_default_configuration()
        preprocessor = SelectRates(random_state=1,
                                                      **{
                                                          hp.hyperparameter.name: hp.value
                                                          for hp
                                                          in
                                                          default.values.values()})
        preprocessor.fit(X_train, Y_train)
        Xt = preprocessor.transform(X_train)
        self.assertEqual(Xt.dtype, np.float64)
