import pytest
from test_async_functions import *

def function1(name, lastname):
    return function2(name, lastname)

def function2(name, lastname):
    return f"{name} {lastname}"

def test_function_call_with_arguments():
    result = function1(name="John", lastname="Doe")
    assert result == "John Doe"

async def async_function():
    return "hello world"

@pytest.mark.asyncio
async def test_async_function():
    result = await async_function()
    assert result == "hello world"

async def async_function2():
    return 42

async def test_async_function_with_async_await():
    result = await async_function2()
    assert result == 42


if __name__ == "__main__":
    pytest.main([__file__])
