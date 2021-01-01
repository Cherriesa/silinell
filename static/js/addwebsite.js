const search = document.querySelector("#searchaddwebsite")
const table = document.querySelector(".searchable")
const tableoutput = document.querySelector(".tableoutput")
const ulpaginations = document.querySelector(".pagination")


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
                    var stickyval = "";
                    if(item.stickied === 'Stikced'){
                        stickyval = '<a href="#" data-toggle="tooltip" title="this incident is stickied"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star" data-toggle="tooltip" data-placement="top"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></a>';
                        
                    }
            
                   
                    tableoutput.innerHTML += '<tr><td>'+  stickyval + '</td>'+'<td>'+  item.website_name +'</td>'+'<td>'+ item.status_action +'</td>'+ '<td>'+ item.status_webstie +'</td>' +  '<td>'+ item.url +'</td>'+ '<td>'+ item.message +'</td>'+ '<td><a class="btn btn-danger" href="/dashboard/incident/delete/'+ item.id + '">delete</a></td></tr>';

                    
                });

            }


        });

        
           
       



    }else{
        table.style.display = "";
        tableoutput.style.display =  "none";



    }

    




});

