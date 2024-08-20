import os
from getpass import getpass

# Setting up API key for GROQ
tokenGROQ = getpass('Enter GROQ_API_KEY here: ')
os.environ["GROQ_API_KEY"] = tokenGROQ