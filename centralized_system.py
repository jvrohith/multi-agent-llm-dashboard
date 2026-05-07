"""
Centralized Multi-Agent LLM System
====================================
Architecture: Central Controller → Planner → Executor → Reviewer
"""

import time
import random


def mock_llm_call(agent_name: str, prompt: str) -> str:
    time.sleep(0.4)
    responses = {
        "Planner": [
            "Step 1: Understand the core problem. Step 2: Break it into 3 subtasks. Step 3: Assign subtasks to Executor for execution.",
            "Plan: Analyze input → Generate solution steps → Validate approach → Execute sequentially with checkpoints.",
        ],
        "Executor": [
            "Executed the plan. Output: Task completed successfully with structured reasoning applied to each step.",
            "Execution done. Result: Applied systematic logic to each subtask and produced a validated answer.",
        ],
        "Reviewer": [
            "Review passed. The output is accurate, well-structured, and meets all requirements.",
            "Review complete. Minor improvements noted, but overall the solution is correct and consistent.",
        ],
        "Controller": [
            "Controller: All agents reported. Aggregating results. Final output is consistent and complete.",
            "Controller: Task pipeline complete. No conflicts detected. Sending final validated response.",
        ],
    }
    options = responses.get(agent_name, ["Agent processed the task."])
    return random.choice(options)


class CentralController:
    def __init__(self):
        self.name = "Controller"
        self.log = []
        self.steps = []

    def assign_task(self, task: str, agent) -> str:
        self.log.append(f"Assigning task to {agent.name}")
        result = agent.run(task)
        self.steps.append({
            "from": self.name,
            "to": agent.name,
            "message": task[:80],
            "result": result
        })
        return result

    def collect_result(self, result: str) -> str:
        summary = mock_llm_call(self.name, result)
        self.steps.append({
            "from": self.name,
            "to": "Output",
            "message": result[:80],
            "result": summary
        })
        return summary


class PlannerAgent:
    def __init__(self):
        self.name = "Planner"

    def run(self, task: str) -> str:
        return mock_llm_call(self.name, task)


class ExecutorAgent:
    def __init__(self):
        self.name = "Executor"

    def run(self, plan: str) -> str:
        return mock_llm_call(self.name, plan)


class ReviewerAgent:
    def __init__(self):
        self.name = "Reviewer"

    def run(self, result: str) -> str:
        return mock_llm_call(self.name, result)


def run_centralized_system(task: str) -> dict:
    start = time.time()
    controller = CentralController()
    planner    = PlannerAgent()
    executor   = ExecutorAgent()
    reviewer   = ReviewerAgent()

    plan   = controller.assign_task(task, planner)
    result = controller.assign_task(plan, executor)
    review = controller.assign_task(result, reviewer)
    final  = controller.collect_result(review)

    return {
        "system":  "Centralized",
        "task":    task,
        "final":   final,
        "steps":   controller.steps,
        "time":    round(time.time() - start, 2),
        "success": True,
        "log":     controller.log,
    }


if __name__ == "__main__":
    r = run_centralized_system("Design a study plan for learning machine learning in 30 days.")
    print("FINAL:", r["final"])