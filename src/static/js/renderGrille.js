async function renderGrille() {
    try {
        const response = await fetch("/grille");
        const matrix = await response.json();

        
        const board = document.getElementById("grid-board");
        board.innerHTML = ""; // Clear "Loading..." text
        
        matrix.forEach((rowData) => {
        const rowDiv = document.createElement("div");
        rowDiv.className = "row";
        
        matrix_length = matrix.length

        for(let i = 0; i < matrix_length; i++) {
            
        }

        rowData.forEach((cellData) => {
            const caseDiv = document.createElement("div");
            caseDiv.className = "col caseDiv";

            caseDiv.style.color = cellData.color;
            caseDiv.style.fontWeight = cellData.weight;
            caseDiv.innerText = cellData.symbol;

            caseDiv.style.minHeight = "30px";

            rowDiv.appendChild(caseDiv);
        });

        board.appendChild(rowDiv);
        });
    } catch (error) {
        console.error("Error rendering grid:", error);
    }
}

document.addEventListener("DOMContentLoaded", renderGrille);