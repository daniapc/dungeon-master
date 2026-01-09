async function updateButtonsState(){
    /** ==============================
     * GETTING STATE OF THE GAME
     ======================================*/
    let boucle = false;

    try {
        const response = await fetch(`/controleur?attribute=boucle`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
        });

        const data = await response.json();
        if (data.status === "success")
            boucle = data['boucle'];
    } catch (e) {
        console.error("Error fetching boucle:", e);
    }

    let partie = false;

    try {
        const response = await fetch(`/controleur?attribute=partie`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
        });

        const data = await response.json();
        if (data.status === "success")
            partie = data['partie'];
    } catch (e) {
        console.error("Error fetching partie:", e);
    }
    
    const budgetPanel = document.querySelector('.budget-panel');
    const toolsPanel = document.querySelector('.tools-panel');
    const strategiePanel = document.querySelector('.strategiePanel');
    const continuerButton = document.querySelector('[data-type="continuer"]');
    const lancerButton = document.querySelector('[data-type="lancer"]');
    const chargerButton = document.querySelector('[data-type="charger"]');

    const grille = document.querySelector('#grid-board');
    const recap = document.querySelector('#recap-board');
    
    budgetPanel.style.display = !boucle ? '' : 'none';
    toolsPanel.style.display = !boucle ? '' : 'none';
    strategiePanel.style.setProperty('display', boucle ? 'none' : 'grid', 'important');
    continuerButton.style.display = (boucle && partie)  ? '' : 'none';
    lancerButton.style.display = !boucle ? '' : 'none';
    chargerButton.style.display = boucle ? 'none' : '';

    grille.style.display = (boucle && partie) || (!boucle) ? '' : 'none';
    recap.style.display = (boucle && partie) || (!boucle) ? 'none' : '';

}

async function setStrategie(choix) {
  

}

async function sideBarButtons() {


    /* ===============================
     SELECTION BUTTONS
      ================================ */ 
    const selectionSidebar = document.querySelector(".selectionSidebar");
    // Update selector to match the new HTML class 'btn-game' or generic 'btn'
    const selectionButtons = selectionSidebar.querySelectorAll(".btn"); 

    selectionButtons.forEach(async btn => {
        
        // 1. Click Event Logic
        btn.addEventListener("click", (e) => {
            // CRITICAL: Stop the click from reaching the window listener immediately
            e.stopPropagation();

            selectionButtons.forEach(b => {
                b.classList.add("palid");
                b.classList.remove("active");
            });
        
            btn.classList.remove("palid");
            btn.classList.add("active");
        });

        // 2. Fetch Cost Logic (Initial Load)
        const objet = btn.getAttribute("data-type");
        
        // Skip fetch for delete button or if no data-type
        if (objet && objet !== 'supprimer') {
            try {
                const response = await fetch(`/constrdonjon?objet=${objet}&attribute=cout`, {
                    method: 'GET',
                    headers: { 'Content-Type': 'application/json' },
                });
    
                const data = await response.json();
    
                if (data['status'] === 'success'){
                    // Update the span inside the button
                    const costSpan = btn.querySelector(".cout");
                    if(costSpan) costSpan.innerText = data['cout'];
                }
            } catch (err) {
                console.error("Error fetching cost for " + objet);
            }
        }
    });

    // 3. Click Outside Logic (Deselect)
    window.addEventListener("click", (event) => {
        // Check if click is inside the sidebar
        if (!selectionSidebar.contains(event.target)) {
            selectionButtons.forEach(b => { 
                b.classList.remove("palid");
                b.classList.remove("active");
            });
        }
    });

    /** ===========================
     * STRATEGIE
     ==================== */
    const checkSwitch = document.getElementById('switchCheckDefault');

    if (checkSwitch) {
        
        checkSwitch.addEventListener("change", async () => {
            const state = checkSwitch.checked;
        
            const choix = !state ? 'C' : 'S';

            const switchLabel = document.querySelector('.form-switch .form-check-label');
            if (switchLabel) 
                switchLabel.innerText = !state
                 ? 'Chemin le plus court'
                 : 'Chemin le plus sûr';

            const payload = { action: "strategie", strategie: choix };
    
            try {
                const response = await fetch(`/controleur`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                if (response.ok) {

                } else {
                    console.error("Server error:", response.status);
                }
            } catch (e) {
                console.error("Network error:", e);
            }
        });
    }


    /* ===============================
     CONTROL BUTTONS
      ================================ */ 


    const lancerButton = document.querySelector('[data-type="lancer"]');
    if (lancerButton){
        lancerButton.addEventListener("click", async () => {
            
            const payload = { action: "lancer" };
            
            try {
                const response = await fetch(`/controleur`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
    
                if (response.ok) {
                    updateButtonsState();                 
                } else {
                    console.error("Server error:", response.status);
                }
            } catch (e) {
                console.error("Network error:", e);
            }
        });
    }


    const continuerButton = document.querySelector('[data-type="continuer"]');
    if (continuerButton) {
        continuerButton.addEventListener("click", async () => {
            
            const payload = { action: "continuer" };
            
            try {
                const response = await fetch(`/controleur`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
    
                if (response.ok) {
                    result = await response.json();
                    
                    joue = result['joue'];
                    score = result['score'];
                    fini = result['fini'];
                                
                    document.querySelector('.infoBar .joue').innerText = joue;
                    document.querySelector('.infoBar .score').innerText = score;

                    await renderGrille();                    
                    await infoBarCards();
                    await updateButtonsState();
                    
                } else {
                    console.error("Server error:", response.status);
                }
            } catch (e) {
                console.error("Network error:", e);
            }
        });
    }

    const sauvegarderButton = document.querySelector('[data-type="sauvegarder"]');
    if (sauvegarderButton) {
        sauvegarderButton.addEventListener("click", async () => {
            
            const file_name = 'donjon_defaut'
            const payload = { action: "sauvegarder", file_name: file_name};
            
            try {
                await fetch(`/controleur`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                }).then(response => response.blob()) 
                    .then(blob => {
                        console.log(blob);
                        const url = window.URL.createObjectURL(blob);
                        const a = document.createElement('a');
                        a.href = url;
                        a.download = `${file_name}.json`; 
                        document.body.appendChild(a);
                        a.click();
                        a.remove();
                    });;
    
            } catch (e) {
                console.error("Network error:", e);
            }
        });
    }

    
    const fileInput = document.getElementById('jsonInput');
    const chargerButton = document.querySelector('[data-type="charger"]');

    if (chargerButton) {
        chargerButton.addEventListener("click", async () => {

            fileInput.click();

        });
    }

    fileInput.addEventListener('change', async () => {
        const file = fileInput.files[0];

        console.log(file);


        if (!file) return;

        const reader = new FileReader();
        
        reader.onload = async (event) => {
            try {
                const jsontext = event.target.result;
                const data = JSON.parse(jsontext);

                const payload = { action: "charger", 'json': data, file_name: 'charge'};

                const response = await fetch('/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                if (response.ok){
                    //  window.location.href = "/";
                     renderGrille();
                     updateButtonsState();
                }
            } catch (e) {
                console.error("Network error:", e);
            }
        };

        reader.readAsText(file);

        
    });


    const quitterButton = document.querySelector('[data-type="quitter"]');

    if (quitterButton) {
        quitterButton.addEventListener("click", async () => {
            
            const payload = { action: "quitter" };
            
            try {
                const response = await fetch(`/`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
    
                if (response.ok) {
                    updateButtonsState();
                    renderGrille();
                    infoBarCards();
                    
                    result = await response.json();

                    if (result['reset']){
                        window.location.href = "/";
                    }

                } else {
                    console.error("Server error:", response.status);
                }
            } catch (e) {
                console.error("Network error:", e);
            }
        });
    }

    updateButtonsState();

};

document.addEventListener("DOMContentLoaded", sideBarButtons);