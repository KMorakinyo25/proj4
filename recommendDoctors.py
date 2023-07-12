import openai

# Set your OpenAI API key
openai.api_key = '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'

# Define your prompt
prompt = "Once upon a time"

# Make an API call
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt,
  max_tokens=100
)

# Extract the generated text from the response
generated_text = response.choices[0].text.strip()

# Print the generated text
print(generated_text)
