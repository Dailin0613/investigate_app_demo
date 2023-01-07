const form = document.querySelector('#form');

let teams = []

window.addEventListener('DOMContentLoaded', async () => {
    const response = await fetch('/team');
    const data = await response.json()
    teams = data
    render_teams(teams)
})

form.addEventListener('submit', async e => {
    e.preventDefault();

    const name = form['name'].value
    const objective = form['objective'].value
    const description = form['description'].value
    const goal = form['goal'].value

    const response = await fetch('/team', {
        method: 'POST',
        headers: {'contentType' : 'multipart/form-data'},
        body: JSON.stringify({
            name,
            objective,
            description,
            goal
        })
    })

    const data = await response.json()
    teams.push(data)
    render_teams(teams)
    form.reset

})

function render_teams(teams){
    const content = document.querySelector('#content')
    content.innerHTML = ''

    teams.forEach(team => {
        const teamItem = document.createElement('div')
        teamItem.innerHTML = `
            <h1 class="card-title">${team.name}</h1>
            <p class="card-text">${team.objective}</p>
            <p class="card-text">${team.description}</p>
            <p class="card-text">${team.goal}</p>
            <div>
                <button class="btn-delete btn btn-dark btn-sm">Delete</button>
            </div>
        `

        const btn_delete = teamItem.querySelector('.btn-delete')
        btn_delete.addEventListener('click', async () => {
            const response = await fetch(`/team/delete/${team.id}`, {
                method: 'DELETE'
            })
            const data = await response.json()

            teams = teams.filter(team => team.id !== data.id)
            render_teams(teams)
        })
        content.append(teamItem)
    })
}