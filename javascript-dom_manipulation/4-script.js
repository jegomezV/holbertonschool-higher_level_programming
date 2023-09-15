const add_item = document.body.querySelector("#add_item");
const my_list = document.body.querySelector(".mylist");

add_item.addEventListener("click", () =>{
    const li = document.createElement("li");
    li.textContent = "Item";
});
