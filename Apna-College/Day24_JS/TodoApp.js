let input = document.querySelector("input");
let button = document.querySelector("button");

function addTask() {
    // Create a new list item
    let li = document.createElement("li");
    li.innerHTML = input.value + " ";

    // Create a new delete button
    let btn = document.createElement("button");
    btn.classList.add("del");
    btn.innerHTML = "Delete";

    // Attach the delete functionality to the button
    btn.addEventListener("click", deleteTask);

    // Append the button to the list item and the list item to the list
    li.append(btn);
    document.querySelector("ul").append(li);

    // Clear the input field after adding the task
    input.value = "";
}

function deleteTask(event) {
    // Remove the list item of the clicked delete button
    event.target.parentElement.remove();
}

// Attach the addTask function to the button click event
button.addEventListener("click", addTask);
