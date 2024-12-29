fetch('http://localhost:8000/api/users/')
            .then(res=>res.json())
            .then(json=>console.log(json))