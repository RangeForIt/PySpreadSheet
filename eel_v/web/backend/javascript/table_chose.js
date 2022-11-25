eel.load_tables()

eel.expose(add_table)
function add_table(names){
    let table = document.querySelector('table#main_table')

    for (let i = 0; i < names.length; i++){

        let tr = document.createElement('tr')
        let td = document.createElement('td')
        let btn = document.createElement('button')

        btn.textContent = names[i][0]
        btn.id = names[i][0]
        btn.className = 'btn'
        btn.onclick = on_table.bind(null, names[i][0])

        td.appendChild(btn)
        tr.appendChild(td)
        table.appendChild(tr)

    }

}

function on_table(name){

    eel.open_table(name)
    window.location.href = "http://localhost:8000/html/table_edit.html"

}

function make_command(){

    let command = document.getElementById('command')

    console.log(command.value)

    eel.make_command(command.value)

}

eel.expose(ask)
function ask(question){

    return confirm(question)

}

eel.expose(alrt)
function alrt(text){

    alert(text)

}

function clear(){

    let table = document.querySelector('table#main_table')

    table.remove()

    table = document.createElement('table')
    table.id = 'main_table'

    document.body.appendChild(table)

}

eel.expose(reload)
function reload(){

    clear()
    eel.load_tables()

}

eel.expose(go_inst)
function go_inst(){

    window.location.href = 'http://localhost:8000/html/table_instance.html'

}