console.log('medium/main')


const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalTitle = document.getElementById('modal-title-confirm')
const modalBody = document.getElementById('modal-body-confirm')
const startButton = document.getElementById('start-button')

const url = window.location.href
console.log(url)

modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {
  const pk = modalBtn.getAttribute('data-pk')
  const name = modalBtn.getAttribute('data-quiz')
  const numQuestions = modalBtn.getAttribute('data-questions')
  const scoreToPass = modalBtn.getAttribute('data-pass')
  const time = modalBtn.getAttribute('data-time')

  modalTitle.innerHTML = `${name}`

  modalBody.innerHTML = `
 
  <div>
  <ul>
   
    <li>number of questions: <b>${numQuestions}</b></li>
    <li>score to pass: <b>${scoreToPass}</b></li>
    <li>time: <b>${time}</b></li>
  </ul>
</div>
  `
  startButton.addEventListener('click', () => {
    window.location.href = url + pk
  })
}))