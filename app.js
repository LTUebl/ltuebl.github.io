// LTU Experimental Biomechanics Laboratory (EBL) Overview Website App Script
// Interactive rendering, filtering, searching, and preview modals

document.addEventListener('DOMContentLoaded', () => {
  const data = window.EBL_DATA || {};
  
  // Theme Toggle
  initTheme();
  
  // Render Dynamic Sections
  renderSimulations(data.simulations || []);
  renderKeenCards(data.keenCards || []);
  renderPosters(data.posters || []);
  renderPublications(data.publications || {});
  
  // Initialize Filter & Search Listeners
  initFiltersAndSearch();
  
  // Initialize Modals
  initModals();
  
  // Initialize Smooth Scrolling & Tab Navigation
  initNavigation();
});

// Theme Management
function initTheme() {
  const themeToggle = document.getElementById('themeToggle');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const savedTheme = localStorage.getItem('ebl_theme') || (prefersDark ? 'dark' : 'light');
  
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);
  
  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('ebl_theme', next);
      updateThemeIcon(next);
    });
  }
}

function updateThemeIcon(theme) {
  const btn = document.getElementById('themeToggle');
  if (!btn) return;
  btn.innerHTML = theme === 'dark' 
    ? '<i class="bi bi-sun-fill" title="Switch to light mode"></i>' 
    : '<i class="bi bi-moon-stars-fill" title="Switch to dark mode"></i>';
}

// Render Interactive Simulations
function renderSimulations(sims) {
  const container = document.getElementById('simulationsGrid');
  if (!container) return;
  
  container.innerHTML = sims.map(sim => `
    <article class="sim-card" data-id="${sim.id}" data-category="${sim.category || 'all'}">
      <div class="sim-card-image" style="background:#FFFFFF;">
        <img src="${sim.image}" alt="${sim.title}" loading="lazy" style="background:#FFFFFF; object-fit:contain;" onerror="this.src='EBL_Home.png'">
        <span class="sim-card-badge">${sim.badge}</span>
      </div>
      <div class="sim-card-content">
        <span class="sim-course-tag">${sim.course}</span>
        <h3 class="sim-title">${sim.title}</h3>
        <h4 class="sim-subtitle">${sim.subtitle}</h4>
        <p class="sim-desc">${sim.description}</p>
        
        <ul class="sim-features-list">
          ${sim.features.map(f => `<li><i class="bi bi-check2-circle"></i> ${f}</li>`).join('')}
        </ul>
        
        <div class="sim-actions">
          <a href="${sim.url}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm">
            <i class="bi bi-box-arrow-up-right"></i> Launch Simulation
          </a>
          <button type="button" class="btn btn-outline btn-sm preview-sim-btn" data-url="${sim.url}" data-title="${sim.title}" data-repo="${sim.repo}">
            <i class="bi bi-play-circle"></i> Embed Preview
          </button>
          <a href="${sim.repo}" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm" title="View Source on GitHub">
            <i class="bi bi-github"></i>
          </a>
        </div>
      </div>
    </article>
  `).join('');
}

// Render KEEN Cards
function renderKeenCards(cards) {
  const container = document.getElementById('keenCardsGrid');
  if (!container) return;
  
  container.innerHTML = cards.map(c => `
    <article class="keen-card ${c.featured ? 'featured-card' : ''}" data-category="${c.category}" data-id="${c.id}">
      <div class="keen-card-header">
        <span class="keen-card-num"><i class="bi bi-card-heading"></i> Card #${c.id}</span>
        <span class="keen-card-badge">${c.category}</span>
      </div>
      <h3 class="keen-card-title">${c.title}</h3>
      <div class="keen-card-course"><i class="bi bi-journal-bookmark"></i> ${c.courses}</div>
      <p class="keen-card-desc">${c.description}</p>
      <div class="keen-card-footer">
        <span class="keen-engagement" title="${c.engagements} peer educator engagements">
          <i class="bi bi-heart-fill"></i> ${c.engagements} Engagements
        </span>
        <a href="${c.url}" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">
          <span>View on KEEN</span> <i class="bi bi-arrow-up-right"></i>
        </a>
      </div>
    </article>
  `).join('');
}

// Render Posters
function renderPosters(posters) {
  const container = document.getElementById('postersGrid');
  if (!container) return;
  
  container.innerHTML = posters.map(p => `
    <article class="poster-card" data-category="${p.category}" data-id="${p.id}">
      <div class="poster-thumbnail-wrap" onclick="openPosterModal('${p.id}')" style="background:#FFFFFF;">
        <img src="${p.thumbnail}" alt="${p.title}" loading="lazy" style="background:#FFFFFF; object-fit:contain;" onerror="this.src='EBL_Research.png'">
        <div class="poster-hover-overlay">
          <button type="button" class="poster-overlay-btn" onclick="event.stopPropagation(); openPosterModal('${p.id}')">
            <i class="bi bi-eye"></i> Quick Preview
          </button>
          <a href="${p.pdf}" target="_blank" class="poster-overlay-btn" onclick="event.stopPropagation()">
            <i class="bi bi-file-earmark-pdf"></i> View PDF
          </a>
        </div>
      </div>
      <div class="poster-content">
        <div class="poster-meta-row">
          <span class="poster-category-badge">${p.category}</span>
          <span class="poster-year">${p.year}</span>
        </div>
        <h3 class="poster-title">${p.title}</h3>
        <p class="poster-authors"><i class="bi bi-people"></i> ${p.authors}</p>
        <p class="poster-venue"><i class="bi bi-geo-alt"></i> ${p.venue}</p>
        <p class="poster-desc">${p.description}</p>
        
        <div class="poster-footer">
          <button type="button" class="btn btn-outline btn-sm" onclick="openPosterModal('${p.id}')">
            <i class="bi bi-zoom-in"></i> Preview Poster
          </button>
          <a href="${p.pdf}" download class="btn btn-primary btn-sm" title="Download Poster PDF">
            <i class="bi bi-download"></i> Download PDF
          </a>
        </div>
      </div>
    </article>
  `).join('');
}

// Render Publications with Verified CV Links
function renderPublications(pubsObj) {
  const container = document.getElementById('publicationsList');
  if (!container) return;
  
  const pubs = pubsObj.publications || [];
  const books = pubsObj.books || [];
  
  let html = '';
  
  // Books & Monograph Highlight
  if (books.length > 0) {
    html += `
      <div style="margin-bottom: 24px;">
        <h4 style="font-size: 1.15rem; margin-bottom: 14px; color: var(--primary);">
          <i class="bi bi-book-half"></i> Books &amp; Research Monographs
        </h4>
        <div style="display: flex; flex-direction: column; gap: 12px;">
          ${books.map(b => `
            <div class="pub-item">
              <span class="pub-number" style="color: var(--primary);"><i class="bi bi-bookmark-star-fill"></i></span>
              <div style="flex-grow: 1;">
                <p class="pub-citation-text">${b.citation}</p>
                <div class="pub-badge-row">
                  <span class="pub-chip">${b.type}</span>
                  <span class="pub-chip">${b.year}</span>
                  ${b.link ? `<a href="${b.link}" target="_blank" rel="noopener noreferrer" class="link-chip" style="font-size:0.78rem; font-weight:700; color:var(--primary);"><i class="bi bi-box-arrow-up-right"></i> Publisher &amp; DOI Link</a>` : ''}
                </div>
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }
  
  html += `
    <div>
      <h4 style="font-size: 1.15rem; margin-bottom: 14px; color: var(--primary);">
        <i class="bi bi-file-earmark-text"></i> Peer-Reviewed Journal Articles &amp; Conference Proceedings
      </h4>
      <div style="display: flex; flex-direction: column; gap: 12px;">
        ${pubs.map(p => `
          <div class="pub-item" data-year="${p.year}">
            <span class="pub-number">${p.number}.</span>
            <div style="flex-grow: 1;">
              <p class="pub-citation-text">${p.citation}</p>
              <div class="pub-badge-row">
                ${p.year ? `<span class="pub-chip"><i class="bi bi-calendar3"></i> ${p.year}</span>` : ''}
                ${p.citations ? `<span class="pub-chip" style="color:var(--primary); font-weight:700;"><i class="bi bi-quote"></i> ${p.citations} Citations</span>` : ''}
                ${p.link ? `
                  <a href="${p.link}" target="_blank" rel="noopener noreferrer" class="link-chip" style="font-size:0.78rem; font-weight:700; color:var(--primary); background:#FFFFFF; border-color:var(--primary);">
                    <i class="bi bi-box-arrow-up-right"></i> View Article / DOI
                  </a>
                ` : ''}
              </div>
            </div>
          </div>
        `).join('')}
      </div>
    </div>
  `;
  
  container.innerHTML = html;
}

// Filtering & Searching Logic
function initFiltersAndSearch() {
  // Simulations Filtering
  const simFilterBtns = document.querySelectorAll('#simFilterPills .filter-btn');
  simFilterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      simFilterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      filterSimulations();
    });
  });

  // KEEN Filtering
  const keenFilterBtns = document.querySelectorAll('#keenFilterPills .filter-btn');
  const keenSearch = document.getElementById('keenSearch');
  
  keenFilterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      keenFilterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      filterKeenCards();
    });
  });
  
  if (keenSearch) {
    keenSearch.addEventListener('input', filterKeenCards);
  }
  
  // Posters Filtering
  const posterFilterBtns = document.querySelectorAll('#posterFilterPills .filter-btn');
  const posterSearch = document.getElementById('posterSearch');
  
  posterFilterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      posterFilterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      filterPosters();
    });
  });
  
  if (posterSearch) {
    posterSearch.addEventListener('input', filterPosters);
  }
}

function filterSimulations() {
  const activeBtn = document.querySelector('#simFilterPills .filter-btn.active');
  const category = activeBtn ? activeBtn.getAttribute('data-filter') : 'all';
  const cards = document.querySelectorAll('.sim-card');
  let visibleCount = 0;
  
  cards.forEach(card => {
    const cardCat = card.getAttribute('data-category') || '';
    const matchCategory = (category === 'all') || (cardCat.toLowerCase().includes(category.toLowerCase()));
    
    if (matchCategory) {
      card.style.display = 'flex';
      visibleCount++;
    } else {
      card.style.display = 'none';
    }
  });
  
  const countBadge = document.getElementById('simCountBadge');
  if (countBadge) countBadge.textContent = `${visibleCount} modules shown`;
}

function filterKeenCards() {
  const activeBtn = document.querySelector('#keenFilterPills .filter-btn.active');
  const category = activeBtn ? activeBtn.getAttribute('data-filter') : 'all';
  const query = (document.getElementById('keenSearch')?.value || '').toLowerCase().trim();
  
  const cards = document.querySelectorAll('.keen-card');
  let visibleCount = 0;
  
  cards.forEach(card => {
    const cardCategory = card.getAttribute('data-category') || '';
    const text = card.textContent.toLowerCase();
    const isFeatured = card.classList.contains('featured-card');
    
    let matchCategory = false;
    if (category === 'all') {
      matchCategory = true;
    } else if (category === 'featured') {
      matchCategory = isFeatured;
    } else if (cardCategory.toLowerCase().includes(category.toLowerCase())) {
      matchCategory = true;
    }
    
    const matchQuery = !query || text.includes(query);
    
    if (matchCategory && matchQuery) {
      card.style.display = 'flex';
      visibleCount++;
    } else {
      card.style.display = 'none';
    }
  });
  
  const countEl = document.getElementById('keenCountBadge');
  if (countEl) countEl.textContent = `${visibleCount} cards found`;
}

function filterPosters() {
  const activeBtn = document.querySelector('#posterFilterPills .filter-btn.active');
  const category = activeBtn ? activeBtn.getAttribute('data-filter') : 'all';
  const query = (document.getElementById('posterSearch')?.value || '').toLowerCase().trim();
  
  const posters = document.querySelectorAll('.poster-card');
  let visibleCount = 0;
  
  posters.forEach(poster => {
    const pCategory = poster.getAttribute('data-category') || '';
    const text = poster.textContent.toLowerCase();
    
    const matchCategory = (category === 'all') || (pCategory.toLowerCase().includes(category.toLowerCase()));
    const matchQuery = !query || text.includes(query);
    
    if (matchCategory && matchQuery) {
      poster.style.display = 'flex';
      visibleCount++;
    } else {
      poster.style.display = 'none';
    }
  });
  
  const countEl = document.getElementById('posterCountBadge');
  if (countEl) countEl.textContent = `${visibleCount} posters shown`;
}

// Modals Handling
function initModals() {
  document.querySelectorAll('.modal-close-btn, .modal-backdrop').forEach(el => {
    el.addEventListener('click', (e) => {
      if (e.target === el) {
        closeModals();
      }
    });
  });
  
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeModals();
  });
  
  // Attach simulation preview listeners
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('.preview-sim-btn');
    if (btn) {
      const url = btn.getAttribute('data-url');
      const title = btn.getAttribute('data-title');
      const repo = btn.getAttribute('data-repo');
      openSimModal(url, title, repo);
    }
  });
}

function closeModals() {
  document.querySelectorAll('.modal-backdrop').forEach(m => {
    m.classList.remove('show');
  });
  const frame = document.getElementById('simModalFrame');
  if (frame) frame.src = 'about:blank';
}

window.openPosterModal = function(posterId) {
  const posters = window.EBL_DATA?.posters || [];
  const poster = posters.find(p => p.id === posterId);
  if (!poster) return;
  
  const modal = document.getElementById('posterModal');
  const titleEl = document.getElementById('posterModalTitle');
  const bodyEl = document.getElementById('posterModalBody');
  const viewPdfBtn = document.getElementById('posterModalViewPdf');
  const dlPdfBtn = document.getElementById('posterModalDownloadPdf');
  
  if (titleEl) titleEl.textContent = poster.title;
  if (viewPdfBtn) viewPdfBtn.href = poster.pdf;
  if (dlPdfBtn) dlPdfBtn.href = poster.pdf;
  
  if (bodyEl) {
    bodyEl.innerHTML = `
      <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 24px; align-items: start;">
        <div style="background: #FFFFFF; border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-md); border:1px solid var(--border-color); text-align: center; padding: 6px;">
          <img src="${poster.thumbnail}" alt="${poster.title}" style="width: 100%; max-height: 520px; object-fit: contain; display: block; background:#FFFFFF;" onerror="this.src='EBL_Research.png'">
        </div>
        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div>
            <span class="poster-category-badge" style="font-size: 0.8rem; padding: 4px 10px;">${poster.category}</span>
            <span style="margin-left: 10px; font-weight: 700; color: var(--text-muted); font-size: 0.9rem;">${poster.year}</span>
          </div>
          <h4 style="font-size: 1.25rem; font-weight: 800; line-height: 1.3; color:var(--primary);">${poster.title}</h4>
          <p style="font-size: 0.88rem; color: var(--text-muted);"><strong>Investigators:</strong> ${poster.authors}</p>
          <p style="font-size: 0.88rem; color: var(--text-muted);"><strong>Faculty Advisor:</strong> ${poster.advisors}</p>
          <p style="font-size: 0.88rem; color: var(--accent); font-weight: 600;"><strong>Venue / Forum:</strong> ${poster.venue}</p>
          <div style="background: var(--bg-alt); padding: 16px; border-radius: var(--radius-md); border: 1px solid var(--border-color); font-size: 0.88rem; line-height: 1.6;">
            <strong>Abstract / Summary:</strong><br>
            ${poster.description}
          </div>
          <div style="display: flex; gap: 10px; margin-top: 10px;">
            <a href="${poster.pdf}" target="_blank" class="btn btn-primary btn-sm" style="flex:1;">
              <i class="bi bi-box-arrow-up-right"></i> Open High-Res PDF
            </a>
            <a href="${poster.pdf}" download class="btn btn-accent btn-sm" style="flex:1;">
              <i class="bi bi-download"></i> Download Poster
            </a>
          </div>
        </div>
      </div>
    `;
  }
  
  if (modal) modal.classList.add('show');
};

function openSimModal(url, title, repo) {
  const modal = document.getElementById('simModal');
  const titleEl = document.getElementById('simModalTitle');
  const frame = document.getElementById('simModalFrame');
  const launchBtn = document.getElementById('simModalLaunch');
  const repoBtn = document.getElementById('simModalRepo');
  
  if (titleEl) titleEl.textContent = title;
  if (frame) frame.src = url;
  if (launchBtn) launchBtn.href = url;
  if (repoBtn) repoBtn.href = repo;
  
  if (modal) modal.classList.add('show');
}

// Navigation & Smooth Scroll
function initNavigation() {
  const navLinksList = document.querySelectorAll('.nav-links .nav-item a');
  const sections = document.querySelectorAll('section[id]');
  
  window.addEventListener('scroll', () => {
    let current = '';
    const scrollY = window.pageYOffset;
    
    sections.forEach(section => {
      const sectionHeight = section.offsetHeight;
      const sectionTop = section.offsetTop - 120;
      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        current = section.getAttribute('id');
      }
    });
    
    navLinksList.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  });
  
  // Mobile drawer toggle
  const mobileBtn = document.getElementById('mobileMenuBtn');
  const headerNavBar = document.querySelector('.header-nav-bar');
  if (mobileBtn && headerNavBar) {
    mobileBtn.addEventListener('click', () => {
      headerNavBar.classList.toggle('mobile-open');
    });
    // Close mobile menu when a nav link is clicked
    document.querySelectorAll('.header-nav-bar .nav-item a').forEach(link => {
      link.addEventListener('click', () => {
        headerNavBar.classList.remove('mobile-open');
      });
    });
  }
}
