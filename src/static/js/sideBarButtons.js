document.addEventListener("DOMContentLoaded", async () => {

    /* ===============================
     BUDGET
      ================================ */ 
    const budget = document.querySelector(".budget");

    const response = await fetch(`/constrdonjon?attribute=${'budget'}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    });

    const data = await response.json();
    if (data.status == "success")
        budget.querySelector(".value").innerText = data['budget'];


    /* ===============================
     SELECTION BUTTONS
      ================================ */ 
    const selectionSidebar = document.querySelector(".selectionSidebar");
    const selectionButtons = selectionSidebar.querySelectorAll(".btn");

    selectionButtons.forEach(async btn => {
        btn.addEventListener("click", () => {
        selectionButtons.forEach(b => {
            b.classList.add("palid")
            b.classList.remove("active")

        });
    
        btn.classList.remove("palid")
        btn.classList.add("active");

        });

        objet = btn.getAttribute("data-type");
        attribute = 'cout'

        const response = await fetch(`/constrdonjon?objet=${objet}&attribute=${attribute}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
        });

        const data = await response.json();

        if (data['status'] == 'success'){
            btn.querySelector(".cout").innerText = data['cout'];
        }


    })

    window.addEventListener("click", (event) => {


        if (!document.querySelector(".btn-group-vertical").contains(event.target)) {
            selectionButtons.forEach(b => { 
                b.classList.remove("palid")
                b.classList.remove("active")});
        }
    });

    /* ===============================
     CONTROL BUTTONS
      ================================ */ 

    const quitterButton = document.querySelector('[data-type="quitter"]');

    // TODO: "are you sure?"
    quitterButton.addEventListener("click", async () => {
        
        payload = {
            action: "quitter"
        }
        
        const response = await fetch(`/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            window.location.reload();
        } else {
            console.error("Server error:", response.status);
        }
    })

    
});