# Real-Time-Activation-Space-Anomaly-Detection-for-LLM

## 1. Project Overview
**Real-Time-Activation-Space-Anomaly-Detection-for-LLM** is an advanced security firewall designed to protect Large Language Models (LLMs) and intelligent classifiers against sophisticated adversarial exploits, prompt injections, and jailbreak attempts. Instead of relying solely on surface-level text filtering (which can easily be bypassed through lexical obfuscation or token manipulation), this system monitors the **internal neural network activations (hidden states)** of transformer models in real time to detect semantic and distributional anomalies during inference.

---

## 2. Problem Statement
Traditional security measures for LLMs depend on pattern-matching, blocklists, and keyword filters at the input layer. However, malicious actors frequently evade these filters by encoding malicious payloads in base64, using semantic paraphrasing, or executing multi-turn jailbreak scenarios. 

* **The Core Vulnerability:** Surface-level text inspection ignores the internal representation of intent inside the neural network. 
* **The Solution:** By analyzing deep latent representations (hidden-layer tensor states), this project intercepts malicious prompts before they trigger harmful model generations, bridging the gap between automated machine learning defense and runtime cybersecurity enforcement.

---

## 3. The Three Core Perspectives

### Perspective A: Deep Learning
* **Mechanism:** Intercepts forward passes in transformer-based architectures using neural hooks.
* **Execution:** Extracts high-dimensional hidden-state tensors from the final transformer layers, performing mean-pooling across token sequences to capture the complete semantic embedding of the input prompt.

### Perspective B: Natural Language Processing (NLP)
* **Mechanism:** Evaluates semantic intent and contextual feature shifts rather than rigid keyword strings.
* **Execution:** Identifies how adversarial prompts manipulate the vector space compared to standard, normative linguistic distributions in human-LLM interactions.

### Perspective C: Machine Learning & Cybersecurity
* **Mechanism:** Implements unsupervised anomaly detection (Isolation Forests / One-Class SVMs) trained on baseline benign prompt distributions.
* **Execution:** Acts as a real-time runtime security guard, computing anomaly scores and out-of-distribution distance metrics to instantly flag and block unauthorized execution paths.

---

## 4. System Architecture

```text
+-----------------------+      +---------------------------+      +-----------------------------+
| User Prompt Input     | ---> | Hugging Face Transformer  | ---> | Hidden State Tensor Extraction|
| (Web UI / API Gateway)|      | (Feature Extractor Engine)|      | (Final Layer Mean Pooling)  |
+-----------------------+      +---------------------------+      +-----------------------------+
                                                                                 |
                                                                                 v
+-----------------------+      +---------------------------+      +-----------------------------+
| Security Verdict      | <--- | Isolation Forest Classifier| <--- | Latent Feature Vector Space |
| (Safe vs. Threat)     |      | (Anomaly Scoring Engine)  |      | (Numerical Vector Matrix)   |
+-----------------------+      +---------------------------+      +-----------------------------+
