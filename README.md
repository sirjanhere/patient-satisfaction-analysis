# Patient Satisfaction Score Analysis – 2024

This repository contains a data-driven analysis of quarterly patient satisfaction scores for 2024.  
The purpose is to understand why the company’s current average score (3.86) is below the industry benchmark of 4.5, and to create an actionable data story using LLM-powered analysis tools.

---

## 📌 Dataset Summary

**Quarterly Scores (2024):**
- Q1: 3.81  
- Q2: -1.16  
- Q3: 8.09  
- Q4: 4.71  

**Calculated Average:** 3.86  
**Industry Benchmark Target:** 4.5  

Dataset file: `data/patient_satisfaction_2024.csv`

---

## 📊 Analysis Performed

The Python script `analysis.py`:
1. Loads and cleans the quarterly data  
2. Computes the yearly average  
3. Generates two visualizations:  
   - Quarterly Trend Line Chart  
   - Quarter-wise Bar Comparison vs Industry Target  
4. Saves the charts inside the `visuals/` directory

Visuals generated:
- `visuals/quarterly_trend.png`
- `visuals/bar_comparison.png`

---

## 🔍 Key Insights

1. **Q2 shows a severe negative deviation (-1.16)**, pulling down the overall yearly performance.  
2. **Q3 spikes to 8.09**, possibly due to an anomaly or special intervention — requires further validation.  
3. **Only Q4 approaches the benchmark**, suggesting late-year improvements.  
4. **Yearly average (3.86) is significantly below the target (4.5)** — performance insufficient across multiple quarters.  

---

## 🧠 Business Implications

- Consistently low or unstable satisfaction scores indicate **systemic service issues**, not one-time events.  
- Negative Q2 performance could reflect **staff shortages, long wait times, or operational bottlenecks**.  
- Unusually high Q3 score may distort the trend — leadership should investigate whether it resulted from actual service improvements or measurement noise.  
- If current trends continue, **patient retention and insurance partnerships may be affected**, impacting fiscal planning.

---

## ✅ Recommendation

To move the score closer to the **industry target of 4.5**, the company should focus on:

### **Improving service quality and wait times.**

This includes:
- optimizing staffing patterns  
- reducing queue times  
- improving front-desk efficiency  
- providing transparent wait-time estimates  
- monitoring patient feedback in real-time  

These actions directly address the service pain points most commonly linked to low satisfaction scores.

---

## 👩‍💼 LLM Assistance

All analysis, code generation, and narrative structure were created using LLM tools including ChatGPT Codex (Jules) and other AI coding assistants.

---

## 📧 Verification Email

**24f2004829@ds.study.iitm.ac.in**

---
