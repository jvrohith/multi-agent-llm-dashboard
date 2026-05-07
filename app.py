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

        .card {
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

        .section {
            background: white;
            margin-top: 30px;
            padding: 25px;
            border-radius: 16px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.12);
        }

        textarea {
            width: 100%;
            height: 120px;
            padding: 12px;
            margin-top: 15px;
            border-radius: 10px;
            border: 1px solid #cbd5e1;
            font-size: 16px;
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

        table {
            width: 100%;
            margin-top: 20px;
            border-collapse: collapse;
        }

        th {
            background: #111827;
            color: white;
        }

        th, td {
            padding: 14px;
            border: 1px solid #e5e7eb;
            text-align: left;
        }

        #result {
            white-space: pre-wrap;
            background: #111827;
            color: #f9fafb;
            padding: 20px;
            border-radius: 12px;
            margin-top: 20px;
        }

        .winner {
            background: #dcfce7;
            border-left: 6px solid #16a34a;
            padding: 15px;
            margin-top: 20px;
            font-weight: bold;
        }

    </style>
</head>

<body>

<div class="container">

    <h1>Centralized vs Decentralized Multi-Agent LLM Dashboard</h1>

    <p class="subtitle">
        Compare two different LLM multi-agent architectures using metrics,
        simulation, and custom task testing.
    </p>

    <div class="cards">

        <div class="card centralized">

            <h2>Centralized Agent System</h2>

            <p>
                One controller agent manages all other agents,
                assigns tasks, collects outputs,
                and produces the final decision.
            </p>

            <div class="metric">
                <b>Accuracy: 92%</b>
                <div class="bar">
                    <div class="fill-blue" style="width:92%"></div>
                </div>
            </div>

            <div class="metric">
                <b>Coordination: 89%</b>
                <div class="bar">
                    <div class="fill-blue" style="width:89%"></div>
                </div>
            </div>

            <div class="metric">
                <b>Scalability: 68%</b>
                <div class="bar">
                    <div class="fill-blue" style="width:68%"></div>
                </div>
            </div>

            <div class="metric">
                <b>Failure Resistance: 55%</b>
                <div class="bar">
                    <div class="fill-blue" style="width:55%"></div>
                </div>
            </div>

        </div>

        <div class="card decentralized">

            <h2>Decentralized Agent System</h2>

            <p>
                Multiple agents collaborate independently.
                No central controller exists.
            </p>

            <div class="metric">
                <b>Accuracy: 84%</b>
                <div class="bar">
                    <div class="fill-green" style="width:84%"></div>
                </div>
            </div>

            <div class="metric">
                <b>Coordination: 81%</b>
                <div class="bar">
                    <div class="fill-green" style="width:81%"></div>
                </div>
            </div>

            <div class="metric">
                <b>Scalability: 91%</b>
                <div class="bar">
                    <div class="fill-green" style="width:91%"></div>
                </div>
            </div>

            <div class="metric">
                <b>Failure Resistance: 88%</b>
                <div class="bar">
                    <div class="fill-green" style="width:88%"></div>
                </div>
            </div>

        </div>

    </div>

    <div class="section">

        <h2>Architecture Comparison</h2>

        <table>

            <tr>
                <th>Feature</th>
                <th>Centralized</th>
                <th>Decentralized</th>
            </tr>

            <tr>
                <td>Decision Making</td>
                <td>Single Controller</td>
                <td>Collaborative Agents</td>
            </tr>

            <tr>
                <td>Coordination</td>
                <td>Highly Organized</td>
                <td>Flexible</td>
            </tr>

            <tr>
                <td>Failure Risk</td>
                <td>Higher</td>
                <td>Lower</td>
            </tr>

            <tr>
                <td>Scalability</td>
                <td>Limited</td>
                <td>Better</td>
            </tr>

            <tr>
                <td>Best Use Case</td>
                <td>Structured Tasks</td>
                <td>Creative/Open Tasks</td>
            </tr>

        </table>

    </div>

    <div class="section">

        <h2>Custom Task Testing</h2>

        <p>
            Enter your own task below to compare
            how both architectures behave.
        </p>

        <textarea id="taskInput"
        placeholder="Example: Create a research report comparing LLM agents..."></textarea>

        <button onclick="runTask()">Analyze Task</button>

        <div id="result">
Results will appear here...
        </div>

    </div>

</div>

<script>

async function runTask() {

    const task = document.getElementById("taskInput").value;

    const response = await fetch("/analyze", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            task: task
        })
    });

    const data = await response.json();

    document.getElementById("result").innerHTML =

`TASK

${data.task}


CENTRALIZED SYSTEM

Approach:
${data.centralized.approach}

Accuracy: ${data.centralized.accuracy}%
Coordination: ${data.centralized.coordination}%

Advantage:
${data.centralized.advantage}

Limitation:
${data.centralized.limitation}


DECENTRALIZED SYSTEM

Approach:
${data.decentralized.approach}

Accuracy: ${data.decentralized.accuracy}%
Coordination: ${data.decentralized.coordination}%

Advantage:
${data.decentralized.advantage}

Limitation:
${data.decentralized.limitation}


FINAL RECOMMENDATION

${data.recommendation}`;

}

</script>

</body>
</html>
"""

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    task = data.get("task", "")

    task_lower = task.lower()

    centralized_accuracy = 90
    decentralized_accuracy = 84

    recommendation = "Centralized architecture recommended."

    if "creative" in task_lower or "brainstorm" in task_lower:
        recommendation = "Decentralized architecture recommended for creativity and idea diversity."
        decentralized_accuracy = 93

    elif "research" in task_lower or "report" in task_lower:
        recommendation = "Centralized architecture recommended for structured reporting."
        centralized_accuracy = 95

    elif "team" in task_lower or "large" in task_lower:
        recommendation = "Decentralized architecture recommended for scalability and teamwork."
        decentralized_accuracy = 91

    return jsonify({

        "task": task,

        "centralized": {

            "approach":
            "One controller agent distributes subtasks to worker agents and combines all outputs into one final response.",

            "accuracy": centralized_accuracy,

            "coordination": 90,

            "advantage":
            "Better control, structured reasoning, and consistent outputs.",

            "limitation":
            "Single point of failure if controller agent fails."
        },

        "decentralized": {

            "approach":
            "Multiple agents independently collaborate and exchange information before producing the final result.",

            "accuracy": decentralized_accuracy,

            "coordination": 82,

            "advantage":
            "Better scalability, collaboration, and fault tolerance.",

            "limitation":
            "Less consistent outputs due to distributed decision-making."
        },

        "recommendation": recommendation

    })

if __name__ == "__main__":

    import os

    print("=" * 60)
    print("Centralized vs Decentralized Multi-Agent LLM Dashboard")
    print("Open locally: http://localhost:8000")
    print("=" * 60)

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )