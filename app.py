import openai

# Replace with your actual OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY" 

def get_completion(prompt, max_tokens=1024, n=1, stop=None, temperature=0.7):
  """
  Gets a text completion from the OpenAI API.

  Args:
    prompt: The input text for the LLM.
    max_tokens: The maximum number of tokens in the output.
    n: The number of completions to generate.
    stop: A sequence of characters to stop generation at.
    temperature: Controls the randomness of the output.

  Returns:
    The generated text.
  """
  response = openai.Completion.create(
      engine="text-davinci-003", 
      prompt=prompt,
      max_tokens=max_tokens,
      n=n,
      stop=stop,
      temperature=temperature
  )
  return response.choices[0].text

# Example usage
prompt = "Write a short story about a cat who goes on an adventure."
story = get_completion(prompt)
print(story)