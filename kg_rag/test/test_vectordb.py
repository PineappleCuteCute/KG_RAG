from kg_rag.utility import *
import sys

VECTOR_DB_PATH = config_data["VECTOR_DB_PATH"]
SENTENCE_EMBEDDING_MODEL_FOR_NODE_RETRIEVAL = config_data["SENTENCE_EMBEDDING_MODEL_FOR_NODE_RETRIEVAL"]

print("Đang kiểm tra việc tải vectorDB ...")
print("")
try:
    vectorstore = load_chroma(VECTOR_DB_PATH, SENTENCE_EMBEDDING_MODEL_FOR_NODE_RETRIEVAL)
    print("vectorDB đã được tải thành công!")
except:
    print("vectorDB không được tải. Kiểm tra đường dẫn được cung cấp trong 'VECTOR_DB_PATH' của config.yaml")
    print("")
    sys.exit(1)
try:
    print("")
    print("Đang kiểm tra việc trích xuất thực thể ...")
    print("")
    entity = "psoriasis"
    print("Đang nhập '{}' làm thực thể để kiểm tra ...".format(entity))    
    print("")
    node_search_result = vectorstore.similarity_search_with_score(entity, k=1)
    extracted_entity = node_search_result[0][0].page_content
    print("Thực thể được trích xuất là '{}'".format(extracted_entity))
    print("")
    if extracted_entity == "psoriasis":                
        print("Việc trích xuất thực thể thành công!")
        print("")
        print("vectorDB đã được điền đúng cách và sẵn sàng để sử dụng!")
    else:
        print("Việc trích xuất thực thể không thành công. Đảm bảo rằng vectorDB đã được điền đúng cách. Tham khảo 'Cách chạy KG-RAG' Bước 5")
        print("")
        sys.exit(1)
except:
    print("Việc trích xuất thực thể không thành công. Đảm bảo rằng vectorDB đã được điền đúng cách. Tham khảo 'Cách chạy KG-RAG' Bước 5")
    print("")
    sys.exit(1)