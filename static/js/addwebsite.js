const search = document.querySelector("#searchaddwebsite")
const table = document.querySelector(".searchable")
const tableoutput = document.querySelector(".tableoutput")
const thecontainer = document.querySelector(".thecontainer")


search.addEventListener("keyup",(e) => {
    const searchvalue = e.target.value;
    console.log("hasilnya",searchvalue)

   

    

        tableoutput.innerHTML = ""

        fetch("/dashboard/incident/search",{
            body:JSON.stringify({searchtxt:searchvalue}),
            method:"POST",


        })
        .then((res) => res.json())
        .then((datahtml) =>{
            console.log("data",datahtml);
            thecontainer.innerHTML=datahtml.html_data

            
            


        });

        
           
       



       
      



    }

    




);

