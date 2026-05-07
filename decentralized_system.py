"""
Decentralized Multi-Agent LLM System
=======================================
Architecture: Peer-to-peer via MessageBus — no central controller.
"""

import time
import random


def mock_llm_call(agent_name: str, prompt: str) -> str:
    time.sleep(0.4)
    responses = {
        "Planner": [
            "Decentralized plan: Break problem into 3 parallel subtasks. Executor handles each independently.",
            "Plan (autonomous): Identified key steps. No controller needed — passing directly to Executor.",
        ],
        "Executor": [
            "Autonomous execution complete. Result: Generated a multi-step solution without controller guidance.",
            "Executed independently. Output is ready for peer review by Reviewer agent.",
        ],
        "Reviewer": [
            "Peer review done. Sending feedback directly to Planner for iteration if needed.",
            "Review passed. Result is valid. Flagging one potential inconsistency for Planner awareness.",
        ],
    }
    options = responses.get(agent_name, ["Agent processed the task autonomously."])
    return random.choice(options)


class MessageBus:
    """Shared peer-to-peer message channel — no controller involved."""

    def __init__(self):
        self._messages: list[dict] = []
        self.history:   list[dict] = []

    def send(self, sender: str, recipient: str, content: str):
        entry = {"from": sender, "to": recipient, "content": content}
        self._messages.append(entry)
        self.history.append(entry)

    def receive(self, recipient: str) -> list[dict]:
        msgs = [m for m in self._messages if m["to"] == recipient]
        self._messages = [m for m in self._messages if m["to"] != recipient]
        return msgs


class AutonomousAgent:
    """Agent that communicates directly with peers. No permissions needed."""

    def __init__(self, name: str, bus: MessageBus):
        self.name = name
        self.bus  = bus

    def run(self, task: str, send_to: str) -> str:
        response = mock_llm_call(self.name, task)
        self.bus.send(self.name, send_to, response)
        return response


def run_decentralized_system(task: str) -> dict:
    start = time.time()
    bus      = MessageBus()
    planner  = AutonomousAgent("Planner",  bus)
    executor = AutonomousAgent("Executor", bus)
    reviewer = AutonomousAgent("Reviewer", bus)

    planner.run(task, send_to="Executor")

    inbox = bus.receive("Executor")
    plan  = inbox[0]["content"] if inbox else task
    executor.run(plan, send_to="Reviewer")

    inbox  = bus.receive("Reviewer")
    result = inbox[0]["content"] if inbox else plan
    review = reviewer.run(result, send_to="Planner")

    feedback   = bus.receive("Planner")
    fb_content = feedback[0]["content"] if feedback else ""

    return {
        "system":   "Decentralized",
        "task":     task,
        "final":    review,
        "steps":    bus.history,
        "time":     round(time.time() - start, 2),
        "success":  True,
        "feedback": fb_content,
    }


if __name__ == "__main__":
    r = run_decentralized_system("Design a study plan for learning machine learning in 30 days.")
    print("FINAL:", r["final"])