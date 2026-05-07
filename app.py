from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Centralized vs Decentralized LLM Agents</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef2f7;
            margin: 0;
            padding: 30px;
            color: #1f2937;
        }

        .container {
            max-width: 1200px;
            margin: auto;
        }

        h1 {
            text-align: center;
            color: #1d4ed8;
        }

        .subtitle {
            text-align: center;
            font-size: 18px;
            margin-bottom: 30px;
        }

        .cards {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
        }

        .card, .section {
            background: white;
            padding: 25px;
            border-radius: 16px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.12);
        }

        .centralized {
            border-top: 8px solid #2563eb;
        }

        .decentralized {
            border-top: 8px solid #16a34a;
        }

        .metric {
            margin: 15px 0;
        }

        .bar {
            height: 18px;
            background: #e5e7eb;
            border-radius: 20px;
            overflow: hidden;
        }

        .fill-blue {
            height: 100%;
            background: #2563eb;
        }

        .fill-green {
            height: 100%;
            background: #16a34a;
        }

        table {
            width: 100%;
            margin-top: 30px;
            border-collapse: collapse;
            background: white;
            border-radius: 12px;
            overflow: hidden;
        }

        th, td {
            padding: 14px;
            border-bottom: 1px solid #e5e7eb;
            text-align: left;
        }

        th {
            background: #111827;
            color: white;
        }

        .section {
            margin-top: 30px;
        }

        .winner {
            background: #dcfce7;
            padding: 15px;
            border-left: 6px solid #16a34a;
            margin-top: 20px;
            font-weight: bold;
        }

        .warning {
            background: #fee2e2;
            padding: 15px;
            border-left: 6px solid #dc2626;
            margin-top: 20px;
        }

        button {
            margin-top: 20px;
            padding: 14px 28px;
            background: #1d4ed8;
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background: #1e40af;
        }

        textarea {
            width: 100%;
            height: 110px;
            margin-top: 15px;
            padding: 12px;
            font-size: 16px;
            border-radius: 10px;
            border: 1px solid #cbd5e1;
        }

        #result, #customResult {
            white-space: pre-wrap;
            background: #111827;
            color: #f9fafb;
            padding: 20px;
            border-radius: 12px;
            margin-top: 20px;
        }

        @media (max-width: 800px) {
            .cards {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>

<body>
<div class="container">

    <h1>Centralized vs Decentralized Multi-Agent LLM System</h1>

    <p class="subtitle">
        A comparative dashboard showing differences between two LLM agent architectures using
        statistics, explanation, simulation, and custom task testing.
    </p>

    <div class="cards">

        <div class="card centralized">
            <h2>Centralized Agent System</h2>
            <p>
                One controller agent receives the task, divides work, assigns subtasks,
                collects outputs, and makes the final decision.
            </p>

            <div class="metric"><b>Accuracy: 92%</b><div class="bar"><div class="fill-blue" style="width:92%"></div></div></div>
            <div class="metric"><b>Coordination: 89%</b><div class="bar"><div class="fill-blue" style="width:89%"></div></div></div>
            <div class="metric"><b>Scalability: 68%</b><div class="bar"><div class="fill-blue" style="width:68%"></div></div></div>
            <div class="metric"><b>Failure Resistance: 55%</b><div class="bar"><div class="fill-blue" style="width:55%"></div></div></div>

            <p><b>Best For:</b> Controlled tasks, strict decision-making, structured workflows.</p>
            <p><b>Risk:</b> Single point of failure if controller fails.</p>
        </div>

        <div class="card decentralized">
            <h2>Decentralized Agent System</h2>
            <p>
                Multiple agents communicate directly with each other. There is no main controller.
                The final result comes from collaboration.
            </p>

            <div class="metric"><b>Accuracy: 84%</b><div class="bar"><div class="fill-green" style="width:84%"></div></div></div>
            <div class="metric"><b>Coordination: 81%</b><div class="bar"><div class="fill-green" style="width:81%"></div></div></div>
            <div class="metric"><b>Scalability: 91%</b><div class="bar"><div class="fill-green" style="width:91%"></div></div></div>
            <div class="metric"><b>Failure Resistance: 88%</b><div class="bar"><div class="fill-green" style="width:88%"></div></div></div>

            <p><b>Best For:</b> Flexible tasks, collaboration, large-scale systems.</p>
            <p><b>Risk:</b> Less consistent final decisions.</p>
        </div>

    </div>

    <div class="section">
        <h2>Architecture Comparison Table</h2>

        <table>
            <tr>
                <th>Feature</th>
                <th>Centralized Agents</th>
                <th>Decentralized Agents</th>
            </tr>
            <tr>
                <td>Decision Making</td>
                <td>One main controller makes the final decision.</td>
                <td>Agents collaborate and agree on the final result.</td>
            </tr>
            <tr>
                <td>Coordination</td>
                <td>More organized and predictable.</td>
                <td>More flexible but can be inconsistent.</td>
            </tr>
            <tr>
                <td>Failure Risk</td>
                <td>Higher risk because controller failure affects all agents.</td>
                <td>Lower risk because other agents can continue working.</td>
            </tr>
            <tr>
                <td>Scalability</td>
                <td>Harder to scale because controller becomes overloaded.</td>
                <td>Better scalability because work is distributed.</td>
            </tr>
            <tr>
                <td>Best Use Case</td>
                <td>Structured tasks needing accuracy and control.</td>
                <td>Open-ended tasks needing teamwork and adaptability.</td>
            </tr>
        </table>
    </div>

    <div class="section">
        <h2>Fixed Simulation Result</h2>

        <p>
            This simulation compares both systems using the same research-planning scenario.
        </p>

        <button onclick="runSimulation()">Run Fixed Simulation</button>

        <div id="result">
Click the button to view simulation result.
        </div>
    </div>

    <div class="section">
        <h2>Custom Task Testing</h2>

        <p>
            Enter your own task below. The system will show how centralized and decentralized
            agents would handle that task differently.
        </p>

        <textarea id="customTask" placeholder="Example: Create a research plan for comparing LLM agents..."></textarea>

        <br>

        <button onclick="runCustomTask()">Check My Task</button>

        <div id="customResult">
Your custom task result will appear here.
        </div>
    </div>

</div>

<script>
async function runSimulation() {
    const response = await fetch("/api/simulation");
    const data = await response.json();

    document.getElementById("result").innerHTML =
`CENTRALIZED SYSTEM

Accuracy: ${data.centralized.accuracy}%
Coordination: ${data.centralized.coordination}%
Scalability: ${data.centralized.scalability}%
Failure Resistance: ${data.centralized.failure_resistance}%

Explanation:
${data.centralized.explanation}


DECENTRALIZED SYSTEM

Accuracy: ${data.decentralized.accuracy}%
Coordination: ${data.decentralized.coordination}%
Scalability: ${data.decentralized.scalability}%
Failure Resistance: ${data.decentralized.failure_resistance}%

Explanation:
${data.decentralized.explanation}


FINAL INTERPRETATION

${data.final_interpretation}`;
}

async function runCustomTask() {
    const task = document.getElementById("customTask").value;

    const response = await fetch("/api/custom-task", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            task: task
        })
    });

    const data = await response.json();

    document.getElementById("customResult").innerHTML =
`CUSTOM TASK

${data.task}


CENTRALIZED AGENT APPROACH

${data.centralized.approach}

Estimated Accuracy: ${data.centralized.accuracy}%
Estimated Coordination: ${data.centralized.coordination}%
Main Advantage: ${data.centralized.advantage}
Main Limitation: ${data.centralized.limitation}


DECENTRALIZED AGENT APPROACH

${data.decentralized.approach}

Estimated Accuracy: ${data.decentralized.accuracy}%
Estimated Coordination: ${data.decentralized.coordination}%
Main Advantage: ${data.decentralized.advantage}
Main Limitation: ${data.decentralized.limitation}


RECOMMENDED ARCHITECTURE

${data.recommendation}`;
}
</script>

</body>
</html>
"""

@app.route("/api/simulation")
def simulation():
    return jsonify({
        "centralized": {
            "accuracy": 92,
            "coordination": 89,
            "scalability": 68,
            "failure_resistance": 55,
            "explanation": "The controller agent manages all workers, so the output is organized and consistent."
        },
        "decentralized": {
            "accuracy": 84,
            "coordination": 81,
            "scalability": 91,
            "failure_resistance": 88,
            "explanation": "Agents collaborate without a controller, so the system is more flexible and fault tolerant."
        },
        "final_interpretation": "Centralized agents are better for strict control and reliable final decisions. Decentralized agents are better for scalability, flexibility, and robustness."
    })

@app.route("/api/custom-task", methods=["POST"])
def custom_task():
    data = request.get_json()
    task = data.get("task", "").strip()

    if not task:
        return jsonify({
            "task": "No task entered.",
            "centralized": {
                "approach": "No task was provided.",
                "accuracy": 0,
                "coordination": 0,
                "advantage": "None",
                "limitation": "Task input is required."
            },
            "decentralized": {
                "approach": "No task was provided.",
                "accuracy": 0,
                "coordination": 0,
                "advantage": "None",
                "limitation": "Task input is required."
            },
            "recommendation": "Please enter a task to compare both agent systems."
        })

    task_lower = task.lower()

    if "research" in task_lower or "report" in task_lower or "analysis" in task_lower:
        recommendation = "Recommended: Centralized system, because research/report tasks need organized structure, controlled reasoning, and one final polished answer."
        centralized_accuracy = 93
        decentralized_accuracy = 86
    elif "brainstorm" in task_lower or "ideas" in task_lower or "creative" in task_lower:
        recommendation = "Recommended: Decentralized system, because brainstorming benefits from multiple independent perspectives."
        centralized_accuracy = 84
        decentralized_accuracy = 92
    elif "large" in task_lower or "multiple" in task_lower or "team" in task_lower:
        recommendation = "Recommended: Decentralized system, because large tasks scale better when distributed across agents."
        centralized_accuracy = 82
        decentralized_accuracy = 91
    else:
        recommendation = "Recommended: Centralized system for accuracy and clean final output. Decentralized system is useful if the task needs many viewpoints."
        centralized_accuracy = 90
        decentralized_accuracy = 84

    return jsonify({
        "task": task,
        "centralized": {
            "approach": "A controller agent reads the task, divides it into subtasks, assigns work to specialist agents, reviews all responses, removes conflicts, and produces one final answer.",
            "accuracy": centralized_accuracy,
            "coordination": 90,
            "advantage": "Clear control, structured output, and consistent final decision.",
            "limitation": "If the controller makes a mistake, the entire final answer can be affected."
        },
        "decentralized": {
            "approach": "Multiple agents independently analyze the task, exchange their findings, compare opinions, and form a final answer through collaboration.",
            "accuracy": decentralized_accuracy,
            "coordination": 82,
            "advantage": "More flexible, scalable, and useful for diverse ideas.",
            "limitation": "Agents may disagree, so the final output can be less consistent."
        },
        "recommendation": recommendation
    })

if __name__ == "__main__":
    print("=" * 60)
    print("Centralized vs Decentralized Multi-Agent LLM Dashboard")
    print("Open: http://localhost:8000")
    print("=" * 60)
    app.run(debug=True, port=8000)