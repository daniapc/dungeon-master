document.addEventListener("DOMContentLoaded", () => {

    const sidebar = document.querySelector(".selectionSidebar");
    const buttons = sidebar.querySelectorAll(".btn");

    buttons.forEach(btn => {
        btn.addEventListener("click", () => 
    {
        buttons.forEach(b => b.classList.add("palid"));
    
        btn.classList.remove("palid");
    }
        )
    })

    window.addEventListener("click", (event) => {


        if (!document.querySelector(".btn-group-vertical").contains(event.target)) {
            buttons.forEach(b => b.classList.remove("palid"));
        }
    });
    
});