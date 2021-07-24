const checkmark = "&#10004;";
const moviesTable = document.getElementById("moviesTable");

fetch("../public/marvelMovies.json")
    .then(response => response.json())
    .then(json => {
        console.log(json);
        populateTable(moviesTable, json.marvelMovies);
    });


function populateTable(table, rows) {
    rows.forEach(movie => {
        let row = table.insertRow();
        let movieColumn = row.insertCell();
        let seenColumn = row.insertCell();
        movieColumn.innerHTML = movie.name;
        seenColumn.innerHTML = movie.seen ? checkmark : null;
    });
}
