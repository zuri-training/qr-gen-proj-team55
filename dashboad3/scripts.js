const form = document.getElementById("form");
const firstName = document.getElementById("fname");
const lastName = document.getElementById("about");
const email = document.getElementById("opening");


form.addEventListener("submit", (event) => {
  event.preventDefault();
  checkInputs();
});

function checkInputs() {
  const nameValue = fname.value.trim();
  const aboutValue = about.value.trim();
  const openingValue = Opening.value.trim();


  if (
    nameValue === "" ||
    about.value === "" ||
    Opening.Value === "" ||
    ) 
    }
  
    if (fnameValue === "") {
      setError(fname, " Please input your company's name");
    } else {
      setSuccess(fname);
    }

    if (aboutValue === "") {
      setError(about, "This field cannot be empty");
    } else {
      setSuccess(about);
    }

    if (openingValue === "") {
      setError(Opening, "Looks like this is not a valid time and date");
    } else {
      setSuccess(opening);
    }


function setError(input, message) {
  const formControl = input.parentElement;
  const small = formControl.querySelector("small");

  small.innerText = message;

  formControl.className = "form-control error";
  formControl.style.marginBottom = "1.5rem";
}

      function setSuccess(input, message) {
          const formControl = input.parentElement;
          formControl.className = "form-control success";
      }
