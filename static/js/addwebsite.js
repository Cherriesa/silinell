const search = document.querySelector("#searchaddwebsite")
const table = document.querySelector(".searchable")
const tableoutput = document.querySelector(".tableoutput")
const thecontainer = document.querySelector(".thecontainer")
const boxscript = document.querySelector(".boxscript")


$(document).on('click', '.confirm-delete', function(){
    return confirm('Are you sure you want to delete this?');
})


search.addEventListener("keyup",(e) => {
    
    const searchvalue = e.target.value;

    const scriptPromise = new Promise((resolve, reject) => {
        $.getScript( "/static/js/pagination.js" );
      });

        fetch("/dashboard/incident/search",{
            body:JSON.stringify({searchtxt:searchvalue}),
            method:"POST",
            
        

        })
        .then((res) => res.json())
        


        
          
        
        .then((datahtml) =>{
            thecontainer.innerHTML=datahtml.html_data
            




         

            
            


        })
      
       
        
           
       



       
      



    }

    




);

