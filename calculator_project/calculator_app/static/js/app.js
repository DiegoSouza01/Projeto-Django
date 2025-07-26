const buttons = document.querySelectorAll(".buttons button");

let expression = "";

function backspace() {
  expression = expression.slice(0, -1); // Remove o último caractere
  document.querySelector(".display").textContent = expression || "0";
  document.getElementById("expression").value = expression; // Atualiza o campo oculto
  console.log("Backspace pressed, expression now:", expression); // Depuração
}

function calculatePercentage() {
  if (expression) {
    // Converte a expressão para porcentagem (divide por 100)
    let number = parseFloat(expression);
    if (!isNaN(number)) {
      expression = (number / 100).toString();
      document.querySelector(".display").textContent = expression;
      document.getElementById("expression").value = expression;
    }
  }
}

// Adiciona listener para a tecla Backspace
document.addEventListener("keydown", (event) => {
  if (event.key === "Backspace") {
    event.preventDefault(); // Impede o comportamento padrão do navegador
    backspace();
  }
});

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    if (button.classList.contains("clear")) {
      expression = "";
    } else if (button.textContent === "=") {
      // Substitui os operadores personalizados por operadores Python

      let sanitizedExpression = expression.replace("×", "*").replace("÷", "/");
      document.getElementById("expression").value = sanitizedExpression;
    } else {
      expression += button.textContent;
    }

    document.querySelector(".display").textContent = expression || "0";
  });
});
