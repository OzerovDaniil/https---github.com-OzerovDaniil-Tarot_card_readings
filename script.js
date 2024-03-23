// Додавання валідації на поле питання

const questionInput = document.getElementById("question");

questionInput.addEventListener("input", () => {
    if (!questionInput.value.endsWith("?") || questionInput.value.length <= 1) {
        questionInput.classList.add("invalid");
    } else {
        questionInput.classList.remove("invalid");
    }
});

// Додавання повідомлення про завантаження

const submitButton = document.querySelector("input[type='submit']");

submitButton.addEventListener("click", () => {
    if (!questionInput.classList.contains("invalid")) {
        submitButton.value = "Завантаження...";
    }
});
