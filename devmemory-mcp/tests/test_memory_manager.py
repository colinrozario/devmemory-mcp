from memory.memory_manager import MemoryManager


def test_memory_manager_store_and_retrieve():
    mgr = MemoryManager()
    mgr.store("test", [1, 2, 3], {"source": "unit-test"})

    result = mgr.retrieve("test")
    assert result["vector"] == [1, 2, 3]
    assert result["metadata"]["source"] == "unit-test"
