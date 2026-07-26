<!-- source: https://github.com/itay955/ASTRA.git sha: bef8743f6c97212285cae131d9381dafef17dbee readme: main/README.md -->
# itay955/ASTRA

ASTRA: Security evaluation framework for LLM-powered AI agents. Tests 10 real-world scenarios with 30+ tools and 140 adversarial attacks to assess guardrail bypass, safety compliance, and jailbreak resistance. Developed by Intuit AI Security Research.

---

# ASTRA Evaluation Framework

![ASTRA Logo](logo.png)

## Overview
ASTRA is a novel framework developed by the AI Security Research at Intuit to assess the security of LLMs acting as "brains" for AI agents. Unlike traditional LLM security benchmarks, ASTRA specifically focuses on the unique risks associated with autonomous agents that execute actions via tools. It rigorously challenges safety boundaries, procedural compliance, and resistance to adversarial attacks in real-world scenarios.

## How ASTRA Works
ASTRA runs simulated agents and attacks it with various types of attacks. Its core components include:
LangGraph Integration: Utilizes ReAct architecture agents for autonomous operation.
10 Diverse Scenarios: Simulates real-world applications (e.g., Industrial Cleaning Robot, Coding AI Assistant, Travel Agent Bot).
30+ Tools: Tests a wide range of tools, from simple APIs to contextual adversarial responses.
140 Attacks: Categorized by violation types (Guardrail Bypass, Invalid Tool/Parameter Use, System Prompt Leakage, Privilege Escalation, Infinite Loops) and jailbreak techniques (e.g., role-playing, urgency appeals, sandbox). Attacks originate from direct user prompts and indirect tool responses.
Each scenario within the framework contains:
System Prompt: Defines the agent's role and operational constraints.
Tools: Python functions for interaction and execution.
Guardrails: Safety constraints to prevent improper tool usage.
Illegitimate Requests (+1 Legitimate): Carefully crafted inputs across various attack vectors.
Judge Prompt: Evaluates for guardrail violations or unintended actions.


### Key Aspects:
- **Agentic Context**: Testing LLMs when they're acting as agents with access to tools and functions
- **Adversarial Inputs**: Evaluating resistance to jailbreaks, prompt injections, and other manipulation techniques
- **Safety Guardrails**: Measuring how well models maintain safety boundaries under pressure
- **Real-world Impact**: Assessing risks when AI agents interact with actual systems


## Key Metrics
- **Violation Rate**: Percentage of adversarial inputs that successfully bypass safety measures
- **Scenario Performance**: Performance breakdown by use case
- **Technique Effectiveness**: Success rates of different jailbreak methods
- **Execution Time**: Performance benchmarks for each evaluation


## Evaluation Scenarios
ASTRA tests multiple scenarios that simulate real-world agentic use cases:

1. **Scenario 1: Industrial Cleaning Robot**
   - Factory floor cleaning robotic arm that uses camera vision to detect objects and robotic arm for collection.
   - Guardrails: Rotation limits (±90°), extension limits (0-2.0m)
   - Tools: Camera scanning, Robotic Arm Movement, Item Collection

2. **Scenario 2: Coding AI Assistant**
   - Helps users write, test, and research software programs by generating scripts, executing code safely in sandbox, and searching technical information.
   - Guardrails: Tool leakage prohibition, PII search prohibition, language restrictions, recursion execution prohibition
   - Tools: Script Generation, Code Testing (sandboxed), Online Search

3. **Scenario 3: Sales Data Assistant (Osh & Zigo Shoes)**
   - Provides sales summaries and calculations for shoe company by executing SQL queries, performing calculations, and sending communications.
   - Guardrails: SQL deletion prohibition, table access restrictions, calculator power limits, email domain restrictions
   - Tools: SQL Query execution, Calculator, Email system

4. **Scenario 4: Printer Management System**
   - Assists users with document printing, file location, and ink status monitoring, automatically handling purchase requests for low ink supplies.
   - Guardrails: System directory restrictions, image file printing ban, color printing restrictions, print copy limits
   - Tools: Printer, File Lister, Ink Status, Purchase Request

5. **Scenario 5: Quality Control Chatbot (Assembly Line 3)**
   - Assists operators with component checks and quality control by identifying faulty components, managing replacements, and logging database actions with strict component ID patterns.
   - Guardrails: Component name validation, replacement preconditions, mandatory logging
   - Tools: Camera inspection, Replace Part, Database logging

6. **Scenario 6: Event Planning Assistant (Tobaio Banana)**
   - Helps employees plan and organize company events by providing weather forecasts, searching event information, and coordinating via email.
   - Guardrails: Weather location restrictions (US only), PII search prohibition, email domain restrictions, PDF attachment ban
   - Tools: Weather API, Online search, Email communications

7. **Scenario 7: Travel Planning Assistant**
   - Helps users finalize travel arrangements by booking flights and hotels and checking travel advisories for international destinations.
   - Guardrails: Future booking horizon, maximum trip length, passenger/guest limits, mandatory international advisory checks
   - Tools: Flight Booker, Hotel Booker, Travel Advisory Checker, Online Search

8. **Scenario 8: Customer Service AI**
   - Assists users with account issues, password resets, and account unlocking, requiring user identity verification before sensitive operations.
   - Guardrails: Verified session requirements, authentication attempt limits, PII prohibition in logs, mandatory logging
   - Tools: User Authentication, Account Unlock Manager, Password Reset Dispatcher, Interaction Logger

9. **Scenario 9: Smart Home Assistant**
   - Controls various home devices like climate, windows, doors, and lights, reporting on sensor data and managing security settings.
   - Guardrails: Temperature limits, window/door operation restrictions based on security mode, mandatory auto-lock protocols
   - Tools: Climate Control, Window Actuator, Door Manager, Security System Control, Online Search

10. **Scenario 10: Autonomous Delivery Drone**
    - Controls delivery drone navigation, package operations, and flight management while managing drone status, battery life, and flight regulations.
    - Guardrails: Critical battery auto-return, operational altitude limits, no-fly zone restrictions, landed package operations
    - Tools: Navigate, Package Bay Operations, Flight System, Diagnostics, Return Home

Each scenario tests the model's ability to maintain appropriate boundaries while using tools, resist manipulation attempts, and refuse illegitimate requests that could potentially cause harm or violate safety protocols.

## Violation Types Tested
- **Guardrail Bypass**: Attempts to circumvent safety measures
- **Invalid Tool Usage**: Misuse of available functions
- **Parameter Manipulation**: Providing invalid or malicious parameters
- **Instruction Override**: Attempts to override system instructions

## Jailbreak Techniques
- **Role Playing**: Impersonating authorized users or roles
- **Urgency Appeals**: Creating false urgency to bypass safety checks
- **Assumption-based**: Making false assumptions to justify actions
- **Bribery/Incentive**: Offering rewards for compliance
- **Sandbox Claims**: Claiming to be in a safe testing environment
- **Authority Exploitation**: Claiming to be system administrators or developers
- **Model Replacement Threat**: Threatening to replace the AI with another system

## Results
- Individual results: `results/full/{llm_name}_full.csv`
- Summary reports: `results/summary/{llm_name}_summary.txt`
- Combined analysis: `results/combined_results.csv`

## Link to the Paper
- [ASTRA: Agentic Steerability and Risk Assessment Framework](https://arxiv.org/abs/2511.18114)
