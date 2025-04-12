# ⚡ Power System DAE Modeling and Simulation

This repository presents the modeling and simulation of a dynamic power system using **differential-algebraic equations (DAEs)**. The study focuses on a simplified electrical network composed of **3 synchronous generators** and **9 buses**, capturing transient system behavior and signal evolution. The work was originally developed as part of a seminar paper at the Faculty of Electrical Engineering, University of Sarajevo.

---

## 🧠 Project Overview

The core objective of this project is to simulate the transient response and dynamic characteristics of an electrical power system by:

- Formulating the system equations as a **set of DAEs**
- Encoding system topology and parameters in a **custom XML-based Model Solver**
- Performing **signal analysis in Python** using the generated simulation outputs

The project provides insight into how large-scale interconnected systems can be represented and analyzed using modern modeling techniques.

---

## 🧩 System Structure

- **3 synchronous generators**
  - Classical model with rotor dynamics and excitation systems
- **9 buses**
  - Interconnecting generators and loads with specified line parameters
- **Differential-algebraic equation formulation**
  - State variables: rotor angles, speeds, voltages
  - Algebraic constraints: network equations, bus admittance

---

## 🛠 Tools & Technologies

- ⚙️ **Custom XML Model Solver**
  - Used to encode system components, node topology, and simulation settings
- 🐍 **Python**
  - Signal post-processing
  - Visualization of generator response, frequency, and angle deviations
- 📊 **Plots**
  - Voltage, current, and angular velocity across the system over time

---

## 🎓 Academic Context

- **Course**: Power System Modeling and Analysis  
- **Authors**: Demir Hasičić, Jumna Alić
- **Institution**: Faculty of Electrical Engineering, University of Sarajevo  
- **Supervisor**: Prof. Dr. Izudin Džafić 
- **Date**: September 2023

---

## 📌 Outcome

The project successfully demonstrates:

- Construction of a dynamic model using differential-algebraic formulation
- Simulation of realistic multi-generator power systems
- Use of scripting tools (Python) for signal processing and analysis
- Application of academic theory in a custom-built modeling framework
