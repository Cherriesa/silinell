//Pagination
pageSize = 8;
incremSlide = 5;
startPage = 0;
numberPage = 0;

var pageCount =  $(".line-content").length / pageSize;
var totalSlidepPage = Math.floor(pageCount / incremSlide);
    
for(var i = 0 ; i<pageCount;i++){
    $("#pagin").append('<li class="page-item"><a href="#" class="page-link">'+(i+1)+'</a></li> ');
    if(i>pageSize){
       $("#pagin li").eq(i).hide();
    }
}

var prev = $("<li/>").addClass("prev page-link").html("Prev").click(function(){
   startPage-=5;
   incremSlide-=5;
   numberPage--;
   slide();
});

prev.hide();

var next = $("<li/>").addClass("next page-link").html("Next").click(function(){
   startPage+=5;
   incremSlide+=5;
   numberPage++;
   slide();
});

$("#pagin").prepend(prev).append(next);

$("#pagin li").first().find("a").addClass("current");

slide = function(sens){
   $("#pagin li").hide();
   
   for(t=startPage;t<incremSlide;t++){
     $("#pagin li").eq(t+1).show();
   }
   if(startPage == 0){
     next.show();
     prev.hide();
   }else if(numberPage == totalSlidepPage ){
     next.hide();
     prev.show();
   }else{
     next.show();
     prev.show();
   }
   
    
}

showPage = function(page) {
	  $(".line-content").css('display','none');
	  $(".line-content").each(function(n) {
	      if (n >= pageSize * (page - 1) && n < pageSize * page)
	          $(this).css('display','grid');;
	  });        
}
    
showPage(1);
$("#pagin li a").eq(0).addClass("current");

$("#pagin li a").click(function() {
   $("#pagin li a").removeClass("current");
   $("#pagin li").removeClass("active");
   $(this).closest('li').addClass('active');
   $(this).attr('id','hallo');
   var span = document.createElement("span");
   document.getElementById("hallo").appendChild(span); 
   $(this).addClass("current");
   $(this).removeAttr("id");
	 showPage(parseInt($(this).text()));
});