# 🚀 EventFlow — Intelligent Crowd Experience Assistant

**EventFlow** is a lightweight, decision-support system designed to optimize real-world event experiences. By simulating crowd density and behavioral patterns, it provides visitors with actionable intelligence on where to go, when to move, and what to avoid.

---

## 🧠 The Problem
Large-scale physical events (concerts, expos, sports) suffer from **"Flash Crowds"**—sudden spikes in density that lead to long wait times, safety hazards, and visitor frustration. Current solutions often focus on tracking; **EventFlow AI focuses on guidance.**

## ✨ Key Features
* **Intent-Based Interaction:** Tailored suggestions for Food, Washrooms, Exploration, and Exits.
* **Rule-Based Crowd Simulation:** A sophisticated logic engine that models peak hours and hotspot density without requiring expensive hardware sensors.
* **AI-Generated Guidance:** Integrates **Google Gemini** to transform raw data into human-friendly, empathetic advice.
* **Glassmorphism UI:** A modern, responsive, and accessible interface built with Vanilla JS for maximum performance.

## 🛠️ Tech Stack
| Layer | Technology |
| :--- | :--- |
| **Frontend** | HTML5, CSS3 (Glassmorphism), Vanilla JavaScript |
| **Backend** | Python, FastAPI |
| **AI Engine** | Google Gemini Pro |
| **Database** | Firebase Realtime Database (Lightweight) |
| **DevOps** | Git, AntiGravity IDE |

---

## 📂 Project Structure
```text
EventFlow/
├── backend/
│   ├── main.py          # FastAPI Entry Point
│   ├── logic.py         # Crowd Simulation Engine
│   ├── config.py        # Event Metadata & Zone Config
│   └── __init__.py
├── frontend/
│   ├── index.html       # Responsive UI
│   ├── style.css        # Glassmorphism Styling
│   └── app.js           # API Integration logic
├── .env                 # Environment Variables (Secrets)
└── README.md            # You are here