async function renderGrille() {
    // (day 2)
    // Base code from Gemini adapted
    try {
        const response = await fetch("/grille");
        const matrix = await response.json();

        const board = document.getElementById("grid-board");
        board.innerHTML = ""; // Clear "Loading..." text
        
        matrix_length = matrix.length

        const rowDiv = document.createElement("div");
        rowDiv.className = "rowCase";
        const caseDiv = document.createElement("div");
        caseDiv.className = "col caseDiv coordinate";
        rowDiv.append(caseDiv);

        for(let i = 0; i < matrix_length; i++) {
            const caseDiv = document.createElement("div");
            caseDiv.className = "col caseDiv coordinate";
            caseDiv.innerText = i;

            rowDiv.append(caseDiv);
        }
        board.append(rowDiv);

        let i = 0;

        matrix.forEach((rowData, rowIndex) => {
            const rowDiv = document.createElement("div");
            rowDiv.className = "rowCase";

            const caseDiv = document.createElement("div");
            caseDiv.className = "col caseDiv coordinate";
            caseDiv.innerText = i;
            rowDiv.append(caseDiv);

            rowData.forEach((cellData, colIndex) => {
                const caseDiv = document.createElement("button");
                caseDiv.className = "col caseDiv";

                if (cellData.symbol && cellData.symbol !== " ") {
                    let imgSrc = "";

                    switch (cellData.symbol) {
                        case 'H':
                            imgSrc = "static/images/heros.png";
                            break;
                        case '#':
                            imgSrc = "static/images/mur.png";
                            break;
                        case '_':
                            imgSrc = "static/images/piege1.png";
                            break;
                        case '^':
                            imgSrc = "static/images/piege2.png";
                            break;
                        case '¤':
                            imgSrc = "static/images/piege3.png";
                            break;
                        case 'M1':
                            imgSrc = "static/images/monstre.png";
                            break;
                        case 'M2':
                            imgSrc = "static/images/monstreV2.png";
                            break;
                        case 'T':
                            imgSrc = "static/images/tresor.png";
                            break;
                        case 'E':
                            imgSrc = "static/images/entree.png";
                            break;
                        default:
                            // If aucune image
                            caseDiv.innerText = cellData.symbol;
                            caseDiv.style.color = cellData.color;
                            caseDiv.style.fontWeight = cellData.weight;
                    }

                    if (imgSrc) {
                        const img = document.createElement("img");
                        img.src = imgSrc;
                        img.style.width = "100%";  
                        img.style.height = "100%";
                        img.style.objectFit = "contain"; 
                        caseDiv.appendChild(img);
                    }
                }
                
                const currentX = colIndex;
                const currentY = rowIndex;
                
                caseDiv.addEventListener("click",  async ()=>{
                    const button = document.querySelector(".selectionSidebar .btn.active");

                    if (button == null)
                        return;

                    const datatype = button.getAttribute("data-type");

                    payload = {}

                    payload['action'] = datatype == 'supprimer' 
                        ? 'delete '
                        : 'put';
                    payload['objet'] = button.getAttribute("data-type");
                    payload['x'] = `${currentX}`;
                    payload['y'] = `${currentY}`;

                    const response = await fetch(`/constrdonjon`, {
                        method: datatype == 'supprimer'
                            ? 'DELETE' 
                            : 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(payload)
                    })

                    if (response.ok) {
                        const result = await response.json();
                        document.querySelector(".budget .value").innerText = result['budget'];
                        
                        await renderGrille();
                        
                    } else {
                        console.error("Server error:", response.status);
                    }
                })


                rowDiv.appendChild(caseDiv);
            });

            board.appendChild(rowDiv);

            i+=1;
        });
    } catch (error) {
        console.error("Error rendering grid:", error);
    }
}

document.addEventListener("DOMContentLoaded", renderGrille);