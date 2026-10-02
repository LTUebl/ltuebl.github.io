import os
import json
import re

with open('posters_debug.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Let's map each poster to accurate metadata based on the file contents and context
posters_meta = []

# Specific curate mapping for each file
details_map = {
    "2021Lear_poster.pdf": {
        "title": "Integrated Sensor Comfort System 2.0",
        "authors": "Elizabeth Beckmon, Sophia Judge, Samantha Weber, Bailey Wills",
        "advisors": "Dr. Eric G. Meyer, Dr. Pan Zagorski (Lear Corporation)",
        "year": "2021",
        "category": "Wearables & Sensing",
        "venue": "BME Capstone / Lear Corporation Partnership",
        "description": "Integration of Adafruit triaxial accelerometers and pressure sensor mapping with MATLAB to quantify automotive seat comfort, vibration transmissibility, and robotic compression testing."
    },
    "ACL Injury Prevention Poster BMES.pdf": {
        "title": "Novel Design of an Anterior Cruciate Ligament (ACL) Injury Prevention Brace",
        "authors": "D. Greenshields, R. Porter, J. Killewald, E.G. Meyer",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2014",
        "category": "Biomechanics & Injury",
        "venue": "BMES Annual Meeting, San Antonio, TX",
        "description": "Biomechanical design of a multi-planar knee brace hinge incorporating valgus bending protection and internal rotation damping to mitigate non-contact ACL tear mechanisms."
    },
    "ASB2025_Impact360Poster.pdf": {
        "title": "Impact360: Real-Time Head Impact Kinematics & Concussion Risk Telemetry",
        "authors": "EBL Sensor Research Group, E.G. Meyer",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2025",
        "category": "Wearables & Sensing",
        "venue": "American Society of Biomechanics (ASB)",
        "description": "Wireless IMU sensor system measuring linear acceleration and angular velocity with real-time severity classification algorithms and mobile dashboard telemetry."
    },
    "ASBPoster_FAST2025.pdf": {
        "title": "Fast Acting Concussion Evaluator (F.A.C.E): From Symptoms to Stats",
        "authors": "Daniela Scagnetti, Jeffry Fuhrmann, Sydney Robinson, Amber Drvodelic, Eric G. Meyer PhD",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2025",
        "category": "Senior Capstone Design",
        "venue": "American Society of Biomechanics (ASB 2025)",
        "description": "Portable multimodal clinical assessment station for tracking adolescent concussion recovery through objective reaction time, sensory feedback, and balance kinematics."
    },
    "ASEE2014KeenPoster.pdf": {
        "title": "Fostering the Entrepreneurial Mindset through 'Quantified-Self' Multidisciplinary Learning Modules",
        "authors": "Dr. Eric G. Meyer, Dr. Mansoor Nasir",
        "advisors": "Kern Entrepreneurial Engineering Network (KEEN)",
        "year": "2014",
        "category": "EML & Pedagogy",
        "venue": "ASEE Annual Conference",
        "description": "Pedagogical implementation of Quantified Self (QS4EML) active learning modules connecting wearable sensors, physiological metrics, and entrepreneurial mindset across engineering curricula."
    },
    "ASEE2015 Poster.pdf": {
        "title": "Providing Diverse Opportunities for Capstone Projects in Biomedical Engineering",
        "authors": "Dr. Eric G. Meyer, Dr. Mansoor Nasir",
        "advisors": "Lawrence Technological University",
        "year": "2015",
        "category": "EML & Pedagogy",
        "venue": "ASEE Annual Conference",
        "description": "Framework for entrepreneurial project-based learning and industry-sponsored multidisciplinary capstone design sequences in undergraduate BME."
    },
    "AUTO-Trac Poster2015.pdf": {
        "title": "AUTO-Trac: Automated Tracking and Kinematics in High-Impact Testing",
        "authors": "EBL Biomechanics Research Team, Eric G. Meyer PhD",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2015",
        "category": "Biomechanics & Injury",
        "venue": "LTU Research Day / Biomechanics Colloquium",
        "description": "High-speed optical tracking system calibration and 3D kinematics analysis for dynamic automotive and athletic impact scenarios."
    },
    "BMECapstone_Poster2018.pdf": {
        "title": "A Knee Movement Monitoring Wearable Device for Rehabilitation",
        "authors": "Alexis Snider, Evan Szabo, Dr. Eric Meyer",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2018",
        "category": "Senior Capstone Design",
        "venue": "BME Senior Capstone / LTU Research Day",
        "description": "Smart knee sleeve embedded with flexible stretch sensors and IMUs for tracking joint range of motion, squat biomechanics, and postoperative rehabilitation compliance."
    },
    "CapstoneS2024FinalPosterCVsecurity.pdf": {
        "title": "Healthcare Worker Violence Prevention: Computer Vision and Wearable Duress System",
        "authors": "Sophia Buckberger, Keith Kolaczyk, Gabrielle Pryor",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2024",
        "category": "Senior Capstone Design",
        "venue": "BME Senior Capstone Design Showcase",
        "description": "Computer vision and wearable alert device utilizing Edge AI and sensor fusion to protect clinical healthcare professionals from workplace physical violence."
    },
    "CarolinMinners Poster_ResearchDay.pdf": {
        "title": "Golf Swing Biomechanics: Instrumented Grip Force & Kinematic Telemetry",
        "authors": "Carolin Minners, Eric G. Meyer PhD",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2023",
        "category": "Wearables & Sensing",
        "venue": "LTU Research Day",
        "description": "Integration of flex-force pressure sensors and inertial measurement units on golf clubs to quantify grip kinetics, club head velocity, and kinematic sequencing."
    },
    "Denture Study Poster.pdf": {
        "title": "Finite Element Analysis of Maxillary Implant-Supported Overdentures",
        "authors": "EBL Dental Research Group, E.G. Meyer PhD",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2014",
        "category": "Orthopedics & Implants",
        "venue": "Biomedical Engineering Society (BMES)",
        "description": "Comparative 3D FEA stress distribution analysis across cortical bone, cancellous bone, and titanium abutments under masticatory physiological bite loads."
    },
    "DesignPrototypinginBME_PosterBMES2017.pdf": {
        "title": "Practicing Design and Prototyping in Biomedical Engineering Programs",
        "authors": "Eric G. Meyer and Mansoor Nasir",
        "advisors": "Lawrence Technological University",
        "year": "2017",
        "category": "EML & Pedagogy",
        "venue": "BMES Annual Meeting 2017, Phoenix, AZ",
        "description": "Curricular model for embedding rapid 3D prototyping, microcontroller programming, and entrepreneurial ideation into undergraduate bioinstrumentation."
    },
    "EBLSensorSystemPoster.pdf": {
        "title": "Hybrid Motion Tracking: Optical MoCap & Wireless Inertial Sensor Data Fusion",
        "authors": "Experimental Biomechanics Laboratory Team, E.G. Meyer PhD",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2019",
        "category": "Wearables & Sensing",
        "venue": "EBL Research Colloquium",
        "description": "Development of a unified sensor fusion pipeline coupling 10-camera Vicon optical motion capture with wireless Delsys IMUs to eliminate occlusion and sensor drift."
    },
    "EPIC Poster_Capstone2012.pdf": {
        "title": "High Resolution Imaging of Intervertebral Disc Degeneration using EPIC-microCT",
        "authors": "Olesya Motovylyak, Michael Newton, Eric G. Meyer PhD",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2012",
        "category": "Orthopedics & Implants",
        "venue": "BME Senior Capstone Showcase",
        "description": "Equilibrium partitioning of an ionic contrast agent micro-CT (EPIC-microCT) to map sulfated glycosaminoglycan (sGAG) distribution in lumbar disc degeneration."
    },
    "LearCapstonPoster2022.pdf": {
        "title": "Lear Comfort System: Automated Seating Ergonomics & Pressure Profiling",
        "authors": "Lucas Adams, Adam Knapp, Samantha Nseir, Andrew Ulaszek",
        "advisors": "Dr. Eric G. Meyer, Dr. Pan-Zagorski (Lear Corp)",
        "year": "2022",
        "category": "Senior Capstone Design",
        "venue": "BME Capstone / Lear Corporation Showcase",
        "description": "Robotic indentor sensor array and capacitive pressure map modeling to assess automotive seating pressure distribution and fatigue alleviation."
    },
    "Magic_Mirror_ResearchDay2025.pdf": {
        "title": "Magic Mirror: Interactive Computer Vision Rehabilitation Display",
        "authors": "EBL Interactive Vision Research Team, Eric G. Meyer PhD",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2025",
        "category": "Wearables & Sensing",
        "venue": "LTU Research Day 2025",
        "description": "Smart display mirror using AI pose estimation (MediaPipe / OpenCap) for real-time visual biofeedback during post-stroke and orthopedic physical therapy exercises."
    },
    "Mechanical Testing of a Spinal Fusion System.pdf": {
        "title": "Biomechanical Testing of a Spinal Fusion System Under Multiaxial Fatigue",
        "authors": "Ryan Reed, Eric G. Meyer, Ph.D",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2016",
        "category": "Orthopedics & Implants",
        "venue": "EBL Orthopedics Research Showcase",
        "description": "Static and dynamic multi-axial cyclic loading tests of spinal pedicle screw-rod fixation systems following ASTM F1717 standard protocols."
    },
    "Meyer_ASB2025_SustainabilityBiomechanicsPoster.pdf": {
        "title": "Sustainability & Entrepreneurial Mindset in Biomechanics Education",
        "authors": "Eric G. Meyer PhD",
        "advisors": "American Society of Biomechanics (ASB)",
        "year": "2025",
        "category": "EML & Pedagogy",
        "venue": "American Society of Biomechanics (ASB 2025)",
        "description": "Embedding sustainable circular design principles, open-source sensor hardware, and KEEN entrepreneurial modules into undergraduate biomechanics laboratories."
    },
    "Meyer_WCB2014_Poster.pdf": {
        "title": "Tibiofemoral Joint Compression and Valgus Rotation in Non-Contact ACL Failure",
        "authors": "Eric G. Meyer, Roger C. Haut",
        "advisors": "World Congress of Biomechanics",
        "year": "2014",
        "category": "Biomechanics & Injury",
        "venue": "7th World Congress of Biomechanics (WCB), Boston, MA",
        "description": "Dynamic in vitro knee joint impact simulations showing that valgus bending dramatically lowers the compressive threshold needed to cause acute ACL rupture."
    },
    "Meyer_WCB2018_Poster.pdf": {
        "title": "Computational and Experimental Modeling of Impact Attenuation in Sports Surfaces",
        "authors": "Eric G. Meyer PhD, EBL Sports Biomechanics Group",
        "advisors": "World Congress of Biomechanics",
        "year": "2018",
        "category": "Biomechanics & Injury",
        "venue": "8th World Congress of Biomechanics (WCB), Dublin, Ireland",
        "description": "Dynamic drop-tower impact tests and non-linear viscoelastic lumped parameter models evaluating turf stiffness, rotational traction, and lower limb injury hazards."
    },
    "MOA_2011.pdf": {
        "title": "Mechanism of Injury in a High Ankle Sprain: A Cadaveric Biomechanics Study",
        "authors": "Joel M. Post, Feng Wei, Jerrod E. Braman, Eric G. Meyer, John W. Powell, Roger C. Haut",
        "advisors": "MSU Orthopaedic Biomechanics / LTU EBL",
        "year": "2011",
        "category": "Biomechanics & Injury",
        "venue": "Michigan Orthopaedic Association (MOA) Annual Meeting",
        "description": "External rotation and axial compression loading experiments measuring syndesmotic ligament strain and interosseous membrane failure in syndesmosis ankle injuries."
    },
    "Open2015 Poster_EGM.pdf": {
        "title": "Entrepreneurship in Small Doses: Integrating EML Modules Across BME Courses",
        "authors": "Mansoor Nasir PhD, Eric G. Meyer PhD",
        "advisors": "VentureWell OPEN Conference",
        "year": "2015",
        "category": "EML & Pedagogy",
        "venue": "VentureWell OPEN Conference, Washington DC",
        "description": "Modular pedagogy introducing value proposition design, customer discovery, and prototyping into traditional technical engineering courses without displacing core content."
    },
    "ORS2006Poster.pdf": {
        "title": "Tibiofemoral Joint Compression Limits and Meniscal Load Sharing in Knee Injury",
        "authors": "Eric G. Meyer, Roger C. Haut",
        "advisors": "Orthopaedic Research Society (ORS)",
        "year": "2006",
        "category": "Biomechanics & Injury",
        "venue": "52nd Orthopaedic Research Society (ORS), Chicago, IL",
        "description": "Fundamental biomechanical thresholds of human knee joint subchondral microfracture and ACL avulsion under rapid blunt axial compressive loading."
    },
    "RabbitACLPoster.pdf": {
        "title": "Joint Responses to Surgical Transection vs. Traumatic Rupture of the ACL in a Rabbit Model",
        "authors": "Eric G. Meyer, Roger C. Haut",
        "advisors": "ASME Summer Bioengineering Conference",
        "year": "2014",
        "category": "Biomechanics & Injury",
        "venue": "ASME SBC / Orthopedic Research Forum",
        "description": "Comparison of post-traumatic osteoarthritis progression following surgical cutting versus closed mechanical traumatic rupture of the ACL."
    },
    "Reseach Day 2023_OpenCap.pdf": {
        "title": "Validation of OpenCap Markerless Motion Capture vs. Optical Motion Tracking",
        "authors": "EBL Biomechanics Research Group, Eric G. Meyer PhD",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2023",
        "category": "Wearables & Sensing",
        "venue": "LTU Research Day 2023",
        "description": "Quantifying the kinematic accuracy of multi-camera smartphone markerless AI video tracking (OpenCap) compared to 10-camera optical Vicon tracking during gait and jump squats."
    },
    "ResearchDayPoster KneeSleeveWearable.pdf": {
        "title": "A Knee Movement Monitoring Wearable Device for Real-Time Joint Telemetry",
        "authors": "Alexis Snider, Evan Szabo, Eric G. Meyer PhD",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2019",
        "category": "Wearables & Sensing",
        "venue": "LTU Research Day 2019",
        "description": "Design and microcontroller implementation of a wearable knee sleeve using resistive bend sensors to monitor flexion angle and prevent post-operative reinjury."
    },
    "Rossman_SB3C2022_Poster.pdf": {
        "title": "Risk of Recurrent Disc Herniation Following Decompression Surgery: Finite Element Analysis",
        "authors": "Samantha Rossman, Eric G. Meyer, Shaon Rundell",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2022",
        "category": "Orthopedics & Implants",
        "venue": "SB3C Summer Biomechanics, Bioengineering & Biotransport Conf",
        "description": "Parametric non-linear finite element model of L4-L5 lumbar functional spinal unit predicting anulus fibrosus stress concentrations after surgical sequestrectomy and discectomy."
    },
    "SB3C_lear2021_Poster.pdf": {
        "title": "Quantifying Long-Term Seating Comfort: Shear and Pressure Transmissibility",
        "authors": "E. Beckmon, S. Judge, S. Weber, B. Wills, E.G. Meyer, P. Zagorski",
        "advisors": "Dr. Eric G. Meyer, Lear Corp",
        "year": "2021",
        "category": "Wearables & Sensing",
        "venue": "SB3C Summer Biomechanics Conference 2021",
        "description": "Novel instrumentation combining shear sensor arrays with triaxial accelerometers to replace subjective human comfort surveys with objective biomechanical metrics."
    },
    "Salvatore Brauer EMG Sensor Poster 2023_EGM1.pdf": {
        "title": "Wireless Surface EMG Sensor System for Targeted Muscular Rehabilitation",
        "authors": "Salvatore Brauer, Eric G. Meyer PhD",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2023",
        "category": "Wearables & Sensing",
        "venue": "LTU Research Day 2023",
        "description": "Real-time surface electromyography monitoring to assess neuromuscular activation patterns and assist patients suffering from muscle degenerative pathologies."
    },
    "Senior Project Poster 2017_Edema.pdf": {
        "title": "Reducing Edema One Foot at a Time: Active Intermittent Compression Therapy",
        "authors": "Rania Anoni, Samantha Wheeler",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2017",
        "category": "Senior Capstone Design",
        "venue": "BME Senior Capstone Showcase",
        "description": "Wearable pneumatic compression boot engineered to stimulate peripheral venous return, reduce lower limb edema, and prevent deep vein thrombosis in bedridden patients."
    },
    "Senior Projects Poster2015.pdf": {
        "title": "Fold-and-Go Knee Scooter for Increased Single Leg Mobility and Independence",
        "authors": "K. Mozurkewich, N. Colarossi, M. Issa",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2015",
        "category": "Senior Capstone Design",
        "venue": "BME Senior Capstone Showcase",
        "description": "Ergonomic, lightweight folding mobility scooter engineered with adjustable knee rest suspension and dual brake steering for non-weight bearing lower limb rehabilitation."
    },
    "Senior-Project-Poster2017_Seating.pdf": {
        "title": "BT Racing Solutions: Tackling Driver Track Fatigue Through Ergonomic Racing Seats",
        "authors": "BME Motorsports Capstone Team",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2017",
        "category": "Senior Capstone Design",
        "venue": "BME Senior Capstone Showcase",
        "description": "Driver cockpit ergonomics, vibration isolation, and customized foam density geometry to minimize lumbar spinal compression during high-G track cornering."
    },
    "Shimokochi et al. 2012 ESSKA Poster.pdf": {
        "title": "Modulating Sagittal Landing Styles Alters Tibiofemoral Force Vector Directions",
        "authors": "Yohei Shimokochi, Jatin P. Ambegaonkar, Eric G. Meyer",
        "advisors": "ESSKA Congress",
        "year": "2012",
        "category": "Biomechanics & Injury",
        "venue": "15th ESSKA Congress, Geneva, Switzerland",
        "description": "Kinematic and ground reaction force analysis showing that forefoot soft landings alter the direction and magnitude of tibiofemoral joint reaction forces to protect the ACL."
    },
    "ShoulderX Final Poster_SeniorProjects.pdf": {
        "title": "ShoulderX: Dynamic Resistance & Rotator Cuff Rehabilitation Device",
        "authors": "BME Senior Capstone Design Team",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2017",
        "category": "Senior Capstone Design",
        "venue": "BME Senior Capstone Showcase",
        "description": "Rehabilitation harness utilizing calibrated elastic resistance bands and angle-guided tracks for post-operative rotator cuff strengthening and range of motion recovery."
    },
    "WalkLift-Poster-2016.pdf": {
        "title": "Walk&Lift Cane: Sit-to-Stand Assistive Device for Mobility Impaired Seniors",
        "authors": "Alexandria Glumb, Fatimah Aljafer",
        "advisors": "Dr. Eric Meyer, Dr. Mansoor Nasir",
        "year": "2016",
        "category": "Senior Capstone Design",
        "venue": "BME Senior Capstone Showcase",
        "description": "Ergonomic dual-handle cane with an integrated lever assist mechanism designed to decrease knee and hip joint torques during sit-to-stand transitions."
    },
    "WashMeyer_MSBME_ResearchDay2022_WearableIMU_Poster.pdf": {
        "title": "Integrating Wireless Wearable IMUs with OpenSim Biomechanical Musculoskeletal Modeling",
        "authors": "Joshua Wash, Eric G. Meyer PhD",
        "advisors": "Dr. Eric G. Meyer",
        "year": "2022",
        "category": "Wearables & Sensing",
        "venue": "LTU Research Day / MS BME Thesis Presentation",
        "description": "Validation pipeline coupling wearable inertial sensor orientation kinematics with OpenSim inverse dynamics models to evaluate joint moments without laboratory camera constraints."
    }
}

final_posters = []
for p in items:
    fn = p['filename']
    det = details_map.get(fn, {})
    final_posters.append({
        "id": p['id'],
        "filename": fn,
        "title": det.get("title", p['title']),
        "authors": det.get("authors", "LTU Biomedical Engineering"),
        "advisors": det.get("advisors", "Dr. Eric G. Meyer"),
        "year": det.get("year", "2022"),
        "category": det.get("category", "Biomechanics & Sensing"),
        "venue": det.get("venue", "LTU Research Day / Conference Showcase"),
        "description": det.get("description", "Experimental biomechanics and wearable engineering research at Lawrence Tech."),
        "pdf": f"Posters/{fn}",
        "thumbnail": f"posters_thumbs/{os.path.splitext(fn)[0]}.jpg"
    })

with open('posters_data.json', 'w', encoding='utf-8') as f:
    json.dump(final_posters, f, indent=2)

print('Successfully created posters_data.json with', len(final_posters), 'posters!')
