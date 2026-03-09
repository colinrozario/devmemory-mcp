from .metadata_store import create_memory
from .vector_store import add_vector, search_vectors


def store_memory(
    memory_type,
    content,
    file_path=None,
    function_name=None
):

    memory_id = create_memory(
        memory_type,
        content,
        file_path,
        function_name
    )

    metadata = {
        "id": memory_id,
        "type": memory_type,
        "file": file_path,
        "function": function_name
    }
    
    # ChromaDB does not support None values in metadata dictionaries. 
    # We must filter out any keys where the value is None before passing it.
    clean_metadata = {k: v for k, v in metadata.items() if v is not None}

    add_vector(content, clean_metadata)

    return {"id": memory_id}


def query_memory(query):

    return search_vectors(query)