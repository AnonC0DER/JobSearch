let loginBtn = document.getElementById('login-form')
let SearchForm = document.getElementById('inner-form')

let Token = localStorage.getItem('token')
let Base_domain = 'http://127.0.0.1:8000/'

if(Token) {
    loginBtn.remove()
}
else{
    SearchForm.remove()
}

function SearchPage(event){
    event.preventDefault();

    var block_to_insert = document.createElement( 'span' );
    var text = document.createTextNode('Searching...');
    block_to_insert.appendChild(text)

    document.getElementsByClassName('suggestion-wrap')[0].appendChild(block_to_insert)

    let token = localStorage.getItem('token')
    let query = event.target['search'].value

    fetch(`${Base_domain}api/job-search/${query}`, {
      method : 'GET', 
      headers : {
        'Content-Type' : 'application/json',
        Authorization : `Token ${token}`
      },
      })
      .then(response => response.json())
      .then(data => {
          ReturnResult(data)
      })
}

function ReturnResult(results) {
    let job_card_div = document.getElementById('jobs-wrapper')
    job_card_div.innerHTML = ''

    for (let i=0; results.length > i; i++){
        let job = results[i]
        
        let jobCard = `
                <div class="jobs--card">
                        <div class="card--header">
                            <table>
                                <tr>
                                    <th>Job title</th>
                                    <th>Company name</th>
                                    <th>Location</th>
                                    <th>Contract</th>
                                    <th>Published date</th>
                                    <th>More details</th>
                                    
                                    <tr>
                                    <td>${job.job_title}</td>
                                    <td>${job.company_name}</td>
                                    <td>${job.location}</td>
                                    <td>${job.contract}</td>
                                    <td>${job.published_date}</td>
                                    <td><a href="${job.more_details}">More details</a></td>
                                    </tr>
                                </tr>
                            </table>
                        </div>
                </div>
        `

        job_card_div.innerHTML += jobCard
    }
}