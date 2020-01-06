import sys
sys.path.append('../')


import random
import pytest
from san_diego import max_pairwise_product


class TestModuleMaxPairwiseProduct(object):

    def test_method_find_max_num(self):
        for _ in range(100):
            n = random.randint(0, 10000)
            input_numbers = random.choices(range(0, 10000), k=n)
            assert max_pairwise_product.find_max_num(input_numbers) == max(input_numbers), 'find_max_num method is failing'


    def test_method_find_max_num_when_list_is_small(self):
        for n in [1, 2]:
            input_numbers = random.choices(range(0, 10000), k=n)
            assert max_pairwise_product.find_max_num(input_numbers) == max(input_numbers), 'find_max_num method is failing'


    def test_method_find_max_num_when_list_is_empty(self):
        with pytest.raises(ValueError):
            input_numbers = random.choices(range(0, 10000), k=0)
            max_pairwise_product.find_max_num(input_numbers)







