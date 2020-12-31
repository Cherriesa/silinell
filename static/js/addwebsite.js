const search = document.querySelector("#searchaddwebsite")
const table = document.querySelector(".searchable")
const tableoutput = document.querySelector(".tableoutput")
search.addEventListener("keyup",(e) => {
    const searchvalue = e.target.value;
    

    if(searchvalue.trim().length > 0){
        tableoutput.innerHTML = ""
        console.log("hasilnya",searchvalue)

        fetch("/dashboard/incident/search",{
            body:JSON.stringify({searchtxt:searchvalue}),
            method:"POST",


        })
        .then((res) => res.json())
        .then((data) =>{
            console.log("data",data);
            table.style.display = "none";
            tableoutput.style.display =  "";

            if (data.length === 0 ){
                console.log("data nya ksosong");
                tableoutput.innerHTML =  "no result";
    
            }else {
                data.forEach((item) => {
                    console.log(item)
                    
                    tableoutput.innerHTML += '<tr><td></td>'+'<td>'+ item.status_action +'</td>'+ '<td>'+ item.status_webstie +'</td>' + '<td>'+ item.website_name +'</td>'+ '<td>'+ item.url +'</td>'+ '<td>'+ item.message +'</td>'+ '<td></td></tr>';

                    
                });

            }


        });

        
           
       



    }else{
        table.style.display = "";
        tableoutput.style.display =  "none";



    }

    




});

