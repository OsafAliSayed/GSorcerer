// variables 
var search = document.getElementById("search");
var cards = document.querySelectorAll(".cards");
console.log(cards)
// event listeners

// functions

search.addEventListener("keyup", function(e){
    var searchValue = e.target.value.toLowerCase();
    cards.forEach(function(card){
        var title = card.querySelector(".card-title").textContent;
        if(title.toLowerCase().indexOf(searchValue) != -1){
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    })
})