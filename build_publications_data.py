import re
import json

with open('cv_text_extracted.txt', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('PUBLICATIONS (PEER-REVIEWED)')
end_idx = text.find('FORMAL PRESENTATIONS', start_idx)
pub_block = text[start_idx:end_idx]

# Pattern for 44 down to 1
items = re.findall(r'(\d+)\.\s+([\s\S]*?)(?=(?:\n\d+\.|\Z))', pub_block)

peer_reviewed = []
for num_str, content in items:
    num = int(num_str)
    if num > 44:
        continue
    clean = ' '.join(content.strip().split())
    # Clean text artifacts
    clean = clean.replace('\u2010', '-').replace('\u2013', '-').replace('\u2014', '-').replace('\u201c', '"').replace('\u201d', '"').replace('\u2018', "'").replace('\u2019', "'")
    clean = re.sub(r'=== PAGE \d+ ===', '', clean)
    
    # Year
    year_m = re.search(r'\b(19\d\d|20\d\d)\b', clean)
    year = year_m.group(1) if year_m else ""
    
    # Citations
    cites = 0
    cite_m = re.search(r'\*?Citations\s*=\s*(\d+)', clean, re.I)
    if cite_m:
        cites = int(cite_m.group(1))
    
    # Link or DOI
    link = ""
    link_m = re.search(r'(https?://[^\s,]+|doi:\s*[^\s,]+)', clean, re.I)
    if link_m:
        link = link_m.group(1).rstrip('.')
        if link.lower().startswith('doi:'):
            link = "https://doi.org/" + link.split(':', 1)[1].strip()

    peer_reviewed.append({
        "number": num,
        "citation": clean,
        "year": year,
        "citations": cites,
        "link": link
    })

# Sort descending by number
peer_reviewed.sort(key=lambda x: x["number"], reverse=True)

books = [
    {
        "id": "B1",
        "title": "Biomechanical response of the knee in sports injury scenarios",
        "citation": "Meyer EG, Haut RC. Biomechanical response of the knee in sports injury scenarios. Chapter in: Knee Joints: Kinematics, Injury Types and Treatment Options. Editor: Mascarenhas R. Nova Science Publishers, 2012. ISBN: 978-1-61942-268-1.",
        "year": "2012",
        "type": "Book Chapter",
        "link": "https://www.amazon.com/Knee-Concepts-Kinematics-Treatment-Functions/dp/1619422689"
    },
    {
        "id": "B2",
        "title": "Disruptive Biotechnology: Past and Future Promises of Biomedical Engineering and Wearables",
        "citation": "Meyer EG. Disruptive Biotechnology: Past and Future Promises of Biomedical Engineering and Wearables. LTU Research Day Presidential Colloquium Booklet. 2023. DOI: 10.13140/RG.2.2.21335.24484.",
        "year": "2023",
        "type": "Colloquium Monograph",
        "link": "http://dx.doi.org/10.13140/RG.2.2.21335.24484"
    }
]

output = {
    "stats": {
        "total_citations": 2890,
        "h_index": 25,
        "peer_reviewed_count": len(peer_reviewed),
        "books_count": len(books),
        "scholar_url": "http://scholar.google.com/citations?user=3SbYkskAAAAJ",
        "researchgate_url": "https://www.researchgate.net/profile/Eric-Meyer-9",
        "orcid_url": "https://orcid.org/0000-0002-7477-6050",
        "linkedin_url": "https://www.linkedin.com/in/eric-meyer-949a90b/"
    },
    "books": books,
    "publications": peer_reviewed
}

with open('publications_data.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2)

print(f"Generated clean publications_data.json with {len(peer_reviewed)} peer-reviewed papers and {len(books)} books!")
