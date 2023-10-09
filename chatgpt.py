# Import library
import openai

# Read API Key
with open("api_key.txt", "r") as file:
    openai.api_key = file.readline()

# Enter a message
message = input("Send a message: ")

# Send request to ChatGPT and print the result
try:
    response = openai.Completion.create(
        engine = 'gpt-3.5-turbo-instruct',
        prompt = message.encode(encoding='ASCII', errors='ignore').decode(),
        temperature = 0.5,
        top_p = 0.3,
        max_tokens = 2048
    )
    print(response.choices[0].text.strip())
except Exception as ex:
    print(f"GPT-3.5 exception: {ex}")