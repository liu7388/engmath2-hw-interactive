# engmath2-hw-interactive

## 📌 Project Overview
This repository contains an interactive web application developed for the **Engineering Mathematics (II) — AI-Assisted Homework Assignment (Track 3: Visual & Interactive Learning Tools)**. 

The core objective of this project is to provide a dynamic, visual simulator for the **1D Heat Equation** using Fourier Sine Series. Built with Python and `Streamlit`, this tool allows users to input custom initial temperature distributions, adjust physical parameters, and observe the real-time thermal diffusion process. It serves as an intuitive educational tool to bridge complex mathematical concepts with visual physics.

* 🌐 **Live Demo (Streamlit Cloud)**: [Click here to launch the interactive simulator](https://engmath2-hw-interactive-dqprhzzvjshjwenhxavitu.streamlit.app/)
* 📑 **Detailed Homework Report (HackMD)**: [Click here to view my full Engineering Mathematics report](https://hackmd.io/@QENvl1H2S7C_KP9TKmSJIA/SJvyBc5bfl)

---

## 📂 Project Structure

The directory structure of this repository is organized as follows to ensure seamless deployment and readability:

```text
engmath2-hw-interactive/
├── .streamlit/
│   └── config.toml        # Enforces the premium dark theme for optimal heatmap visualization
├── app.py                 # Core Streamlit application and mathematical logic
├── requirements.txt       # Python dependencies (Streamlit, NumPy, Matplotlib)
└── README.md              # This documentation file
```

## 📊 Core Features & Mathematical Concepts
### 1. Dynamic Fourier Series Expansion
* **Objective**: Visualize how arbitrary initial temperature distributions $f(x)$ are approximated using a finite number of sine waves.
* **Methodology**: The application utilizes numerical integration (Trapezoidal rule via NumPy) to dynamically compute Fourier coefficients $B_n$ based on user-defined mathematical strings (e.g., step functions or Gaussian distributions).
* **Key Observations**: By playing the "Terms ($N$)" animation, users can visually observe the series convergence and clearly identify the Gibbs phenomenon (overshoot) near the discontinuities of a square wave.

### 2. Thermal Diffusion Simulation
* **Objective**: Understand the time evolution of the 1D Heat Equation: $u_t = c \cdot u_{xx}$.
* **Methodology**: Implements the analytical solution:
$$u(x,t) = \sum_{n=1}^{N} B_n \sin\left(\frac{n\pi x}{L}\right) e^{-c \left(\frac{n\pi}{L}\right)^2 t}$$
* **Key Observations**: By animating the "Time ($t$)" and adjusting the Diffusion Coefficient ($c$), users can intuitively grasp how high-frequency terms decay exponentially faster than low-frequency terms due to the exponential decay factor, resulting in the rapid smoothing of the temperature curve.

## 🛠️ Quick Start & Environment Setup
To clone this project and run the interactive simulator locally, follow these steps:

### 1. Clone the Repository
* **Objective**: Obtain a local copy of the source code. 
* **Methodology**: Use Git to clone the repository and navigate into the project directory.

**Execution Command:**
```bash
git clone https://github.com/liu7388/engmath2-hw-interactive.git
cd engmath2-hw-interactive
``` 

### 2. Install Dependencies
Ensure you have Python 3.8+ installed, then install the required core computing libraries:

**Execution Command**:
```bash
pip install -r requirements.txt
``` 


### 3. Run the Streamlit Application
Execute the Streamlit framework to launch the local web server and interact with the application.

**Execution Command**:
```bash
streamlit run app.py
``` 
(This will automatically open a new tab in your default web browser pointing to http://localhost:8501)