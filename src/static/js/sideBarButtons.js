document.addEventListener("DOMContentLoaded", async () => {

    /* ===============================
     BUDGET
      ================================ */ 
    const budget = document.querySelector(".budget");

    try {
        const response = await fetch(`/constrdonjon?attribute=budget`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
        });

        const data = await response.json();
        if (data.status === "success")
            budget.querySelector(".value").innerText = data['budget'];
    } catch (e) {
        console.error("Error fetching budget:", e);
    }

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


    /* ===============================
     CONTROL BUTTONS
      ================================ */ 
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
                    window.location.reload();
                } else {
                    console.error("Server error:", response.status);
                }
            } catch (e) {
                console.error("Network error:", e);
            }
        });
    }

    const continuerButton = document.querySelector('[data-type="lancer"]');
    if (continuerButton) {
        continuerButton.addEventListener("click", async () => {
            
            const payload = { action: "lancer" };
            
            try {
                const response = await fetch(`/`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
    
                if (response.ok) {
                    result = await response.json();

                    joue = result['joue'];
                    score = result['score'];

                    document.querySelector('.infoBar .joue').innerText = joue;
                    document.querySelector('.infoBar .score').innerText = score;

                    await renderGrille();                    
                    await infoBarCards();                    
                } else {
                    console.error("Server error:", response.status);
                }
            } catch (e) {
                console.error("Network error:", e);
            }
        });
    }

});