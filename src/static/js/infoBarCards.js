async function infoBarCards () {

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

            console.log(data);
            console.log( data['heros']);

            herosList = data['heros'];

            herosList.forEach(hero => {
                const heroDiv = document.createElement('div');

                heroDiv.className = 'panel mb-3';

                heroDiv.innerText = 
                    `${hero['index']}: ${hero['x']},${hero['y']}`;

                heros.appendChild(heroDiv);
            });
        }

    } catch (e) {
        console.error("Error fetching budget:", e);
    }
}

document.addEventListener("DOMContentLoaded", infoBarCards);