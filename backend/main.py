# use PEP8
import os,requests
from fastapi import FastAPI,HTTPException,status
from typing import Annotated
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

app:FastAPI = FastAPI()
api_key = os.getenv("GROQ_CHATBOT_API")
client = Groq(api_key=api_key)
@app.get("/")
def index():
    return {"message": "Welcome to AIDAS!"}

@app.post("/generate")
async def generate_content(prompt:str):
    try:
        chat_completion = client.chat.completions.create(
            #
            # Required parameters
            #
            messages=[
                # Set an optional system message. This sets the behavior of the
                # assistant and can be used to provide specific instructions for
                # how it should behave throughout the conversation.
                {
                    "role": "system",
                    "content": "you are a helpful assistant."
                },
                # Set a user message for the assistant to respond to.
                {
                    "role": "user",
                    "content": prompt,
                }
            ],

            # The language model which will generate the completion.
            model="llama3-8b-8192",

            #
            # Optional parameters
            #

            # Controls randomness: lowering results in less random completions.
            # As the temperature approaches zero, the model will become deterministic
            # and repetitive.
            temperature=0.5,

            # The maximum number of tokens to generate. Requests can use up to
            # 32,768 tokens shared between prompt and completion.
            max_tokens=1024,

            # Controls diversity via nucleus sampling: 0.5 means half of all
            # likelihood-weighted options are considered.
            top_p=1,

            # A stop sequence is a predefined or user-specified text string that
            # signals an AI to stop generating content, ensuring its responses
            # remain focused and concise. Examples include punctuation marks and
            # markers like "[end]".
            stop=None,

            # If set, partial message deltas will be sent.
            stream=False,
        )

        # Print the completion returned by the LLM.
        bot_response = chat_completion.choices[0].message.content
        return {"response": bot_response, "status": status.HTTP_200_OK}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",reload=True)