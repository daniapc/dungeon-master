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

        matrix.forEach((rowData) => {
            const rowDiv = document.createElement("div");
            rowDiv.className = "rowCase";

            const caseDiv = document.createElement("div");
            caseDiv.className = "col caseDiv coordinate";
            caseDiv.innerText = i;
            rowDiv.append(caseDiv);

            rowData.forEach((cellData) => {
                const caseDiv = document.createElement("button");
                caseDiv.className = "col caseDiv";

                caseDiv.style.color = cellData.color;
                caseDiv.style.fontWeight = cellData.weight;
                caseDiv.innerText = cellData.symbol; 
                
                caseDiv.addEventListener("click",  ()=>{

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