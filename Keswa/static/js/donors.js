$.getJSON('donors.json', function(data) {
    // The data variable contains the JSON data
    console.log(data);
  });
  
  $.getJSON('path/to/donors.json', function(data) {
    var table = $('<table></table>');
    table.append('<thead><tr><th>Name</th><th>Email</th><th>Amount</th><th>Frequency</th><th>Payment</th></tr></thead>');
    var tbody = $('<tbody></tbody>');
  
    data.forEach(function(donor) {
      var row = $('<tr></tr>');
      row.append('<td>' + donor.name + '</td>');
      row.append('<td>' + donor.email + '</td>');
      row.append('<td>' + donor.amount + '</td>');
      row.append('<td>' + donor.frequency + '</td>');
      row.append('<td>' + donor.payment + '</td>');
      tbody.append(row);
    });
  
    table.append(tbody);
    $('#donor-table').append(table);
  });