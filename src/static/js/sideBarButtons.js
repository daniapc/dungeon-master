document.addEventListener("DOMContentLoaded", () => {

    const sidebar = document.querySelector(".selectionSidebar");
    const buttons = sidebar.querySelectorAll(".btn");

    buttons.forEach(btn => {
        btn.addEventListener("click", () => 
    {
        buttons.forEach(b => {
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
            buttons.forEach(b => { 
                b.classList.remove("palid")
                b.classList.remove("active")});
        }
    });
    
});