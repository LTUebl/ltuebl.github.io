# LTU Experimental Biomechanics Laboratory (EBL) & Curricular Innovation Overview

This repository hosts the public overview website for the **LTU Experimental Biomechanics Laboratory (EBL)** and **Wearable Technology Innovation Center (WTIC)**, directed by **Dr. Eric G. Meyer, PhD**, Associate Professor of Biomedical Engineering at [Lawrence Technological University](https://www.ltu.edu).

Live Website: **[https://ltuebl.github.io/](https://ltuebl.github.io/)**

---

## 🌟 Key Features

1. **Curricular Pillars (Teaching Philosophy):**
   - **SAL (Simulation Active Learning):** Interactive computational models, discrete mechanics, and cellular mechanobiology sandboxes.
   - **EML (Entrepreneurial Minded Learning):** Integrating KEEN 3Cs (*Curiosity, Connections, Creating Value*) and Quantified Self (*QS4EML*) across core engineering courses.
   - **ACL / PBL (Active Collaborative Learning & Project-Based Learning):** Studio-style design experiences, multidisciplinary teamwork, and client-sponsored projects (e.g., Lear Corporation).
   - **Innovation & Emerging Technologies:** Open-source biomedical hardware, Explainable AI for engineering education (KNC 2026), and Edge AI computer vision.

2. **Interactive Live Web Simulations (6 LTUebl GitHub Apps):**
   - **Assembly Theory & Information Simulation** (`https://ltuebl.github.io/AssemblyNumberSimulation/`)
   - **Polymer Network Mechanics Simulator** (`https://ltuebl.github.io/FBDnetworkanalysis/`)
   - **Polymer Statistical Mechanics & Conformation Simulator** (`https://ltuebl.github.io/PolymerStatisticalMechanics/`)
   - **Discrete Viscoelastic Model Simulation** (`https://ltuebl.github.io/Viscoelasticity/`)
   - **Circuit Playground 3D Orientation & Biomechanics Streamer** (`https://ltuebl.github.io/circuitplayground-3d-orientation/`)
   - **Mastery-Based Learning: Vector Practice** (`https://ltuebl.github.io/MBL-Quiz1-Vector-Practice/`)

3. **Published KEEN Module Cards (Engineering Unleashed):**
   - Direct showcase of **23 peer-reviewed teaching module cards** with over **1,961+ peer educator engagements**.
   - Prominently highlights **Card #5823** (*Biomedical Engineering Essential Skills*), **Card #5797** (*KNC 2026 Explainable AI for Educators*), and popular modules like **Card #1449** (365 engagements) and **Card #684** (330 engagements).
   - Real-time search and topic filters (Quantified Self, AI & Innovation, Biomechanics, Wearables, Surgical Simulation).

4. **Research & Student Design Posters Gallery (36 Posters):**
   - Interactive gallery containing 36 undergraduate capstone, graduate thesis, and faculty research posters.
   - High-resolution thumbnails with instant zoomable preview modal and direct PDF downloads.
   - Categorized by Wearables & Sensing, Biomechanics & Injury, Orthopedics & Implants, Senior Capstone Design, and EML & Pedagogy.

5. **State-of-the-Art Research Facilities:**
   - **Experimental Biomechanics Laboratory (EBL - Taubman Complex J134):** 10-camera Vicon optical motion capture, dual Kistler force platforms, 16-channel wireless Delsys Trigno EMG/accelerometers, drop tower, materials testing, and FEBio computational biomechanics.
   - **Wearable Technology Innovation Center (WTIC):** Wearable sensors, robotics, and multi-year industry collaboration with Lear Corporation.

6. **Peer-Reviewed Publications & Scholarship:**
   - 44 Peer-reviewed journal articles and proceedings (>2,890 citations, h-index 25).
   - 2 Books / Monographs.
   - Direct links to Google Scholar, ResearchGate, ORCID, and publisher DOIs.

7. **Institutional & Professional Connections:**
   - Direct links to LTU Faculty Profile, LTU Biomedical Engineering Department, Engineering Unleashed, Trinity College Dublin Centre for Bioengineering, and Michigan State University Orthopaedic Biomechanics Laboratories.

---

## 📁 Repository Structure

```
├── index.html                   # Main overview website landing page
├── styles.css                   # Custom responsive styling, LTU branding & dark/light theme
├── app.js                       # Interactive filters, search logic, and modal viewer handlers
├── data.js                      # Consolidated data for simulations, KEEN cards, posters & pubs
├── posters_thumbs/              # Web-optimized preview images for all 36 research posters
├── Posters/                     # High-resolution PDF posters (viewable and downloadable)
├── KEEN/                        # KEEN module card spreadsheets, presentations, and guides
├── MeyerCV2026.pdf              # Full academic curriculum vitae (2026)
├── MeyerFacultyProfile.pdf      # LTU faculty profile highlight
├── LTU_BME_EBL_Brochure.pdf     # LTU BME & EBL lab facility brochure
└── README.md                    # Repository documentation
```

---

## 🚀 GitHub Pages Deployment

To publish this website through the **LTUebl** GitHub account:
1. Push this folder to your repository (e.g. `LTUebl/ltuebl.github.io` for the organization root page, or `LTUebl/overview` or `LTUebl/EBL`).
2. Go to **Settings > Pages** in your GitHub repository.
3. Under **Branch**, select `main` and root directory (`/`).
4. Click **Save**. The website will be live automatically at:
   - `https://ltuebl.github.io/` (if named `ltuebl.github.io`) or
   - `https://ltuebl.github.io/<repo-name>/`
