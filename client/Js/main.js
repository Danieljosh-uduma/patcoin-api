fetch('http://localhost:8000/api')
            .then(res=>res.json())
            .then(json=>console.log(json))