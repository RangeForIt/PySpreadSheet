eel.set_table()

eel.expose(show_t)
function show_t(table_data, data){
    let table = document.querySelector('table')

    let tr_1 = document.createElement('tr')
    tr_1.id = "not_row"

    for (let i = 0; i < data.length; i++){

        let td_1 = document.createElement('td')
        let em = document.createElement('em')
        em.textContent = data[i][7]

        td_1.appendChild(em)
        tr_1.appendChild(td_1)

    }

    table.appendChild(tr_1)

    for (let i = 0; i < table_data.length; i++){
        let tr = document.createElement('tr')
        tr.id = "row"

        for (let j = 0; j < table_data[i].length; j++){
            
            let td = document.createElement('td')
            let inp = document.createElement('input')
            inp.className = "cell"
            inp.value = table_data[i][j]
            td.appendChild(inp)
            tr.appendChild(td)

        }

        table.appendChild(tr)

    }

}

function get(){

    let table = document.querySelector('table')

    let rows = table.getElementsByTagName('tr')

    let result = []

    for (let i = 0; i < rows.length; i++){
        if (rows[i].id == "row"){

            console.log(rows[i])

            let a = []
            let els = rows[i].getElementsByTagName('input')

            for (let j = 0; j < els.length; j++){

                a[j] = els[j].value
            
            }

            result[i] = a
        }

        else{

            continue

        }
    }

    return result

}

function clear(){

    let table = document.querySelector('table')

    let rows = table.getElementsByTagName('tr')

    for (let i = 0; i < rows.length; i++){

        rows[i].remove()

    }
}

function save(){

    eel.save(get())

}

eel.expose(new_row)
function new_row(num){

    let row = num
    console.log(row)

    let table = document.querySelector('table')

    let tr = document.createElement('tr')
    tr.id = 'row'

    for (let i = 0; i < row; ++i){


        let td = document.createElement('td')

        let inp = document.createElement('input')
        inp.className = 'cell'

        td.appendChild(inp)

        tr.appendChild(td)

    }

    table.appendChild(tr)

}

function add_new(){

    eel.new_r()

}

function remove_last(){

    let table = document.querySelector('table')

    let rows = table.getElementsByTagName('tr')

    rows[rows.length - 1].remove()

}

eel.expose(alerti)
function alerti(text){

    alert(text)

}