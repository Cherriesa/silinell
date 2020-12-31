const search = document.querySelector("#searchaddwebsite")
const table = document.querySelector("#tableoutput")

search.addEventListener("keyup",(e) => {
    const searchvalue = e.target.value;

    if(searchvalue.trim().length > 0){
        console.log("hasilnya".searchvalue)

        fetch("/search-ex",{

        })

    }




});

