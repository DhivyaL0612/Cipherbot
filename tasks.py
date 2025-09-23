from crewai import Task
from agents import planner_agent, resource_agent, tutor_agent

def create_tasks(topic: str):
    task1 = Task(
        description=f"Create a curriculum for learning {topic}.",
        agent=planner_agent,
        expected_output="A structured curriculum outline."
    )

    task2 = Task(
        description=f"Find resources to learn {topic}.",
        agent=resource_agent,
        expected_output="List of useful links and platforms."
    )

    task3 = Task(
        description=f"Explain the key concept of {topic} in simple terms.",
        agent=tutor_agent,
        expected_output="Simple explanation of the topic."
    )

    return [task1, task2, task3]
