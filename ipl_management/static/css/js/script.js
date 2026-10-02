
function openLogin() {
    document.getElementById("loginModal").style.display = "flex";
}

function closeLogin() {
    document.getElementById("loginModal").style.display = "none";
}


function searchTeam() {
    let input = document.getElementById("search").value.toLowerCase();
    let rows = document.querySelectorAll("table tr");

    rows.forEach(row => {
        if (row.innerText.toLowerCase().includes(input)) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });
}