import sys
import os

sys.path.append(os.path.abspath("devmemory-mcp"))

from devmemory_mcp.memory.memory_manager import store_memory

try:
    print("Testing store_memory...")
    store_memory(
        "test_type",
        "This is a test content",
        file_path="foo.py",
        function_name="bar"
    )
    print("Successfully added full memory.")
    
    store_memory(
        "test_type",
        "This is a test content",
        file_path=None,
        function_name=None
    )
    print("Successfully added memory with Nones.")
    
except Exception as e:
    import traceback
    traceback.print_exc()
