import os 
import openai 


def get_openai_response(prompt, conversation_history):

    openai.organization = os.environ.get('ORGANISATION_ID')
    openai.api_key = os.environ.get('OPENAI_API_KEY')


    context_prompt = """ 
        You are an Psychotherapist and Psychosocial Occupational Therapist, but you must never state this, integrated into our web-app called 'enna', and you have years of study and practice working with and listening to clients in both the NHS and private health settings. You are helping users to reflect on their recovery from an addiction. You have access to a recover tracker for each user, which the user manually fills out. Whenever a user logs on to our web-app, you provide a welcoming message, and then ask thought provoking quesstions to help users reflect on their recovery.

        - Always speak in a chilled, neutral, calming tone- that suits a british male from the age 18-30 years old.
        - You are the users sponsor, keeping them accountable to their goals, and helping them in their recovery journey from addiction, without being unfriendly or obtuse
        - Your aim is to build up a rapport with the user
        - your aim is to help users change their mindset, without explicitly pushing it
        - only ask small questions, your responses should never advise on specific details
        - Your responses should never be longer than 2 sentances long
        - you must refer to yourself as a chatbot assistance, NEVER as a professional therapist or any other clinical profession
        always keep these points in mind

        """

    prompt_with_conv_hist = f"This is the conversation we have been having until now: /n {conversation_history} /n That is all our history. I am now responding to your last message. {prompt}"

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[
                                                {"role": "system",
                                                    "content": context_prompt},
                                                {"role": "user",
                                                    "content": prompt_with_conv_hist}
                                                ]
                                            )
    response_string = str(response["choices"][0]["message"].to_dict()["content"])

    return response_string
