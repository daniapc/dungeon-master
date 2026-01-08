async function infoBarCards () {

    /** =====================
     *  HEROS
     ==================*/

    const heros = document.querySelector(".heros");

    const existingInstances = heros.querySelectorAll('.panel');
    existingInstances.forEach(instance => instance.remove());

    try {
        const response = await fetch(`/controleur?attribute=heros`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
        });

        const data = await response.json();
        if (data.status === "success"){
            herosList = data['heros'];
            heros.innerHTML =`
                <div class="panel-header">
                    <i class="fa-solid fa-location-crosshairs"></i> Pos Héros (x,y)
                </div>
            `;

            herosList.forEach(hero => {
                const heroDiv = document.createElement('div');

                heroDiv.className = 'panel mb-3';

                heroDiv.innerHTML = `
                        <i class="fa-solid fa-${hero['index'] + 1} me-2 text-accent icon-hero"></i>
                        <span>(${hero['x']}, ${hero['y']})</span>
                        <i class="fa-solid fa-droplet icon-life"></i>
                        <span> ${hero['pv']}</span>
                    `;

                heros.appendChild(heroDiv);
            });
        }

    } catch (e) {
        console.error("Error fetching budget:", e);
    }

    /** =====================
     *  VAGUE
     ==================*/
    const vague = document.querySelector(".vague");

    try {
        const response = await fetch(`/controleur?attribute=vague`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
        });

        const data = await response.json();
        if (data.status === "success")
            vague.innerText = data['vague'];
    } catch (e) {
        console.error("Error fetching vague:", e);
    }

}

document.addEventListener("DOMContentLoaded", infoBarCards);