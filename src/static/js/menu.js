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
}

document.addEventListener("DOMContentLoaded", menu);