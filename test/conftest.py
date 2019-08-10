import pytest

@pytest.fixture(scope="session")
def first(request):
    print(f"\n Connect to DB before {request.scope} ")

    def second():
        print(f"\n Close connect after {request.scope}")

    request.addfinalizer(second)


@pytest.fixture()
def third_fixture():
    l = [x for x in range(20) if x % 2 == 0]
    return sum(l)


@pytest.fixture(params=[10])
def fixture_with_params(request):
    return request.param
