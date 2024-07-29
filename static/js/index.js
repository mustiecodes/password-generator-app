function generatePassword() {
  const length = document.getElementById("length").value;
  const useUpper = document.getElementById("use_upper").checked;
  const useNumbers = document.getElementById("use_numbers").checked;
  const useSpecial = document.getElementById("use_special").checked;

  fetch(
    `/generate?length=${length}&use_upper=${useUpper}&use_numbers=${useNumbers}&use_special=${useSpecial}`
  )
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("passwordOutput").textContent = data.password;
    })
    .catch((error) => console.error("Error:", error));
}
