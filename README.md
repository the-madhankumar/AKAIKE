# CSV BOT

## Problem Statement
  You are tasked with building a lightweight AI agent that can intelligently answer basic questions from a simple CSV file containing customer purchase data or any client data.
  The agent should be able to:
  Parse the CSV file.
  Understand simple user queries in natural language.
  Perform appropriate data lookups and respond with correct answers.

## Data Agent Responsibilites
    -> Able to upload the csv data.
    -> and it must get the analysis out of it.

## Technical Requirements 
     Frontend - streamlit 
     Backend (Routes integration) - Flask 
     Input - Natural language query.
     Output - Text answer based on CSV data.
     Api Providers - Groq
     llm used - llama3-8b-8192

## Approach
    - The backend will have two queries `upload` and `query`
  
