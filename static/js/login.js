let Base_domain = 'http://127.0.0.1:8000/'

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}


if (document.getElementById('login-form')) {
    let form = document.getElementById('login-form')
    form.addEventListener('submit', (e) => {
        e.preventDefault()
    
        
        let formData = {
            'email': form.email.value,
            'password': form.password.value
        }
    
        var csrftoken = readCookie('csrftoken');
        fetch(`${Base_domain}api/users/token/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken' : csrftoken,
            },
            body: JSON.stringify(formData)
        })
            .then(response => response.json())
            .then(data => {
                if ('non_field_errors' in data) {
                    alert('Username OR password did not work')
                    console.log(data)
                }
                else {
                    alert('Redirecting to home page...')
                    localStorage.setItem('token', data.token)
                    window.location = '/'
                }
            })
    })
} else {
    let form = document.getElementById('register-form')
    form.addEventListener('submit', (e) => {
        e.preventDefault()
    
        
        let formData = {
            'email': form.email.value,
            'name': form.name.value,
            'password': form.password.value
        }
    
        var csrftoken = readCookie('csrftoken');
        fetch(`${Base_domain}api/users/create/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken' : csrftoken,
            },
            body: JSON.stringify(formData)
        })
            .then(response => response.json())
            .then(data => {
                if (data.email == 'user with this email already exists.'){
                    alert('User with this email already exists !')
                    console.log(data)
                } 
                else if (data.password == 'Ensure this field has at least 5 characters.'){
                    alert('Ensure this field has at least 5 characters.')
                    console.log(data)
                }
                else if (data.email == form.email.value){
                    alert('Registration completed successfully.')
                    window.location = '/login'
                }
                
            })
    })
}