from crewai.tools import BaseTool

class FormatCurriculumTool(BaseTool):
    name: str = "format_curriculum"
    description: str = "Formats a topic into a basic curriculum outline."

    def _run(self, topic: str) -> str:
        steps = [
            f"1. Introduction to {topic}",
            f"2. Key concepts in {topic}",
            f"3. Practical applications of {topic}",
            f"4. Advanced topics in {topic}",
            f"5. Summary and revision"
        ]
        return "\n".join(steps)


class SuggestResourcesTool(BaseTool):
    name: str = "suggest_resources"
    description: str = "Suggests generic online resources for a given topic."

    def _run(self, topic: str) -> str:
        resources = [
            f"https://www.khanacademy.org/search?page_search_query={topic}",
            f"https://www.coursera.org/search?query={topic}",
            f"https://www.youtube.com/results?search_query={topic}+tutorial",
            f"https://www.geeksforgeeks.org/?s={topic}"
        ]
        return "\n".join(resources)


class ExplainConceptTool(BaseTool):
    name: str = "explain_concept"
    description: str = "Provides a simple explanation for a concept."

    def _run(self, concept: str) -> str:
        return f"{concept} is a fundamental idea in its domain. To understand it, start with basic definitions, explore examples, and relate it to real-world applications."
