# import pytest
#
# @pytest.fixture(autouse=True)
# def always_used_fixture(request):
#     print(f"\n Always, HI!")
#
#     def second():
#         print(f"\n Do something, after test")
#
#     request.addfinalizer(second)
