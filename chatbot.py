import openai
import pandas as pd

# Đặt API key của OpenAI
openai.api_key = "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"

# Đường dẫn đến file Excel
excel_file_path = "C:/Users/phong/Documents/Year 4/Do_an_2/Chatbot/Data.xlsx"

# Đọc dữ liệu từ file Excel vào DataFrame
df = pd.read_excel(excel_file_path)

def chat_with_bot(user_question):
    # Tìm kiếm câu trả lời trong DataFrame
    row = df[df['Câu hỏi'] == user_question]
    
    if not row.empty:
        # Nếu câu trả lời có sẵn trong file Excel
        answer = row.iloc[0]['Câu trả lời']
    else:
        # Nếu không tìm thấy câu trả lời, gửi câu hỏi tới API ChatGPT
        try:
            response = openai.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt= user_question.encode(encoding = 'ASCII',
                errors = 'ignore').decode(),
                temperature = 0.5,
                top_p = 0.3,
                max_tokens = 512
                )
            answer = response.choices[0].text.strip()
        except Exception as ex:
            answer = f"GPT-3.5 exception: {ex}"

    return answer

# Hỏi người dùng câu hỏi
user_question = input("Nhập câu hỏi của bạn: ")

# Gọi hàm để lấy câu trả lời
bot_reply = chat_with_bot(user_question)

# Hiển thị câu trả lời của chatbot
print("Chatbot:", bot_reply)
