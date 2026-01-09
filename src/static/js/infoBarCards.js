async function infoBarCards () {


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
    const vague = document.querySelector(".vague-count");

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

    /** =====================================================
     * RECAP
     =========================================== */
    const recap = document.querySelector("#recap-board");
    const isVisible = recap && window.getComputedStyle(recap).display !== 'none';

    try {
        response = await fetch(`/controleur?attribute=recap`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
        });

        const data = await response.json();
        
        if (data.status === "success"){
            const result = data['partie'];

            const herosEngages = recap.querySelector('.heros-engages');
            herosEngages.querySelector('.vague').innerText = result['nb_heros'];
            herosEngages.querySelector('.total').innerText = result['nb_heros_total'];

            const hMorts = recap.querySelector('.heros-morts');
            hMorts.querySelector('.vague').innerText = result['nb_heros_morts'];
            hMorts.querySelector('.total').innerText = result['nb_heros_morts_total'];

            const pFaibles = recap.querySelector('.pieges-faibles');
            pFaibles.querySelector('.vague').innerText = result['nb_piege_faible_active'];
            pFaibles.querySelector('.total').innerText = result['nb_piege_faible_active_total'];

            const pMoyens = recap.querySelector('.pieges-moyens');
            pMoyens.querySelector('.vague').innerText = result['nb_piege_moyen_active'];
            pMoyens.querySelector('.total').innerText = result['nb_piege_moyen_active_total'];

            const pPuissants = recap.querySelector('.pieges-puissants');
            pPuissants.querySelector('.vague').innerText = result['nb_piege_puissant_active'];
            pPuissants.querySelector('.total').innerText = result['nb_piege_puissant_active_total'];

            const monstres = recap.querySelector('.monstres');
            monstres.querySelector('.vague').innerText = result['nb_monstres_morts'];
            monstres.querySelector('.total').innerText = result['nb_monstres_morts_total'];

            const tresor = recap.querySelector('.tresor');
            tresor.querySelector('.trouve').innerText = result['tresor_trouve'] ? "OUI" : "NON";
        }
            // vague.innerText = data['recap'];
    } catch (e) {
        console.error("Error fetching recap:", e);
    }
    


}

document.addEventListener("DOMContentLoaded", infoBarCards);