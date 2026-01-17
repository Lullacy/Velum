const API_URL = "/api/analyze"; // Proxied via Nginx

// Synonyms map (Client-side implementation of defense.py logic)
const EVASION_MAP = {
    "union": "association",
    "strike": "work stoppage",
    "wages": "compensation",
    "protest": "gathering",
    "organize": "coordinate",
    "demand": "request"
};

const postInput = document.getElementById('postInput');
const analyzeBtn = document.getElementById('analyzeBtn');
const reclaimBtn = document.getElementById('reclaimBtn');
const resultsArea = document.getElementById('resultsArea');

let lastAnalysis = null;

analyzeBtn.addEventListener('click', async () => {
    const text = postInput.value.trim();
    if (!text) return;

    setLoading(true);
    reclaimBtn.disabled = true;

    try {
        const response = await fetch(`${API_URL}?text=${encodeURIComponent(text)}`, {
            method: 'POST'
        });
        const data = await response.json();
        lastAnalysis = data;
        
        displayResult(data);
        
        if (data.would_be_flagged) {
            reclaimBtn.disabled = false;
        }

    } catch (error) {
        resultsArea.innerHTML = `<div style="color:red">Error connecting to Resistance Node (API). Is backend running?</div>`;
        console.error(error);
    } finally {
        setLoading(false);
    }
});

reclaimBtn.addEventListener('click', () => {
    if (!postInput.value) return;
    
    // Apply client-side evasion logic
    let text = postInput.value.toLowerCase();
    let originalText = postInput.value;
    
    // Perform simple replacement
    for (const [bad, good] of Object.entries(EVASION_MAP)) {
        if (text.includes(bad)) {
            // Very basic replacement regex
            const regex = new RegExp(bad, 'gi');
            originalText = originalText.replace(regex, good);
        }
    }
    
    // Update UI
    postInput.value = originalText;
    
    // Add visual feedback
    const suggestionBox = document.createElement('div');
    suggestionBox.className = 'suggestion-box';
    suggestionBox.innerHTML = `
        <span class="suggestion-title">🛡️ Voice Reclaimed</span>
        <p>Contextual reformulation applied. Try analyzing again.</p>
    `;
    resultsArea.appendChild(suggestionBox);
    
    reclaimBtn.disabled = true;
    analyzeBtn.click(); // Auto-reanalyze
});

function displayResult(data) {
    resultsArea.innerHTML = '';
    
    const card = document.createElement('div');
    card.className = `result-card ${data.would_be_flagged ? 'flagged' : 'safe'}`;
    
    const header = document.createElement('div');
    header.className = 'result-header';
    header.innerText = data.would_be_flagged ? '❌ SILENCED (Flagged)' : '✅ VOICE HEARD (Allowed)';
    
    card.appendChild(header);
    
    const detail = document.createElement('div');
    if (data.would_be_flagged) {
        detail.innerHTML = `
            <p>The algorithm has suppressed this content.</p>
            <div class="reasons">Detected Triggers: [ ${data.flagged_reasons.join(', ')} ]</div>
        `;
    } else {
        detail.innerHTML = `<p>Your message has successfully bypassed the filter.</p>`;
    }
    card.appendChild(detail);
    
    resultsArea.appendChild(card);
}

function setLoading(isLoading) {
    if (isLoading) {
        analyzeBtn.innerHTML = 'Scanning...';
        analyzeBtn.disabled = true;
    } else {
        analyzeBtn.innerHTML = 'Analyze for Bias';
        analyzeBtn.disabled = false;
    }
}
