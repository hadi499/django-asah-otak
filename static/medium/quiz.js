console.log('medium/quiz');


const quizBox = document.getElementById('quiz-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const timerBox = document.getElementById('timer-box')
const wrapTimer = document.getElementById('wrap-timer')
const startLagi = document.getElementById('start-lagi')
const url = window.location.href
console.log(url)



const activateTimer = (timeInSeconds) => {
  let seconds = timeInSeconds; // Total detik

  const updateDisplay = () => {
    let displaySeconds;

    // Format detik agar selalu dua digit
    if (seconds.toString().length < 2) {
      displaySeconds = '0' + seconds;
    } else {
      displaySeconds = seconds;
    }

    // Menampilkan detik di dalam elemen timerBox
    timerBox.innerHTML = `<b class="text-primary">${displaySeconds}</b>`;
  };

  // Tampilkan detik awal
  updateDisplay();

  const timer = setInterval(() => {
    seconds--;

    // Hentikan timer jika waktu habis
    if (seconds < 0) {
      clearInterval(timer);
      wrapTimer.classList.add('border-danger');
      timerBox.innerHTML = `<b class="text-danger rounded">00</b>`;
      sendData();
    } else {
      updateDisplay();
    }
  }, 1000);

  // Menghentikan timer saat form di-submit
  const stopTimerOnSubmit = () => {
    clearInterval(timer);
    console.log('Timer dihentikan karena submit');
  };

  // Tambahkan event listener untuk submit pada form
  quizForm.addEventListener('submit', stopTimerOnSubmit);
};


// Ambil pertanyaan dan jawaban
$.ajax({
  type: 'GET',
  url: `${url}data`,
  success: function (response) {
    console.log(response)
    const data = response.data
    data.forEach(el => {
      for (const [question, answers] of Object.entries(el)) {
        // Membuat div pembungkus untuk pertanyaan dan jawabannya
        let questionDiv = `
          <div class="mb-3 border " style="width: 150px;">
            <div class="text-center mb-2 bg-primary-subtle py-2">
              <b>${question}</b>
            </div>
            <div>
        `;

        // Menambahkan jawaban ke dalam div pembungkus
        answers.forEach(answer => {
          questionDiv += `
            <div class="px-3  mb-2 ">
              <input type="radio" class="ans form-check-input" id="${question}-${answer}" name="${question}" value="${answer}">
              <label for="${question}-${answer}">${answer}</label>
            </div>
          `;
        });

        // Menutup div pembungkus
        questionDiv += `
            </div>
          </div>
        `;

        // Menambahkan div pembungkus ke dalam quizBox
        quizBox.innerHTML += questionDiv;
      }
    });

    activateTimer(response.time)
  },
  error: function (error) {
    console.log(error)
  }
});



// send data
const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const sendData = () => {
  const element = [...document.getElementsByClassName('ans')]
  const data = {}
  data['csrfmiddlewaretoken'] = csrf[0].value
  element.forEach(el => {
    if (el.checked) {
      data[el.name] = el.value
    } else {
      if (!data[el.name]) {
        data[el.name] = null
      }
    }
  })
  $.ajax({
    type: 'POST',
    url: `${url}save/`,
    data: data,
    success: function (response) {
      console.log(response)
      const results = response.results
      console.log(results)
      quizForm.classList.add('not-visible')
      const lulus = `<div class="text-primary " >😁  Lulus, score: ${response.score}<div> `
      const gagal = `<div class="me-3 text-danger " >🥵  Gagal, score: ${response.score}</div>`

      // scoreBox.innerHTML = `${response.passed ? 'Selamat anda lulus, Nilai kamu adalah   ' : 'Ups...Kamu gagal, Nilai kamu adalah '} `
      scoreBox.innerHTML = `${response.passed ? lulus : gagal} `
      console.log(url)
      startLagi.innerHTML = `</div><a href="${url}" class="btn btn-outline-primary">start game lagi</a></span>`



      results.forEach(res => {
        const resDiv = document.createElement('div')
        for (const [question, resp] of Object.entries(res)) {
          resDiv.innerHTML += question
          const cls = ['container', 'p-3', 'text-light', 'h6', 'mt-4']
          resDiv.classList.add(...cls)
          resDiv.style.width = '300px'

          if (resp == 'not answered') {
            resDiv.innerHTML += ' , Tidak dijawab'
            resDiv.classList.add('bg-danger')
          } else {
            const answer = resp['answered']
            const correct = resp['correct_answer']

            if (answer == correct) {
              resDiv.classList.add('bg-success')
              resDiv.innerHTML += ` | dijawab: ${answer}`
            } else {
              resDiv.classList.add('bg-danger')
              resDiv.innerHTML += ` | dijawab: ${answer}`
              // resDiv.innerHTML += ` | kunci jawaban: ${correct}`
            }

          }
        }
        // const body = document.getElementsByTagName('body')[0]
        resultBox.append(resDiv)
      })

    },
    error: function (error) {
      console.log(error)
    }
  })
}


quizForm.addEventListener('submit', e => {
  e.preventDefault()
  sendData()
  // wrapTimerBox.classList.add('not-visible')
  // alertTime.classList.add('not-visible')
})
