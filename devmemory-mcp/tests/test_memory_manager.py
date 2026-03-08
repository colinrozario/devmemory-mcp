from memory.memory_manager import store_memory, query_memory


def test_store_and_query_memory_smoke():
    result = store_memory("test", "hello world", file_path="/tmp/foo.py")
    assert "id" in result

    # Basic smoke check that the query API runs without crashing.
    query_result = query_memory("hello")
    assert isinstance(query_result, dict)
