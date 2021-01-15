const search = document.querySelector("#searchaddwebsite")
const table = document.querySelector(".searchable")
const tableoutput = document.querySelector(".tableoutput")
const thecontainer = document.querySelector(".thecontainer")
const boxscript = document.querySelector(".boxscript")


search.addEventListener("input",(e) => {
    e.preventDefault();
    const searchvalue = e.target.value;

    

        fetch("/dashboard/incident/search",{
            body:JSON.stringify({searchtxt:searchvalue}),
            method:"POST",
            
        

        })
        .then((res) => res.json())
    
        


        
          
        
        .then((datahtml) =>{
                $(thecontainer).html(datahtml.html_data)
 
            




         

            
            


        })
    

      
       
        
           
     



       
      



    
    
    
    
    
});

