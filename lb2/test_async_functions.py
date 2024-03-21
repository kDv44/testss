import unittest
import json
import asyncio


# Завдання 1
def function1(name, lastname):
    return function2(name, lastname)

def function2(name, lastname):
    return f"{name} {lastname}"

class TestFunctions(unittest.TestCase):
    def test_function1_calls_function2_with_arguments(self):
        expected_result = "John Doe"
        result = function1(name="John", lastname="Doe")
        self.assertEqual(result, expected_result)

# Завдання 2
async def async_function():
    return "hello world"

class TestAsyncFunction(unittest.TestCase):
    def test_async_function_returns_hello_world(self):
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(async_function())
        self.assertEqual(result, "hello world")


# Завдання 3
async def async_function_with_promise():
    return 42

async def async_function_caller():
    return await async_function_with_promise()

class TestAsyncAwait(unittest.TestCase):
    def test_async_function_caller_returns_expected_value(self):
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(async_function_caller())
        self.assertEqual(result, 42)


# Завдання 4
async def async_function_error():
    raise ValueError("Something went wrong")

class TestAsyncError(unittest.TestCase):
    def test_async_function_error_raises_expected_error(self):
        loop = asyncio.get_event_loop()
        with self.assertRaises(ValueError):
            loop.run_until_complete(async_function_error())


# Завдання 5
async def fetch_api():
    return json.dumps({"message": "Hello, world!"})

class TestFetchAPI(unittest.TestCase):
    def test_fetch_api_returns_expected_json_response(self):
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(fetch_api())
        expected_result = json.dumps({"message": "Hello, world!"})
        self.assertEqual(result, expected_result)

# Завдання 6
async def fetch_fake_api():
    return json.dumps({"result": "success"})

class TestFetchFakeAPI(unittest.TestCase):
    def test_fetch_fake_api_returns_expected_json_response(self):
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(fetch_fake_api())
        expected_result = json.dumps({"result": "success"})
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
