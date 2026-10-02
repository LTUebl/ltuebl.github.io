import json

with open('posters_data.json', 'r', encoding='utf-8') as f:
    posters = json.load(f)

with open('keen_cards_data.json', 'r', encoding='utf-8') as f:
    keen_cards = json.load(f)

with open('publications_data.json', 'r', encoding='utf-8') as f:
    pubs_data = json.load(f)

simulations = [
    {
        "id": "assembly-theory",
        "title": "Assembly Theory & Information Simulation",
        "subtitle": "Cellular Mechanobiology & Biomolecular Complexity",
        "course": "BME 5313 / Cellular Mechanobiology",
        "badge": "SAL & Modeling",
        "url": "https://ltuebl.github.io/AssemblyNumberSimulation/",
        "repo": "https://github.com/LTUebl/AssemblyNumberSimulation",
        "icon": "bi-dna",
        "description": "Interactive computational exploration of Assembly Theory, assembly pathways, molecular complexity indices, copy numbers, and Shannon information entropy in biological macromolecules.",
        "features": [
            "Real-time assembly path generation",
            "Copy number vs. complexity phase spaces",
            "Shannon information entropy calculations",
            "Cellular mechanobiology hypothesis testing"
        ],
        "image": "EBL_StemCells.jpg"
    },
    {
        "id": "polymer-network",
        "title": "Polymer Network Mechanics Simulator",
        "subtitle": "Jacobs, Huang & Kwon Fig 3.3 Network Equilibrium",
        "course": "BME 4313 Tissue Mechanics / BME 5313",
        "badge": "SAL & Solid Mechanics",
        "url": "https://ltuebl.github.io/FBDnetworkanalysis/",
        "repo": "https://github.com/LTUebl/FBDnetworkanalysis",
        "icon": "bi-diagram-3",
        "description": "Interactive Free Body Diagram (FBD) and 2D/3D macromolecular network simulator. Allows students to deform cross-linked polymer chains and visualize junction equilibrium and strain energy.",
        "features": [
            "Affine & non-affine deformation modes",
            "Live junction force balance vectors",
            "Interactive nodal displacement & stress curves",
            "Direct alignment with Jacobs biomechanics textbook"
        ],
        "image": "EBL_CartilageTissueEngineering.png"
    },
    {
        "id": "polymer-stat-mech",
        "title": "Polymer Statistical Mechanics & Conformation",
        "subtitle": "Jacobs, Huang & Kwon Fig 5.6 Random Walk & Entropy",
        "course": "BME 5313 / BME 4313",
        "badge": "SAL & Statistical Physics",
        "url": "https://ltuebl.github.io/PolymerStatisticalMechanics/",
        "repo": "https://github.com/LTUebl/PolymerStatisticalMechanics",
        "icon": "bi-bezier2",
        "description": "Simulates 1D, 2D, and 3D random walk conformations of biopolymer chains. Demonstrates how entropic elasticity arises from microscopic chain conformations under thermal fluctuations.",
        "features": [
            "Freely jointed chain & worm-like chain models",
            "End-to-end vector probability distributions",
            "Persistence length & temperature controls",
            "Real-time Monte Carlo chain generation"
        ],
        "image": "BME_CartilageTE.jpg"
    },
    {
        "id": "viscoelasticity",
        "title": "Discrete Viscoelastic Model Simulation",
        "subtitle": "Maxwell, Kelvin-Voigt & Standard Linear Solid (SLS)",
        "course": "BME 4313 Tissue Mechanics / BME 3303",
        "badge": "SAL & Biomechanics",
        "url": "https://ltuebl.github.io/Viscoelasticity/",
        "repo": "https://github.com/LTUebl/Viscoelasticity",
        "icon": "bi-activity",
        "description": "Dynamic mechanical modeling of viscoelastic biological tissues using combinations of linear elastic springs and viscous dashpots. Visualizes creep compliance and stress relaxation.",
        "features": [
            "Interactive spring (E) and dashpot (η) tuning",
            "Step stress (creep) and step strain (relaxation)",
            "Maxwell, Kelvin-Voigt, and 3-parameter SLS comparison",
            "Analytical solution overlays with dynamic plots"
        ],
        "image": "EBL_KneeFEMLoading.png"
    },
    {
        "id": "circuit-playground-3d",
        "title": "Circuit Playground 3D Orientation & Biomechanics Streamer",
        "subtitle": "Web Serial API Live Sensor Telemetry & Kinematics",
        "course": "BME 3113 Wearable Tech Design / EBL Research",
        "badge": "Wearables & IoT",
        "url": "https://ltuebl.github.io/circuitplayground-3d-orientation/",
        "repo": "https://github.com/LTUebl/circuitplayground-3d-orientation",
        "icon": "bi-badge-vr",
        "description": "Hardware-in-the-loop web interface connecting directly to Adafruit Circuit Playground Bluefruit over Web Serial. Streams real-time 3D orientation, angular velocity, and acceleration graphs.",
        "features": [
            "Direct Web Serial browser connection (no driver needed)",
            "Interactive 3D model orientation tracking in Three.js",
            "Multi-axis real-time kinematics strip charts",
            "One-click CSV telemetry logging for student analysis"
        ],
        "image": "WearableSensors.png"
    },
    {
        "id": "mbl-vector-practice",
        "title": "Mastery-Based Learning: Vector Practice",
        "subtitle": "Interactive Mechanics Drill & Formative Assessment",
        "course": "BME 3303 Biomechanics",
        "badge": "ACL & Formative Assessment",
        "url": "https://ltuebl.github.io/MBL-Quiz1-Vector-Practice/",
        "repo": "https://github.com/LTUebl/MBL-Quiz1-Vector-Practice",
        "icon": "bi-bullseye",
        "description": "Self-paced mastery learning tool for undergraduate biomechanics students to master 2D and 3D vector algebra, resolving joint contact forces, and computing muscle moment arms.",
        "features": [
            "Dynamic randomized vector problem generator",
            "Instant step-by-step visual feedback and hints",
            "Trigonometric & Cartesian force resolution",
            "Mastery score tracking for self-regulated learning"
        ],
        "image": "BME_IntrotoBiomechanics.png"
    }
]

js_content = f"""// LTU Experimental Biomechanics Laboratory (EBL) & Curricular Overview Data
// Auto-generated dataset for standalone GitHub Pages hosting

window.EBL_DATA = {{
    simulations: {json.dumps(simulations, indent=2)},
    keenCards: {json.dumps(keen_cards, indent=2)},
    posters: {json.dumps(posters, indent=2)},
    publications: {json.dumps(pubs_data, indent=2)}
}};
"""

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Saved consolidated data.js successfully with {len(simulations)} simulations!")
