import os
from kg_rag.utility import config_data

def download_llama(method):
    from kg_rag.utility import llama_model
    try:
        llama_model(config_data["LLAMA_MODEL_NAME"], config_data["LLAMA_MODEL_BRANCH"], config_data["LLM_CACHE_DIR"], method=method)
        print("Model đã được tải xuống thành công vào thư mục cache được cung cấp!")
    except:
        print("Model không được tải xuống! Hãy đảm bảo rằng các điều kiện được đề cập ở trên đã được đáp ứng.")
        

print("")
print("Bắt đầu thiết lập KG-RAG ...")
print("")

user_input = input("Bạn đã cập nhật tệp config.yaml với tất cả các cấu hình cần thiết (chẳng hạn như đường dẫn GPT .env, đường dẫn tệp vectorDB, các đường dẫn tệp khác) chưa? Nhập Y hoặc N: ")
print("")
if user_input == "Y":
    print("Đang kiểm tra vectorDB bệnh ...")
    try:
        if os.path.exists(config_data["VECTOR_DB_PATH"]):
            print("vectorDB đã tồn tại!")
        else:
            print("Đang tạo vectorDB ...")
            from kg_rag.vectorDB.create_vectordb import create_vectordb
            create_vectordb()
    except:
        print("Hãy kiểm tra lại đường dẫn đã được cung cấp trong VECTOR_DB_PATH của tệp config.yaml.")

    print("")
    user_input_1 = input("Bạn có muốn cài đặt mô hình Llama không? Nhập Y hoặc N: ")
    if user_input_1 == "Y":
        user_input_2 = input("Bạn đã cập nhật tệp config.yaml với cấu hình phù hợp để tải xuống mô hình Llama chưa? Nhập Y hoặc N: ")
        if user_input_2 == "Y":
            user_input_3 = input("Bạn có đang sử dụng mô hình Llama chính thức từ Meta không? Nhập Y hoặc N: ")
            if user_input_3 == "Y":
                user_input_4 = input("Bạn đã có quyền truy cập để sử dụng mô hình chưa? Nhập Y hoặc N: ")
                if user_input_4 == "Y":
                    download_llama()
                    print("Chúc mừng! Quá trình thiết lập đã hoàn tất.")
                else:
                    print("Hủy bỏ!")
            else:
                download_llama(method='method-1')
                user_input_5 = input("Bạn có nhận được thông báo như 'Model không được tải xuống!' không? Nhập Y hoặc N: ")
                if user_input_5 == "N":                
                    print("Chúc mừng! Quá trình thiết lập đã hoàn tất.")
                else:
                    download_llama(method='method-2')
                    user_input_6 = input("Bạn có nhận được thông báo như 'Model không được tải xuống!' không? Nhập Y hoặc N: ")
                    if user_input_6 == "N":                        
                        print("""
                        QUAN TRỌNG : 
                        Mô hình Llama đã được tải xuống bằng phương pháp 'LlamaTokenizer' thay vì 'AutoTokenizer'. 
                        Vì vậy, khi bạn chạy script tạo văn bản, vui lòng cung cấp thêm đối số dòng lệnh '-m method-2'.
                        Ví dụ:
                            python -m kg_rag.rag_based_generation.Llama.text_generation -m method-2
                        """)
                        print("Chúc mừng! Quá trình thiết lập đã hoàn tất.")
                    else:
                        print("Chúng tôi đã thử hai phương pháp để tải xuống Llama. Nếu cả hai đều không hoạt động, vui lòng kiểm tra yêu cầu cấu hình Llama trên trang thẻ mô hình của huggingface. Hủy bỏ!")
        else:
            print("Hủy bỏ!")
    else:
        print("Không sao. Llama sẽ được cài đặt tự động khi bạn chạy mô hình lần đầu tiên.")
        print("Chúc mừng! Quá trình thiết lập đã hoàn tất.")
else:
    print("Bước đầu tiên, hãy cập nhật tệp config.yaml và sau đó chạy lại script python này.")