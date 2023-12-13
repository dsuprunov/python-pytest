import pytest
from src.stack import Stack


@pytest.fixture(scope='session', autouse=True)
def run_me_to_set_test_env():
    print('-- run me before --')
    yield
    print('-- run me after --')


# @pytest.mark.usefixtures('run_me_to_set_test_env')
class TestStack:
    TEST_STACK_SIZE = 5

    @pytest.fixture(scope='session')
    def my_test_stack(self):
        return Stack().insert(*range(self.TEST_STACK_SIZE))

    @pytest.mark.parametrize('a, b, c', [
        (1, 2, [2, 1]),
    ])
    def test_insert_one(self, a, b, c):
        assert Stack().insert(a).insert(b).items() == c

    @pytest.mark.parametrize('a, b', [
        ([1, 2, 3], [3, 2, 1])
    ])
    def test_insert_many(self, a, b):
        assert Stack().insert(*a).items() == b

    def test_size(self, my_test_stack):
        stack = my_test_stack.copy()
        assert stack.size() == self.TEST_STACK_SIZE

    def test_remove(self, my_test_stack):
        stack = my_test_stack.copy()
        stack.remove()
        assert stack.size() == self.TEST_STACK_SIZE - 1

    def test_copy(self, my_test_stack):
        assert my_test_stack.copy() == my_test_stack
