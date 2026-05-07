"""
Evaluation Runner — Centralized vs Decentralized Multi-Agent LLM
"""

from centralized_system   import run_centralized_system
from decentralized_system import run_decentralized_system

TASKS = [
    "Design a study plan for learning machine learning in 30 days.",
    "Create a strategy to launch a new mobile app with a small budget.",
    "Outline a multi-step plan for software system architecture design.",
]


def run_evaluation(tasks: list = None) -> dict:
    if tasks is None:
        tasks = TASKS

    results = []
    for task in tasks:
        c = _safe_run(run_centralized_system,   task)
        d = _safe_run(run_decentralized_system, task)
        results.append({"task": task, "centralized": c, "decentralized": d})

    c_times   = [r["centralized"]["time"]   for r in results]
    d_times   = [r["decentralized"]["time"] for r in results]
    c_success = sum(1 for r in results if r["centralized"]["success"])
    d_success = sum(1 for r in results if r["decentralized"]["success"])

    return {
        "results": results,
        "summary": {
            "tasks_total":     len(tasks),
            "c_success":       c_success,
            "d_success":       d_success,
            "c_avg_time":      round(sum(c_times) / len(c_times), 2),
            "d_avg_time":      round(sum(d_times) / len(d_times), 2),
            "c_has_controller": True,
            "d_has_controller": False,
            "c_peer_to_peer":   False,
            "d_peer_to_peer":   True,
            "c_failure_point":  True,
            "d_failure_point":  False,
        }
    }


def _safe_run(fn, task: str) -> dict:
    try:
        return fn(task)
    except Exception as e:
        return {"success": False, "time": 0, "final": str(e), "steps": []}


if __name__ == "__main__":
    data = run_evaluation()
    s = data["summary"]
    print(f"Centralized  — success: {s['c_success']}/{s['tasks_total']}  avg time: {s['c_avg_time']}s")
    print(f"Decentralized — success: {s['d_success']}/{s['tasks_total']}  avg time: {s['d_avg_time']}s")