const headers = document.getElementById('calenderHeaders')

        fetch('http://127.0.0.1:8000/agenda2')
        .then(response => response.json())
        .then(data => {
            console.log(data.data)
            calendarDates=data.data;
            for(dia in calendarDates){
                // d = Monday \ Tuesday \ Wednesday
                console.log(dia, 'este es dia')
                
                const div = document.createElement("div")
                div.append(dia)
                div.classList.add('calendar-header')
                headers.appendChild(div)
                
            }
        });
// const block = document.getElementById('blocks')
//         fetch('http://127.0.0.1:8000/agenda2')
//         .then(response => response.json())
//         .then(data => {
//             console.log(data.data)
//             calendarDates=data.data;
//             for(dia in calendarDates){
//                 // d = Monday \ Tuesday \ Wednesday
//                 console.log(dia, 'este es dia')
                
//                 const div = document.createElement("div")
//                 div.append(dia)
//                 div.classList.add('block-agg')
//                 block.appendChild(div)
                
//             }
//         });