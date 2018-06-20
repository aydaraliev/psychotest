document.getElementById('button').addEventListener('click', function () {
  var login = document.getElementById('login').value;
  var password = document.getElementById('password').value;
  if (login === '' || password === '') {
    alert("Please fill all fields");
  } else {

    var request = new XMLHttpRequest();
    request.open('POST', 'http://http://188.166.88.156/tests/get_all_users', true);
    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
    var params = JSON.stringify({ login: login, password: password });
    request.responseType = 'blob';

    request.onload = function() {
      // Only handle status code 200
      if(request.status === 200) {
        // Try to find out the filename from the content disposition `filename` value
        var disposition = request.getResponseHeader('content-disposition');
        var matches = /"([^"]*)"/.exec(disposition);
        var filename = (matches != null && matches[1] ? matches[1] : 'file.pdf');

        // The actual download
        var blob = new Blob([request.response], { type: 'application/pdf' });
        var link = document.createElement('a');
        link.href = window.URL.createObjectURL(blob);
        link.download = filename;

        document.body.appendChild(link);

        link.click();

        document.body.removeChild(link);
      }

      // some error handling should be done here...
    };

    request.send(params);
  }
});

