from transformers import pipeline

def genai_function():
    # Initialize the text generation pipeline with a model
    generator = pipeline('text-generation', model='gpt2')
    # Define the prompt for generating a resume
    prompt = """
    This is my resume: <insert_random_resume_information>
    This is the job description: <insert_random_job_info>
    Please generate a sample text requesting for a referral.
    """
    # Generate the text
    result = generator(prompt, max_length=200, num_return_sequences=1)
    # Print the generated text
    print(result[0]['generated_text'])
    
    
genai_function()