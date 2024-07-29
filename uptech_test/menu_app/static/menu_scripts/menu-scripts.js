function change_collapse(list){
    list.classList.toggle('collapse')
}


function collapse_btn_onclick(btn_id, list_id){
    let button = document.getElementById(btn_id)
    let selected_lists = document.getElementById(list_id)
    button.classList.toggle('btn-collapsed')
    if (selected_lists !== null) change_collapse(selected_lists);
}