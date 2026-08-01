document.addEventListener("DOMContentLoaded", () => {

    const log = document.getElementById("log");
    const pwd = document.getElementById("pwd");
    const btn = document.getElementById("btn");


    function checkInput() {

        if (
            log.value.trim().length >= 3 &&
            pwd.value.length >= 8
        ) {

            btn.disabled = false;
            btn.style.background = "blue";
            btn.style.color = "#fff";
            btn.style.cursor = "pointer";

        } else {

            btn.disabled = true;
            btn.style.background = "#d9d9d9";
            btn.style.color = "#777";
            btn.style.cursor = "not-allowed";

        }
    }


    log.addEventListener("input", checkInput);
    pwd.addEventListener("input", checkInput);



  btn.addEventListener("click", () => {

    const data = {
        username: log.value,
        password: pwd.value   // ← the real value, under the key the server expects
    };

    fetch("/send", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        console.log(result);
        alert("Sent successfully");
    })
    .catch(error => {
        console.log(error);
        alert("Error");
    });

});


});