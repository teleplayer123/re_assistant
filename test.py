import ollama
from ollama import Client

# client = Client(
#   host='http://localhost:11434',
#   headers={'x-some-header': 'some-value'}
# )
# response = client.chat(model='gemma3:1b', messages=[
#   {
#     'role': 'user',
#     'content': 'Write a rust program to visualize the mandelbrot set.',
#   },
# ])

# print(response['message']['content'])

response = ollama.chat(model='gemma3:1b', messages=[
  {
    'role': 'user',
    'content': 'Write a rust program to visualize the mandelbrot set.',
  },
])
print(response['message']['content'])

