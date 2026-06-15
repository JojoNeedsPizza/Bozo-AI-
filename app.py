print("Better AI Chat Than ChatGPT")
print("Bozo.ai")
print("woowowowowowoow")
# Wont share my Ai key with yall xD
apikey = input("Input your Google AI Studio API Key:")

from google import genai

client = genai.Client(api_key= apikey)

user_inputanswer= input("Gimme ur question Bozo ^^:")
uia = user_inputanswer
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=user_inputanswer
)
print(response.text)


if uia =="+Exit+":
  repeat = False

else:
  repeat = True
  while repeat is True:
   print("Success")
   break
