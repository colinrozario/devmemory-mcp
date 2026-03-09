import sys
import os

sys.path.append(os.path.abspath("devmemory-mcp"))

from memory.memory_manager import store_memory
from pprint import pprint

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

    store_memory(
        memory_type="test_type",
        content="Cursor successfully connected to DevMemory on my first try!",
        file_path="",
        function_name=""
    )
    print("Successfully added memory with empty strings.")
    
except Exception as e:
    import traceback
    traceback.print_exc()
