async function menu() {
    const jeuButton = document.querySelector('[data-type="jouer"]');

    if (jeuButton) {
        jeuButton.addEventListener("click", async () => {
            
            const payload = { action: "jouer" };
            
            try {
                const response = await fetch(`/`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
    
                if (response.ok) {
                    window.location.href = "/";

                } else {
                    console.error("Server error:", response.status);
                }
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

        if (!file) return;

        const reader = new FileReader();
        
        reader.onload = async (event) => {
            try {
                const jsontext = event.target.result;
                const data = JSON.parse(jsontext);

                const payload = { action: "charger", 'json': data, file_name: 'charge', from_menu: true};

                const response = await fetch('/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                if (response.ok){
                     window.location.href = "/";
                    //  renderGrille();
                    //  updateButtonsState();
                }
            } catch (e) {
                console.error("Network error:", e);
            }
        };

        reader.readAsText(file);
    });

    const quitButton = document.querySelector('[data-type="quitter"]');
    
    quitButton.addEventListener("click", async () => {
        window.close();
            
    });

}

document.addEventListener("DOMContentLoaded", menu);