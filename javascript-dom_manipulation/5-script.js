const update = document.body.querySelector("#update");
const header = document.body.querySelector("header")

update.addEventListener("click", () => {
header.textContent = "New Header!!!";
});
