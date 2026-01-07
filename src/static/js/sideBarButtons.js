document.addEventListener("DOMContentLoaded", () => {

    const selectionSidebar = document.querySelector(".selectionSidebar");
    const selectionButtons = selectionSidebar.querySelectorAll(".btn");

    selectionButtons.forEach(btn => {
        btn.addEventListener("click", () => 
    {
        selectionButtons.forEach(b => {
            b.classList.add("palid")
            b.classList.remove("active")

        });
    
        btn.classList.remove("palid")
        btn.classList.add("active");

    }
        )
    })

    window.addEventListener("click", (event) => {


        if (!document.querySelector(".btn-group-vertical").contains(event.target)) {
            selectionButtons.forEach(b => { 
                b.classList.remove("palid")
                b.classList.remove("active")});
        }
    });

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