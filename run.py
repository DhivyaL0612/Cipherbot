from crewai import Crew, Process
from tasks import create_tasks
from agents import planner_agent, resource_agent, tutor_agent

def run_bot(topic: str):
    tasks = create_tasks(topic)
    crew = Crew(agents=[planner_agent, resource_agent, tutor_agent], tasks=tasks, process=Process.sequential, verbose=True)
    result = crew.kickoff()


    # If result is a dict or list, format it
    if isinstance(result, dict):
        return "\n\n".join([f"**{k}**:\n{v}" for k, v in result.items()])
    elif isinstance(result, list):
        return "\n\n".join(result)
    else:
        return str(result)
    


    
    
