function insertRow() {
    let table = document.getElementById('sampleTable');
    let row = table.insertRow(0);
    let cel1 = row.insertCell(0);
    let cel2 = row.insertCell(1);
    cel1.textContent = 'new cell1';
    cel2.textContent = 'new cell2';

}