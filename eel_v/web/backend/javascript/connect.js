function give_data(){

    window.location.href = 'http://localhost:8000/html/table_chose.html'
    eel.take_data([document.getElementById('host').value, document.getElementById('user').value, document.getElementById('password').value, document.getElementById('database').value], document.getElementById('remember').value)

}

eel.expose(set_data)
function set_data(data){

    let arr = [document.getElementById('host'), document.getElementById('user'), document.getElementById('password'), document.getElementById('database')]
    for (let i = 0; i < 4; i++){

        arr[i].value = data[i]

    }

    document.getElementById('remember').checked = true

}