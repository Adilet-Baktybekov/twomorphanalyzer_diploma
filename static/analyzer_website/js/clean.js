const btn = document.getElementById('btn');

btn.addEventListener('click', function handleClick(event) {
  // 👇️ if you are submitting a form (prevents page reload)
  event.preventDefault();

  const word = document.getElementById('wd');

  // Send value to server
  console.log(word.value);

  // 👇️ clear input field
  word.value = '';
});