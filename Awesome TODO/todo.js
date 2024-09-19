const toDoForm = document.querySelector(".toDoForm");
const toDoInput = toDoForm.querySelector("input");
const toDos = document.querySelector(".toDos");

const TODOLIST = "toDoList";
let toDoList = [];

function saveToDo(toDo) {
    const toDoObj = {
        text: toDo,
        id: toDoList.length + 1,
    };
    toDoList.push(toDoObj);
    localStorage.setItem(TODOLIST, JSON.stringify(toDoList));
}

function paintToDo(toDo) {
    const li = document.createElement("li");
    const span = document.createElement("span");
    span.innerHTML = toDo;
    li.appendChild(span);
    toDos.appendChild(li);
}

function createToDo(event) {
    event.preventDefault();
    const toDo = toDoInput.value;
    paintToDo(toDo);
    saveToDo(toDo);
    toDoInput.value = "";
}

function loadToDoList() {
    const loadedToDoList = localStorage.getItem(TODOLIST);
    if (loadedToDoList !== null) {
        const parsedToDoList = JSON.parse(loadedToDoList);
        for (let toDo of parsedToDoList) {
            const { text } = toDo;
            paintToDo(text);
            saveToDo(text);
        }
    }
}

function init() {
    loadToDoList();
    toDoForm.addEventListener("submit", createToDo);
}
init();
