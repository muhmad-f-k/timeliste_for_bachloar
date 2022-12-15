// Hent ut tabellen og knappen fra HTML-dokumentet
const table = document.querySelector("table");
const button = document.querySelector("button");

// Legg til en lytter på knappen for å kjøre en funksjon når brukeren trykker på den
button.addEventListener("click", () => {
  // Hent ut antall rader i tabellen
  const numRows = table.rows.length;

  // Legg til en ny rad i tabellen ved hjelp av .insertRow()-metoden
  const newRow = table.insertRow(numRows);

  // Legg til innhold i den nye raden ved å sette verdier til cellene
  const cell1 = newRow.insertCell(0);
  cell1.innerHTML = "Ny verdi 1";
  const cell2 = newRow.insertCell(1);
  cell2.innerHTML = "Ny verdi 2";
});
