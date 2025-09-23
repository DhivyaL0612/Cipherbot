import os
import streamlit as st
from litellm import completion
from crewai import Agent
from tools import FormatCurriculumTool, SuggestResourcesTool, ExplainConceptTool

# Set Gemini API key from Streamlit secrets
os.environ["GEMINI_API_KEY"] = st.secrets["gemini_key"]

# LiteLLM wrapper to match CrewAI's expected LLM interface
class LiteLLMGeminiWrapper:
    def __init__(self, model_name="gemini/gemini-2.5-flash", temperature=0.7):
        self.model_name = model_name
        self.temperature = temperature
        self.system_prompt = {
            "role": "system",
            "content": (
                "You are a helpful educational assistant who provides structured learning guidance, "
                "suggests resources, and explains concepts clearly. Respond in markdown format."
            )
        }

    def run(self, prompt: str) -> str:
        response = completion(
            model=self.model_name,
            messages=[
                self.system_prompt,
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature
        )
        return response["choices"][0]["message"]["content"]

# Instantiate the Gemini LLM via LiteLLM
llm = LiteLLMGeminiWrapper(model_name="gemini/gemini-2.5-flash", temperature=0.7)

# Define CrewAI agents with LiteLLM Gemini and tools
planner_agent = Agent(
    role="Curriculum Planner",
    goal="Design a structured curriculum for any topic",
    backstory="Expert in instructional design and education.",
    tools=[FormatCurriculumTool()],
    verbose=True,
    llm=llm
)

resource_agent = Agent(
    role="Resource Finder",
    goal="Find useful learning resources for any topic",
    backstory="Knows where to find the best tutorials and courses.",
    tools=[SuggestResourcesTool()],
    verbose=True,
    llm=llm
)

tutor_agent = Agent(
    role="Tutor",
    goal="Explain concepts in simple terms",
    backstory="Experienced teacher who simplifies complex ideas.",
    tools=[ExplainConceptTool()],
    verbose=True,
    llm=llm
)
