import pandas
import os
import unittest
f_loc = os.path.dirname(__file__)

from .. import stream
class TestStreamCSV(unittest.TestCase):
    def setUp(self):
        self.ab_path = os.path.join(f_loc, "data","abalone", "abalone.data")
        self.ab_ref = pandas.DataFrame.from_csv(self.ab_path,
                                                header=None,
                                                index_col=None)
        self.ab_stream = stream.Stream.CSV(self.ab_path)
        self.ab_test = pandas.concat(list(self.ab_stream.data()))
        self.ab_test.index = self.ab_ref.index
    def test_sizematch(self):
        self.assertTupleEqual(self.ab_ref.shape,
                              self.ab_test.shape)
        
    def test_equal(self):
        for col in self.ab_ref.columns:
            try:
                self.assertTrue(all(self.ab_ref.loc[:,col] ==
                                    self.ab_test.loc[:,col]))
            except:
                self.assertTrue(all((self.ab_ref.loc[:,col] -
                                     self.ab_test.loc[:,col]) < 1e-10))
        


                        
                                   

                
