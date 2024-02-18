// variables 
var search = document.getElementById("search");
var issues = document.querySelectorAll(".issue");

// event listeners

// search by labels
search.addEventListener("keyup", function(e){ 
    var searchValues = e.target.value.toLowerCase().split(" ");
    searchValues.forEach(function(searchValue){
        searchByLabel(searchValue);
    });
});

// functions
function searchByLabel(searchValue){
    issues.forEach(function(issue){
        var labels = issue.querySelectorAll(".label");
        console.log(labels);
        labels.forEach(function(label){
            if(label.innerHTML.toLowerCase().indexOf(searchValue) != -1){
                issue.style.display = "block";
            } else {
                issue.style.display = "none";
            }
        })
    })
}